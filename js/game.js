/* ================================================================
   game.js — Win Condition & Initialization
   
   The entry point that wires everything together:
     checkWinCondition() — check if either player reached 0 HP
     showGameOver()      — display the victory/defeat overlay
     initGame()          — reset state, build decks, start game
   
   Called automatically when the page loads.
   ================================================================ */

/* --- Win Condition --- */

function playVictoryFallbackChime() {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;

    const ctx = new AudioCtx();
    const now = ctx.currentTime;
    const notes = [523.25, 659.25, 783.99]; // C5, E5, G5

    notes.forEach((freq, i) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'triangle';
      osc.frequency.value = freq;

      gain.gain.setValueAtTime(0.0001, now + i * 0.14);
      gain.gain.exponentialRampToValueAtTime(0.16, now + i * 0.14 + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + i * 0.14 + 0.2);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(now + i * 0.14);
      osc.stop(now + i * 0.14 + 0.22);
    });
  } catch (e) {
    console.log('Fallback victory chime failed:', e);
  }
}

function playSoundById(audioId, fallbackFn) {
  const sound = document.getElementById(audioId);

  if (!sound) {
    if (fallbackFn) fallbackFn();
    return;
  }

  sound.currentTime = 0;
  const playPromise = sound.play();

  if (playPromise && typeof playPromise.catch === 'function') {
    playPromise.catch(e => {
      console.log('Audio play failed:', e);
      if (fallbackFn) fallbackFn();
    });
  }
}

/** Check if either player has reached 0 HP.
 *  Renders the game state and shows the game-over overlay if someone won.
 *  @returns {boolean} true if the game ended */
function checkWinCondition() {
  if (gs.ai.health <= 0) {
    gs.ai.health = 0;
    gs.isGameOver = true;
    gs.isPaused = false;
    stopTimer();
    render();
    showGameOver(true);
    return true;
  }

  if (gs.player.health <= 0) {
    gs.player.health = 0;
    gs.isGameOver = true;
    gs.isPaused = false;
    stopTimer();
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
    playSoundById('victory-sound', playVictoryFallbackChime);
  } else {
    title.textContent = t('defeatTitle');
    title.className = 'lose';
    sub.textContent = t('defeatSub');
    playSoundById('defeat-sound');
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
    isPaused: false,
    isGameOver: false,
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

function togglePause() {
  if (gs.isGameOver) return;

  gs.isPaused = !gs.isPaused;
  if (gs.isPaused) {
    stopTimer();
    log(t('gamePaused'));
  } else {
    if (gs.turn === 'player') {
      startTimer();
    } else if (gs.turn === 'ai' && gs.phase === 'aiThinking') {
      setTimeout(() => aiTurnStep(), 150);
    }
  }

  updateStaticTexts();
  render();
}

function startGameFromIntro() {
  const intro = document.getElementById('intro-screen');
  if (intro) intro.classList.remove('active');
  initGame();
}

// Show intro first, only initialize static translated text on load
updateStaticTexts();

window.startGameFromIntro = startGameFromIntro;
window.togglePause = togglePause;
