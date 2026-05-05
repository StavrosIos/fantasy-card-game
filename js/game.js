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
    title.textContent = t('victoryTitle');
    title.className = 'win';
    sub.textContent = t('victorySub');
    const sound = document.getElementById('victory-sound');
    if (sound) sound.play().catch(e => console.log("Audio play failed:", e));
  } else {
    title.textContent = t('defeatTitle');
    title.className = 'lose';
    sub.textContent = t('defeatSub');
    const sound = document.getElementById('defeat-sound');
    if (sound) sound.play().catch(e => console.log("Audio play failed:", e));
  }

  overlay.classList.add('active');
}

/* --- Initialization --- */

/** Initialize a new game: reset state, build decks, draw hands.
 *  Called automatically on page load and when "Play Again" is clicked. */
async function initGame() {
  // First, load templates if they haven't been loaded
  if (CARD_TEMPLATES.length === 0) {
    log(t('loadingCards'));
    await loadCardTemplates();
  }

  // Randomly pick hero images for player and AI
  const playerHeroImage = HERO_IMAGES[Math.floor(Math.random() * HERO_IMAGES.length)];
  const aiHeroImage = HERO_IMAGES[Math.floor(Math.random() * HERO_IMAGES.length)];

  // Reset state
  gs = {
    player: { health:20, mana:0, maxMana:1, deck:[], hand:[], board:[], heroImage: playerHeroImage },
    ai:     { health:20, mana:0, maxMana:1, deck:[], hand:[], board:[], heroImage: aiHeroImage },
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

  updateStaticTexts();
  log(t('gameStarted'));
  render();
  startTimer();
}

function startGameFromIntro() {
  const intro = document.getElementById('intro-screen');
  if (intro) intro.classList.remove('active');
  initGame();
}

// Show intro first, only initialize static translated text on load
updateStaticTexts();

window.startGameFromIntro = startGameFromIntro;
