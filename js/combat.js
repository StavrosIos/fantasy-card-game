/* ================================================================
   combat.js — Combat, Battlecry & Deathrattle
   
   Handles all card interactions: playing cards from hand,
   selecting attackers on the board, executing attacks, and
   resolving abilities (battlecry + deathrattle).
   
   Functions:
     onHandCardClick()      — click a card in hand to play it
     onBoardCardClick()     — select attacker or target on board
     executePlayerAttack()  — player attacks with selected minion
     executeAiAttack()      — AI attacks with selected minion
     playCard()             — move card from hand to board
     applyBattlecry()       — resolve on-play abilities
     applyDeathrattle()     — resolve death abilities
     cleanupDeadMinions()   — remove dead minions, process deaths
   ================================================================ */

/* --- Player Interactions --- */

/** Click on a card in player's hand — play it immediately if possible. */
function onHandCardClick(idx) {
  const card = gs.player.hand[idx];

  if (gs.turn !== 'player' || gs.phase === 'aiThinking') {
    log("Not your turn!");
    return;
  }

  // Check mana
  if (gs.player.mana < card.manaCost) {
    log("Not enough mana for " + card.name + ' (need ' + card.manaCost + ')');
    return;
  }

  // Check board space (max 7)
  if (gs.player.board.length >= 7) {
    log('Your board is full!');
    return;
  }

  // If we have an attacker selected, deselect it (playing a card is higher priority)
  if (gs.attackerId !== null) {
    gs.attackerId = null;
  }

  // Play the card immediately
  playCard(idx, 'player');
  render();
}

/** Click on a board card — select attacker (own) or target (enemy). */
function onBoardCardClick(card, isAI) {
  if (gs.turn === 'player') {
    // Player's turn: clicking own board card selects it as attacker
    if (!isAI) {
      // Clicking own card — select/deselect as attacker
      if (gs.attackerId === card.id) {
        gs.attackerId = null;
        log('');
      } else if (card.frozen) {
        log(card.name + ' is frozen and can\'t attack!');
      } else if (card.hasAttacked) {
        log(card.name + ' has already attacked this turn.');
      } else {
        gs.attackerId = card.id;
        log('Selected ' + card.name + '. Click an enemy minion or hero to attack.');
      }
      render();
      return;
    }

    // Clicking AI board card — attack it (if we have an attacker selected)
    if (isAI && gs.attackerId !== null) {
      executePlayerAttack(card.id);
    }
  }

  // AI's turn: clicking player board card — target it for AI attack
  if (gs.turn === 'ai' && !isAI) {
    executeAiAttack(card.id);
  }
}

/* --- Combat Execution --- */

/** Player attacks with their selected minion.
 *  @param {number|null} targetId — ID of enemy board card, or null for hero */
function executePlayerAttack(targetId) {
  const attacker = gs.player.board.find(c => c.id === gs.attackerId);
  if (!attacker) return;

  const attackerEl = document.querySelector(`[data-id="${attacker.id}"]`);
  let defenderEl = null;

  // Check taunt: must attack taunt minions first
  const enemyTaunts = gs.ai.board.filter(c => c.taunt);
  if (enemyTaunts.length > 0 && targetId !== null) {
    const target = gs.ai.board.find(c => c.id === targetId);
    if (target && !target.taunt) {
      log('Must attack a taunting minion first!');
      return;
    }
  }

  if (targetId === null) {
    // Attack AI hero
    defenderEl = document.querySelector('.ai-board .hero-card');
    animateAttack(attackerEl, defenderEl, () => {
      gs.ai.health -= attacker.attack;
      log(attacker.name + ' attacks AI for ' + attacker.attack + '!');
      finalizeAttack(attacker);
    });
  } else {
    // Attack enemy minion
    const defender = gs.ai.board.find(c => c.id === targetId);
    if (!defender) return;

    defenderEl = document.querySelector(`[data-id="${defender.id}"]`);

    animateAttack(attackerEl, defenderEl, () => {
      let atk = attacker.attack;
      if (attacker.ability === 'Poison') atk += 1;

      defender.health -= atk;
      attacker.health -= defender.attack;
      log(attacker.name + ' attacks ' + defender.name + '! (' + atk + ' vs ' + defender.attack + ')');
      finalizeAttack(attacker);
    });
  }
}

/** AI attacks with its selected minion.
 *  @param {number|null} targetId — ID of player board card, or null for hero */
function executeAiAttack(targetId) {
  const attacker = gs.ai.board.find(c => c.id === gs._aiAttackerId);
  if (!attacker) return;

  const attackerEl = document.querySelector(`[data-id="${attacker.id}"]`);
  let defenderEl = null;

  // Check taunt: must attack player taunts first
  const playerTaunts = gs.player.board.filter(c => c.taunt);
  if (playerTaunts.length > 0 && targetId !== null) {
    const target = gs.player.board.find(c => c.id === targetId);
    if (target && !target.taunt) {
      log('Must attack a taunting minion first!');
      return;
    }
  }

  if (targetId === null) {
    // Attack player hero
    defenderEl = document.querySelector('.player-board .hero-card');
    animateAttack(attackerEl, defenderEl, () => {
      gs.player.health -= attacker.attack;
      log('AI ' + attacker.name + ' attacks you for ' + attacker.attack + '!');
      finalizeAttack(attacker);
    });
  } else {
    // Attack player minion
    const defender = gs.player.board.find(c => c.id === targetId);
    if (!defender) return;

    defenderEl = document.querySelector(`[data-id="${defender.id}"]`);
    animateAttack(attackerEl, defenderEl, () => {
      let atk = attacker.attack;
      if (attacker.ability === 'Poison') atk += 1;

      defender.health -= atk;
      attacker.health -= defender.attack;
      log('AI ' + attacker.name + ' attacks ' + defender.name + '!');
      finalizeAttack(attacker);
    });
  }
}

/** Finalize attack state changes and render */
function finalizeAttack(attacker) {
  attacker.hasAttacked = true;
  gs.attackerId = null;
  gs._aiAttackerId = null;

  cleanupDeadMinions();
  checkWinCondition();
  render();
}

/** Animate an attack from one element to another. */
function animateAttack(attackerEl, defenderEl, onImpact) {
  if (!attackerEl || !defenderEl) {
    onImpact();
    return;
  }

  const rectA = attackerEl.getBoundingClientRect();
  const rectB = defenderEl.getBoundingClientRect();

  const deltaX = rectB.left + rectB.width / 2 - (rectA.left + rectA.width / 2);
  const deltaY = rectB.top + rectB.height / 2 - (rectA.top + rectA.height / 2);

  attackerEl.classList.add('attacking');
  attackerEl.style.transform = `translate(${deltaX}px, ${deltaY}px) scale(1.1)`;

  setTimeout(() => {
    // Impact
    defenderEl.classList.add('hit');
    onImpact();

    setTimeout(() => {
      attackerEl.style.transform = '';
      attackerEl.classList.remove('attacking');
      defenderEl.classList.remove('hit');
    }, 200);
  }, 200);
}

/* --- Play Card — Move from Hand to Board --- */

/** Move a card from hand to board, pay mana, apply battlecry.
 *  @param {number} handIdx — index in the player's or AI's hand array
 *  @param {string} owner — 'player' or 'ai'
 *  @returns {boolean} true if card was played successfully */
function playCard(handIdx, owner) {
  const hand = owner === 'player' ? gs.player.hand : gs.ai.hand;
  const board = owner === 'player' ? gs.player.board : gs.ai.board;

  if (handIdx < 0 || handIdx >= hand.length) return false;
  const card = hand[handIdx];

  // Check mana
  if (owner === 'player') {
    if (gs.player.mana < card.manaCost) return false;
  } else {
    if (gs.ai.mana < card.manaCost) return false;
  }

  // Check board space (max 7)
  if (board.length >= 7) return false;

  // Pay mana
  if (owner === 'player') { gs.player.mana -= card.manaCost; }
  else { gs.ai.mana -= card.manaCost; }

  // Remove from hand
  hand.splice(handIdx, 1);

  // Add to board — set canAttack based on Rush/Charge abilities
  const lowerAbilities = card.abilities.map(a => a.toLowerCase());
  card.canAttack = lowerAbilities.some(a => a.includes('rush') || a.includes('pierce') || a.includes('charge') || a.includes('flight'));
  board.push(card);

  // Apply battlecry
  applyBattlecry(card, owner);

  log((owner === 'player' ? 'You play ' : 'AI plays ') + card.name);

  // Clean up any deaths from battlecry
  cleanupDeadMinions();

  return true;
}

/* --- Battlecry Abilities (On-Play Effects) --- */

/** Apply battlecry abilities when a card is played.
 *  @param {Object} card — the card object being played
 *  @param {string} owner — 'player' or 'ai' */
function applyBattlecry(card, owner) {
  const abilities = card.abilities || [];

  if (abilities.length === 0) {
    log(card.name + ' enters the battlefield.');
    return;
  }

  abilities.forEach(abilityStr => {
    // Only process "immediate" abilities (Battlecries)
    // Avoid abilities that trigger "at the start/end of turn" or "each turn"
    const lower = abilityStr.toLowerCase();
    if (lower.includes('turn') && !lower.includes('first turn')) return;

    processAbilityEffect(card, abilityStr, owner);
  });
}

/** Internal helper to parse and execute an ability string. */
function processAbilityEffect(card, abilityStr, owner) {
  const lower = abilityStr.toLowerCase();
  const enemy = owner === 'player' ? gs.ai : gs.player;
  const myState = owner === 'player' ? gs.player : gs.ai;

  let triggered = false;
  let effectName = "";

  // 1. Draw cards
  if (lower.includes('draw')) {
    const match = lower.match(/draw (\d+)/);
    const count = match ? parseInt(match[1]) : 1;
    for (let i = 0; i < count; i++) {
      if (myState.deck.length > 0) myState.hand.push(myState.deck.pop());
    }
    effectName = `Draw ${count}`;
    triggered = true;
  }

  // 2. Deal Damage
  if (lower.includes('deal')) {
    const match = lower.match(/deal (\d+)/);
    const damage = match ? parseInt(match[1]) : 1;

    if (lower.includes('all enemies') || lower.includes('everything')) {
      enemy.board.forEach(c => c.health -= damage);
      enemy.health -= damage;
      myState.board.forEach(c => { if (c.id !== card.id) c.health -= damage; });
      if (lower.includes('everything')) myState.health -= damage;
      effectName = "Area Blast";
    } else if (lower.includes('all enemy minions')) {
      enemy.board.forEach(c => c.health -= damage);
      effectName = "Enemy Sweep";
    } else if (lower.includes('a minion') || lower.includes('enemy minion')) {
      if (enemy.board.length > 0) {
        const target = enemy.board[Math.floor(Math.random() * enemy.board.length)];
        target.health -= damage;
        effectName = `Strike ${target.name}`;
      }
    } else if (lower.includes('random enemy')) {
      if (enemy.board.length > 0 && Math.random() < 0.5) {
        const target = enemy.board[Math.floor(Math.random() * enemy.board.length)];
        target.health -= damage;
      } else {
        enemy.health -= damage;
      }
      effectName = "Random Shot";
    } else if (lower.includes('any target')) {
        // AI chooses random enemy, player could have UI but for now random
        if (enemy.board.length > 0 && Math.random() < 0.5) {
            const target = enemy.board[Math.floor(Math.random() * enemy.board.length)];
            target.health -= damage;
        } else {
            enemy.health -= damage;
        }
        effectName = "Precision Strike";
    }
    triggered = true;
  }

  // 3. Heal / Restore
  if (lower.includes('restore') || lower.includes('heal')) {
    const match = lower.match(/(\d+) health/);
    const amount = match ? parseInt(match[1]) : 2;

    if (lower.includes('your hero') || lower.includes('hero')) {
      myState.health = Math.min(20, myState.health + amount);
      effectName = "Heal Hero";
    } else if (lower.includes('all friends')) {
      myState.board.forEach(c => c.health = Math.min(c.maxHealth, c.health + amount));
      myState.health = Math.min(20, myState.health + amount);
      effectName = "Group Heal";
    }
    triggered = true;
  }

  // 4. Summon tokens
  if (lower.includes('summon')) {
    const board = myState.board;
    if (board.length < 7) {
      if (lower.includes('skeleton')) {
        board.push(createCardInstance({ name:'Skeleton', manaCost:0, attack:1, health:1, mythology: card.mythology, abilities:[] }));
      } else if (lower.includes('construct')) {
        board.push(createCardInstance({ name:'Construct', manaCost:0, attack:2, health:1, mythology: card.mythology, abilities:[] }));
      } else if (lower.includes('spirit')) {
        board.push(createCardInstance({ name:'Spirit', manaCost:0, attack:2, health:2, mythology: card.mythology, abilities:[] }));
      } else if (lower.includes('valkyrie')) {
        board.push(createCardInstance({ name:'Valkyrie', manaCost:0, attack:1, health:2, mythology: card.mythology, abilities:[] }));
      }
      effectName = "Summoning";
      triggered = true;
    }
  }

  // 5. Stat Boosts
  if (lower.includes('give') || lower.includes('gain')) {
    const atkMatch = lower.match(/\+(\d+) attack/);
    const hpMatch = lower.match(/\+(\d+) health/);
    const atk = atkMatch ? parseInt(atkMatch[1]) : 0;
    const hp = hpMatch ? parseInt(hpMatch[1]) : 0;

    if (lower.includes('all friendly minions') || lower.includes('your other minions')) {
        myState.board.forEach(c => {
            if (c.id !== card.id) {
                c.attack += atk;
                c.health += hp;
                c.maxHealth += hp;
            }
        });
        effectName = "War Cry";
    } else if (lower.includes('a minion')) {
        if (myState.board.length > 1) {
            const target = myState.board.find(c => c.id !== card.id) || myState.board[0];
            target.attack += atk;
            target.health += hp;
            target.maxHealth += hp;
            effectName = `Buff ${target.name}`;
        }
    }
    triggered = true;
  }

  // Keywords
  if (lower.includes('taunt')) { card.taunt = true; effectName="Taunt"; triggered=true; }
  if (lower.includes('stealth')) { card.stealthed = true; effectName="Stealth"; triggered=true; }
  if (lower.includes('freeze')) {
      if (enemy.board.length > 0) {
          const target = enemy.board[Math.floor(Math.random() * enemy.board.length)];
          target.frozen = true;
          effectName = `Freeze ${target.name}`;
          triggered = true;
      }
  }

  if (triggered) {
    log(`${card.name} triggers: ${effectName || abilityStr}`);
    showAbilityEffect(card);
  }
}

/** Visual feedback for ability triggers */
function showAbilityEffect(card) {
    const el = document.querySelector(`[data-id="${card.id}"]`);
    if (el) {
        el.classList.add('trigger-ability');
        setTimeout(() => el.classList.remove('trigger-ability'), 800);
    }
}

/* --- Deathrattle Abilities (On-Death Effects) --- */

/** Apply deathrattle abilities when a minion dies.
 *  @param {Object} card — the dying card object
 *  @param {string} owner — 'player' or 'ai' */
function applyDeathrattle(card, owner) {
  const enemy = owner === 'player' ? gs.ai : gs.player;

  switch (card.ability) {
    case 'Burn': {
      enemy.board.forEach(c => { c.health -= 2; });
      log(card.name + ' burns! 2 damage to all enemies.');
      break;
    }

    case 'Reborn': {
      const revived = createCardInstance(findTemplateFor(card));
      revived.health = 1;
      if (owner === 'player') { gs.player.hand.push(revived); } else { gs.ai.hand.push(revived); }
      log(card.name + ' is reborn with 1 HP!');
      break;
    }

    case 'Return': {
      if (owner === 'player') { gs.player.hand.push(card); } else { gs.ai.hand.push(card); }
      log(card.name + ' returns to hand!');
      break;
    }

    case 'Swarm': {
      const board = owner === 'player' ? gs.player.board : gs.ai.board;
      for (let s = 0; s < 2; s++) {
        board.push(createCardInstance({ name:'Skeleton', manaCost:0, attack:1, health:1, archetype:'Undead', ability:'', abilityDesc:'', art:'💀' }));
      }
      log('Skeletons rise from the dead!');
      break;
    }
  }
}

/* --- Cleanup Dead Minions --- */

/** Remove all dead minions from both boards and process their deathrattles.
 *  Iterates backwards to avoid index-shift issues when splicing. */
function cleanupDeadMinions() {
  // Process AI board deaths (backwards)
  for (let i = gs.ai.board.length - 1; i >= 0; i--) {
    const card = gs.ai.board[i];
    if (card.health <= 0) {
      applyDeathrattle(card, 'ai');
      gs.ai.board.splice(i, 1);
    }
  }

  // Process player board deaths (backwards)
  for (let i = gs.player.board.length - 1; i >= 0; i--) {
    const card = gs.player.board[i];
    if (card.health <= 0) {
      applyDeathrattle(card, 'player');
      gs.player.board.splice(i, 1);
    }
  }
}
