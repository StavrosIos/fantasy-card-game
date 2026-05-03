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
    gs.ai.health -= attacker.attack;
    log(attacker.name + ' attacks AI for ' + attacker.attack + '!');
  } else {
    // Attack enemy minion
    const defender = gs.ai.board.find(c => c.id === targetId);
    if (!defender) return;

    let atk = attacker.attack;
    if (attacker.ability === 'Poison') atk += 1;

    defender.health -= atk;
    attacker.health -= defender.attack;
    log(attacker.name + ' attacks ' + defender.name + '! (' + atk + ' vs ' + defender.attack + ')');
  }

  attacker.hasAttacked = true;
  gs.attackerId = null;

  cleanupDeadMinions();
  checkWinCondition();
  render();
}

/** AI attacks with its selected minion.
 *  @param {number|null} targetId — ID of player board card, or null for hero */
function executeAiAttack(targetId) {
  const attacker = gs.ai.board.find(c => c.id === gs._aiAttackerId);
  if (!attacker) return;

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
    gs.player.health -= attacker.attack;
    log('AI ' + attacker.name + ' attacks you for ' + attacker.attack + '!');
  } else {
    // Attack player minion
    const defender = gs.player.board.find(c => c.id === targetId);
    if (!defender) return;

    let atk = attacker.attack;
    if (attacker.ability === 'Poison') atk += 1;

    defender.health -= atk;
    attacker.health -= defender.attack;
    log('AI ' + attacker.name + ' attacks ' + defender.name + '!');
  }

  attacker.hasAttacked = true;
  gs._aiAttackerId = null;

  cleanupDeadMinions();
  checkWinCondition();
  render();
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
  card.canAttack = (card.ability === 'Rush' || card.ability === 'Pierce' || card.ability === 'Flame Rush');
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
  const enemy = owner === 'player' ? gs.ai : gs.player;

  switch (card.ability) {
    case 'Fireball': {
      if (enemy.board.length > 0) {
        const target = enemy.board[Math.floor(Math.random() * enemy.board.length)];
        target.health -= 1;
        log(card.name + ' fires at ' + target.name + '!');
      } else {
        enemy.health -= 1;
        log(card.name + ' hits the hero for 1!');
      }
      break;
    }

    case 'Inferno': {
      enemy.board.forEach(c => { c.health -= 2; });
      log(card.name + ' unleashes Inferno!');
      break;
    }

    case 'Freeze': {
      const targets = enemy.board.filter(c => !c.frozen);
      if (targets.length > 0) {
        const target = targets[Math.floor(Math.random() * targets.length)];
        target.frozen = true;
        log(card.name + ' freezes ' + target.name + '!');
      }
      break;
    }

    case 'Chill': {
      const targets = enemy.board.filter(c => c.attack > 0);
      if (targets.length > 0) {
        const target = targets[Math.floor(Math.random() * targets.length)];
        target.attack -= 1;
        log(card.name + ' chills ' + target.name + '!');
      }
      break;
    }

    case 'Cleave': {
      const board = owner === 'player' ? gs.player.board : gs.ai.board;
      board.forEach(c => { if (c.id !== card.id) c.health -= 1; });
      log(card.name + ' cleaves all other minions!');
      break;
    }

    case 'Heal': {
      if (owner === 'player') {
        gs.player.health = Math.min(20, gs.player.health + 2);
      } else {
        gs.ai.health = Math.min(20, gs.ai.health + 2);
      }
      log(card.name + ' heals for 2 HP!');
      break;
    }

    case 'Shield': {
      card.health += 1;
      card.maxHealth += 1;
      log(card.name + ' gains a shield! (+1 HP)');
      break;
    }

    case 'Drain': {
      if (owner === 'player') {
        gs.ai.health -= 2;
        gs.player.health = Math.min(20, gs.player.health + 2);
      } else {
        gs.player.health -= 2;
        gs.ai.health = Math.min(20, gs.ai.health + 2);
      }
      log(card.name + ' drains life!');
      break;
    }

    case 'Summon Ice': {
      const board = owner === 'player' ? gs.player.board : gs.ai.board;
      board.push(createCardInstance({ name:'Frost Elemental', manaCost:0, attack:1, health:2, archetype:'Ice Sorcerer', ability:'', abilityDesc:'', art:'🧊' }));
      log(card.name + ' summons a Frost Elemental!');
      break;
    }

    case 'Flame Rush': {
      card.canAttack = true; // Charge
      if (owner === 'player') { gs.player.health -= 1; } else { gs.ai.health -= 1; }
      log(card.name + ' rushes in!');
      break;
    }

    case 'Gust': {
      enemy.board.forEach(c => { c.health -= 1; });
      log(card.name + ' summons a gust!');
      break;
    }

    case 'Stealth': {
      card.stealthed = true;
      log(card.name + ' becomes stealthed!');
      break;
    }

    case 'Taunt': {
      card.taunt = true;
      log(card.name + ' gains Taunt!');
      break;
    }

    case 'Pierce': {
      card.canAttack = true; // Charge
      break;
    }

    case 'Rush': {
      card.canAttack = true; // Already set, but explicit
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

    // Deathrattle abilities — handled in cleanupDeadMinions
    case 'Burn':
    case 'Reborn':
    case 'Return':
      // No battlecry effect
      break;

    default: {
      if (card.abilities && card.abilities.length > 0) {
        card.abilities.forEach(abilityStr => {
          const lower = abilityStr.toLowerCase();

          // Divine Strategy: Draw 2 cards
          if (lower.includes("draw") && lower.includes("cards")) {
            const match = lower.match(/draw (\d+) cards?/);
            const count = match ? parseInt(match[1]) : 1;
            const myState = owner === 'player' ? gs.player : gs.ai;
            for (let i = 0; i < count; i++) {
              if (myState.deck.length > 0) myState.hand.push(myState.deck.pop());
            }
            log(card.name + " triggers: Draw " + count + " cards");
          }

          // Shield of Aegis: Prevent 5 damage to your hero
          if (lower.includes("prevent") && lower.includes("damage")) {
            const match = lower.match(/prevent (\d+) damage/);
            const amount = match ? parseInt(match[1]) : 2;
            const myState = owner === 'player' ? gs.player : gs.ai;
            myState.health = Math.min(20, myState.health + amount);
            log(card.name + " triggers: Protects hero (Restored " + amount + " HP)");
          }

          // Thunderbolt: Deal 5 damage to all enemy minions
          if (lower.includes("deal") && lower.includes("damage to all enemy minions")) {
            const match = lower.match(/deal (\d+) damage/);
            const damage = match ? parseInt(match[1]) : 2;
            enemy.board.forEach(c => c.health -= damage);
            log(card.name + " triggers: Deal " + damage + " damage to ALL enemies");
          }
          
          // Generic "Deal X damage to a minion"
          else if (lower.includes("deal") && lower.includes("damage to a minion")) {
             const match = lower.match(/deal (\d+) damage/);
             const damage = match ? parseInt(match[1]) : 2;
             if (enemy.board.length > 0) {
                const target = enemy.board[Math.floor(Math.random() * enemy.board.length)];
                target.health -= damage;
                log(card.name + " fires at " + target.name + " for " + damage + "!");
             }
          }

          // Restore X health to your hero
          if (lower.includes("restore") && lower.includes("health to your hero")) {
            const match = lower.match(/restore (\d+) health/);
            const amount = match ? parseInt(match[1]) : 3;
            const myState = owner === 'player' ? gs.player : gs.ai;
            myState.health = Math.min(20, myState.health + amount);
            log(card.name + " triggers: Restore " + amount + " HP");
          }
        });
      } else {
        log(card.name + ' plays.');
      }
    }
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
