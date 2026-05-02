/* ================================================================
   game.js — Win Condition & Initialization
   
   The entry point that wires everything together:
     checkWinCondition() — check if either player reached 0 HP
     showGameOver()      — display the victory/defeat overlay
     initGame()          — reset state, build decks, start game
   
   Called automatically when the page loads.
   ================================================================ */

/* --- Win Condition --- */

/** Check if either player has reached 0 HP.
 *  Renders the game state and shows the game-over overlay if someone won.
 *  @returns {boolean} true if the game ended */
function checkWinCondition() {
  if (gs.ai.health <= 0) {
    gs.ai.health = 0;
    render();
    showGameOver(true);
    return true;
  }

  if (gs.player.health <= 0) {
    gs.player.health = 0;
    render();
    showGameOver(false);
    return true;
  }

  return false;
}

/** Display the game-over overlay with win/lose message.
 *  @param {boolean} playerWon — true if the player won */
function showGameOver(playerWon) {
  const overlay = document.getElementById('game-over');
  const title = document.getElementById('game-over-title');
  const sub = document.getElementById('game-over-sub');

  if (playerWon) {
    title.textContent = '🏆 VICTORY!';
    title.className = 'win';
    sub.textContent = 'You defeated the AI opponent!';
  } else {
    title.textContent = '💀 DEFEAT';
    title.className = 'lose';
    sub.textContent = 'The AI has bested you. Try again!';
  }

  overlay.classList.add('active');
}

/* --- Initialization --- */

/** Initialize a new game: reset state, build decks, draw hands.
 *  Called automatically on page load and when "Play Again" is clicked. */
function initGame() {
  // Reset state
  gs = {
    player: { health:20, mana:0, maxMana:1, deck:[], hand:[], board:[] },
    ai:     { health:20, mana:0, maxMana:1, deck:[], hand:[], board:[] },
    turn: 'player',
    phase: 'main',
    selectedHandIdx: null,
    attackerId: null,
    _aiAttackerId: null,
    turnNumber: 1,
  };

  nextCardId = 1;

  // Build decks
  gs.player.deck = buildDeck();
  gs.ai.deck = buildDeck();

  // Draw initial hands (3 cards each)
  for (let i = 0; i < 3; i++) {
    if (gs.player.deck.length > 0) gs.player.hand.push(gs.player.deck.pop());
    if (gs.ai.deck.length > 0) gs.ai.hand.push(gs.ai.deck.pop());
  }

  // Hide game over overlay
  document.getElementById('game-over').classList.remove('active');

  log('Game started! You draw 3 cards. Click a card to play it.');
  render();
}

// Start the game on load
initGame();
