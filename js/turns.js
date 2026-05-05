/* ================================================================
   turns.js — Turn Management & AI Logic
   
   Controls the flow of turns: player actions, AI decision-making,
   mana/health progression, and end-of-turn effects.
   
   Functions:
     endPlayerTurn()    — player clicks "End Turn" button
     startAiTurn()      — begin AI's turn (draw, gain mana)
     aiTurnStep()       — one step of AI action (play card or attack)
     processEndOfTurn() — resolve end-of-turn effects (Regen, Heal)
   ================================================================ */

/* --- Player Turn End --- */

/** Player ends their turn — triggers AI's turn.
 *  Called when the player clicks the "End Turn" button. */
function endPlayerTurn() {
  if (gs.turn !== 'player' || gs.phase === 'aiThinking') return;

  stopTimer();

  // Process end-of-turn effects for player board
  processEndOfTurn('player');

  gs.turn = 'ai';
  gs.attackerId = null;

  // AI turn begins
  startAiTurn();
}

/* --- AI Turn Start --- */

/** Start the AI's turn: draw a card, gain mana, unfreeze minions.
 *  Then begin the AI's action sequence with a delay for readability. */
function startAiTurn() {
  gs.phase = 'aiThinking';

  // Draw a card
  if (gs.ai.deck.length > 0) {
    gs.ai.hand.push(gs.ai.deck.pop());
  }

  // Gain mana (max 10)
  gs.ai.maxMana = Math.min(10, gs.ai.maxMana + 1);
  gs.ai.mana = gs.ai.maxMana;

  // Unfreeze AI minions
  gs.ai.board.forEach(c => { c.frozen = false; });

  // Reset attack flags
  gs.ai.board.forEach(c => { c.hasAttacked = false; });

  render();
  log(t('aiThinking'));

  // AI takes its turn with delays for readability
  setTimeout(() => aiTurnStep(), 800);
}

/* --- AI Turn Steps --- */

/** One step of the AI's turn: try to play a card, then attack with minions.
 *  Recurses until the AI has no more actions, then ends its turn. */
function aiTurnStep() {
  // Check win condition first
  if (checkWinCondition()) return;

  // Try to play a card (greedy: most expensive affordable)
  const playableCards = gs.ai.hand
    .map((c, i) => ({ card: c, idx: i }))
    .filter(x => x.card.manaCost <= gs.ai.mana);

  if (playableCards.length > 0 && gs.ai.board.length < 7) {
    playableCards.sort((a, b) => b.card.manaCost - a.card.manaCost);
    const chosen = playableCards[0];

    // Play if board is empty or 70% chance
    const willPlay = gs.ai.board.length === 0 || Math.random() < 0.7;

    if (willPlay) {
      playCard(chosen.idx, 'ai');
      render();

      setTimeout(() => aiTurnStep(), 600);
      return;
    }
  }

  // AI attacks with all available minions
  const attackers = gs.ai.board.filter(c => !c.hasAttacked && !c.frozen);

  if (attackers.length > 0) {
    const attacker = attackers[Math.floor(Math.random() * attackers.length)];

    // Check if player has taunt minions
    const playerTaunts = gs.player.board.filter(c => c.taunt);

    if (playerTaunts.length > 0) {
      // Must attack taunt minion
      const target = playerTaunts[Math.floor(Math.random() * playerTaunts.length)];
      gs._aiAttackerId = attacker.id;
      executeAiAttack(target.id);
    } else if (gs.player.board.length > 0 && Math.random() < 0.6) {
      // Sometimes attack a minion (40% chance to attack hero instead)
      const target = gs.player.board[Math.floor(Math.random() * gs.player.board.length)];
      gs._aiAttackerId = attacker.id;
      executeAiAttack(target.id);
    } else {
      // Attack player hero
      gs._aiAttackerId = attacker.id;
      executeAiAttack(null);
    }

    attacker.hasAttacked = true;
    // Don't call render() here because the animation + finalizeAttack will do it
    // render(); 

    // Continue with next action after a delay that accounts for the attack animation (approx 400ms)
    setTimeout(() => aiTurnStep(), 1000);
    return;
  }

  // AI has finished attacking — end its turn, start player's turn
  processEndOfTurn('ai');

  gs.turn = 'player';
  gs.phase = 'main';
  gs.attackerId = null;

  // Player turn begins: draw, gain mana, unfreeze
  if (gs.player.deck.length > 0) {
    gs.player.hand.push(gs.player.deck.pop());
  }

  gs.player.maxMana = Math.min(10, gs.player.maxMana + 1);
  gs.player.mana = gs.player.maxMana;

  gs.player.board.forEach(c => { c.frozen = false; });
  gs.player.board.forEach(c => { c.hasAttacked = false; });

  gs.turnNumber++;
  render();
  log(t('yourTurn') + ' — ' + t('turnLabel') + ' ' + gs.turnNumber);
  
  // Only start timer for player
  if (gs.turn === 'player') {
    startTimer();
  }
}

/* --- Turn Timer --- */

/** Start the 20-second turn timer for the player. */
function startTimer() {
  stopTimer();
  gs.turnTimer = 20;
  render();

  gs.timerInterval = setInterval(() => {
    gs.turnTimer--;

    if (gs.turnTimer <= 3 && gs.turnTimer > 0) {
      const sound = document.getElementById('clock-sound');
      if (sound) {
        sound.currentTime = 0;
        sound.play().catch(e => console.log("Audio play failed:", e));
      }
    }

    if (gs.turnTimer <= 0) {
      gs.turnTimer = 0;
      stopTimer();
      log(t('timesUp'));
      endPlayerTurn();
    }
    renderTimer(); // Only update timer UI to prevent card jumping
  }, 1000);
}

/** Stop and clear the turn timer. */
function stopTimer() {
  if (gs.timerInterval) {
    clearInterval(gs.timerInterval);
    gs.timerInterval = null;
  }
}

/* --- End-of-Turn Effects --- */

/** Process end-of-turn effects for a player's board.
 *  @param {string} owner — 'player' or 'ai' */
function processEndOfTurn(owner) {
  const board = owner === 'player' ? gs.player.board : gs.ai.board;

  board.forEach(card => {
    const abilities = card.abilities || [];
    if (card.ability) abilities.unshift(card.ability);

    abilities.forEach(abilityStr => {
        const lower = abilityStr.toLowerCase();
        // Check for periodic effects: "each turn", "per turn", "start/end of turn"
        if (lower.includes('turn') && !lower.includes('first turn')) {
            processAbilityEffect(card, abilityStr, owner);
        }
    });
  });

  cleanupDeadMinions();
}
