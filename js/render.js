/* ================================================================
   render.js — All Rendering Functions
   
   Draws the entire game state to the DOM. Called after every
   state change (play card, attack, end turn, etc.).
   
   Functions:
     render()          — top-level, calls all sub-renderers
     renderHand()      — renders a hand (face-up for player, face-down for AI)
     renderBoard()     — renders a board row (selectable/targetable cards)
   ================================================================ */

/* --- Top-Level Render --- */

/** Draw the entire game state to the DOM. */
function render() {
  // Health & mana displays
  document.getElementById('player-health').textContent = gs.player.health + ' HP';
  document.getElementById('player-mana').textContent = gs.player.mana + ' / ' + gs.player.maxMana + ' Mana';
  document.getElementById('ai-health').textContent = gs.ai.health + ' HP';
  document.getElementById('ai-mana').textContent = gs.ai.mana + ' / ' + gs.ai.maxMana + ' Mana';
  document.getElementById('player-deck-count').textContent = gs.player.deck.length;
  document.getElementById('ai-deck-count').textContent = gs.ai.deck.length;

  // Turn indicator
  const ti = document.getElementById('turn-indicator');
  if (gs.turn === 'player') {
    ti.textContent = 'Your Turn — Turn ' + gs.turnNumber;
    ti.className = 'turn-indicator player-turn';
  } else {
    ti.textContent = "AI's Turn — Turn " + gs.turnNumber;
    ti.className = 'turn-indicator ai-turn';
  }

  // End turn button visibility
  document.getElementById('btn-end-turn').style.display =
    (gs.turn === 'player' && gs.phase !== 'aiThinking') ? '' : 'none';

  // Render AI board (targetable when player has attacker selected)
  renderBoard(gs.ai.board, 'ai-board', true);

  // Render player board (selectable as attacker)
  renderBoard(gs.player.board, 'player-board', false);

  // Render player hand (clickable to play)
  renderHand(gs.player.hand, 'player-hand', true);
}

/**
 * Creates an info overlay element for a card
 * @param {Object} card 
 * @returns {string} HTML string
 */
function getCardOverlayHTML(card) {
  return `
    <div class="card-info-overlay">
      <div class="info-title">${card.name}</div>
      <div class="info-rarity ${card.rarity}">${card.rarity}</div>
      <div class="info-type">${card.typeLine || ''}</div>
      <div class="info-abilities">
        ${card.abilities ? card.abilities.map(a => `<div class="ability-item">${a}</div>`).join('') : ''}
      </div>
      <div class="info-stats">
        <span>Attack: ${card.attack}</span>
        <span>Health: ${card.health}</span>
      </div>
    </div>
  `;
}

/* --- Hand Rendering --- */

/** Render a hand of cards.
 *  @param {Array} cards — array of card objects
 *  @param {string} containerId — DOM element ID to render into
 *  @param {boolean} isPlayer — true for player hand (face-up), false for AI (face-down) */
function renderHand(cards, containerId, isPlayer) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';

  for (let i = 0; i < cards.length; i++) {
    const card = cards[i];
    const el = document.createElement('div');

    if (isPlayer) {
      // Player hand card — interactive, can be played
      const canPlay = gs.turn === 'player' && gs.player.mana >= card.manaCost;
      el.className = 'card ' + getThemeClass(card.mythology) + (!canPlay ? ' unplayable' : '');
      el.dataset.idx = i;

      // Highlight selected card for playing
      if (gs.selectedHandIdx === i) {
        el.classList.add('selected');
      }

      el.innerHTML = `
        <div class="card-mana">${card.manaCost}</div>
        ${card.image ? `<img src="${card.image}" alt="${card.name}" class="card-image">` : `<div class="card-art">${card.art || ''}</div>`}
        <div class="card-name">${card.name}</div>
        <div class="card-stats">
          <span class="atk">⚔${card.attack}</span>
          <span class="hp">♥${card.health}</span>
        </div>
        ${getCardOverlayHTML(card)}
      `;

      el.addEventListener('click', () => onHandCardClick(i));
      
      // Delayed zoom logic
      let hoverTimeout;
      el.addEventListener('mouseenter', () => {
        hoverTimeout = setTimeout(() => {
          if (card.image) {
            const popup = document.getElementById('card-image-popup');
            const popupImg = document.getElementById('popup-img');
            popupImg.src = card.image;
            popup.classList.add('active');
          }
        }, 2000);
      });
      el.addEventListener('mouseleave', () => {
        clearTimeout(hoverTimeout);
        document.getElementById('card-image-popup').classList.remove('active');
      });
    } else {
      // AI hand — face down, non-interactive
      el.className = 'card';
      el.style.background = 'linear-gradient(135deg, #2d1b4e 0%, #1a0a2e 100%)';
      el.style.border = '2px solid #5a3d8a';
      el.innerHTML = '<div class="card-art" style="font-size:1.5em;">🂠</div>';
    }

    container.appendChild(el);
  }
}

/* --- Board Rendering --- */

/** Render a board row of cards.
 *  @param {Array} cards — array of card objects on the board
 *  @param {string} containerId — DOM element ID to render into
 *  @param {boolean} isAI — true for AI board, false for player board */
function renderBoard(cards, containerId, isAI) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';

  for (let i = 0; i < cards.length; i++) {
    const card = cards[i];
    const el = document.createElement('div');

    let classes = 'board-card card ' + getThemeClass(card.mythology);
    if (card.frozen) classes += ' frozen';

    // Selected attacker highlight (player's own board card)
    if (!isAI && gs.attackerId === card.id) {
      classes += ' selected';
    }

    // Targetable: enemy board cards when player has attacker selected
    if (isAI && gs.attackerId !== null) {
      classes += ' targetable';
    }

    el.className = classes;
    el.dataset.idx = i;
    el.dataset.id = card.id;

    // Status icons overlay (frozen, taunt)
    const statusIcons = [];
    if (card.frozen) statusIcons.push('❄️');
    if (card.taunt) statusIcons.push('🛡️');

    el.innerHTML = `
      <div class="card-mana">${card.manaCost}</div>
      ${card.image ? `<img src="${card.image}" alt="${card.name}" class="card-image">` : `<div class="card-art">${card.art || ''}${statusIcons.length ? ' ' + statusIcons.join('') : ''}</div>`}
      <div class="card-name">${card.name}</div>
      <div class="card-stats">
        <span class="atk">⚔${card.attack}</span>
        <span class="hp">♥${card.health}</span>
      </div>
      ${getCardOverlayHTML(card)}
    `;

    el.addEventListener('click', () => onBoardCardClick(card, isAI));

    // Delayed zoom logic
    let hoverTimeout;
    el.addEventListener('mouseenter', () => {
      hoverTimeout = setTimeout(() => {
        if (card.image) {
          const popup = document.getElementById('card-image-popup');
          const popupImg = document.getElementById('popup-img');
          popupImg.src = card.image;
          popup.classList.add('active');
        }
      }, 2000);
    });
    el.addEventListener('mouseleave', () => {
      clearTimeout(hoverTimeout);
      document.getElementById('card-image-popup').classList.remove('active');
    });

    container.appendChild(el);
  }

  // Always show heroes as targetable portraits on the board
  if (isAI) {
    const heroEl = document.createElement('div');
    heroEl.className = 'board-card card hero-card';
    if (gs.attackerId !== null) {
      const hasTaunt = gs.ai.board.some(c => c.taunt);
      if (!hasTaunt) heroEl.classList.add('targetable');
    }
    heroEl.style.background = 'linear-gradient(180deg, #4a1a2e 0%, #2d0f15 100%)';
    heroEl.style.border = '3px solid #c0392b';
    heroEl.innerHTML = `
      ${gs.ai.heroImage ? `<img src="hero-cards/${gs.ai.heroImage}" alt="AI Hero" class="card-image">` : `<div class="card-art">👹</div>`}
      <div class="card-name">${gs.ai.heroImage ? gs.ai.heroImage.split('-')[1].replace(/([A-Z])/g, ' $1').trim() : 'AI Hero'}</div>
      <div class="card-stats" style="justify-content:center;"><span class="hp">♥${gs.ai.health}</span></div>
    `;
    heroEl.addEventListener('click', (e) => {
      e.stopPropagation();
      if (gs.attackerId !== null) executePlayerAttack(null);
    });

    // Hero cards zoom on hover
    let heroHoverTimeout;
    heroEl.addEventListener('mouseenter', () => {
      heroEl.classList.add('zoomed');
      heroHoverTimeout = setTimeout(() => {
        const heroImg = gs.ai.heroImage ? `hero-cards/${gs.ai.heroImage}` : null;
        if (heroImg) {
          const popup = document.getElementById('card-image-popup');
          const popupImg = document.getElementById('popup-img');
          popupImg.src = heroImg;
          popup.classList.add('active');
        }
      }, 2000);
    });
    heroEl.addEventListener('mouseleave', () => {
      heroEl.classList.remove('zoomed');
      clearTimeout(heroHoverTimeout);
      document.getElementById('card-image-popup').classList.remove('active');
    });

    container.insertBefore(heroEl, container.firstChild);
  } else {
    const heroEl = document.createElement('div');
    heroEl.className = 'board-card card hero-card';
    if (gs.turn === 'ai' && gs._aiAttackerId !== null) {
      const hasTaunt = gs.player.board.some(c => c.taunt);
      if (!hasTaunt) heroEl.classList.add('targetable');
    }
    heroEl.style.background = 'linear-gradient(180deg, #1a2e4a 0%, #0f152d 100%)';
    heroEl.style.border = '3px solid #35b5ff';
    heroEl.innerHTML = `
      ${gs.player.heroImage ? `<img src="hero-cards/${gs.player.heroImage}" alt="Your Hero" class="card-image">` : `<div class="card-art">🧙</div>`}
      <div class="card-name">${gs.player.heroImage ? gs.player.heroImage.split('-')[1].replace(/([A-Z])/g, ' $1').trim() : 'Your Hero'}</div>
      <div class="card-stats" style="justify-content:center;"><span class="hp">♥${gs.player.health}</span></div>
    `;
    heroEl.addEventListener('click', (e) => {
      e.stopPropagation();
      if (gs.turn === 'ai' && gs._aiAttackerId !== null) executeAiAttack(null);
    });

    // Hero cards zoom on hover
    let heroHoverTimeout;
    heroEl.addEventListener('mouseenter', () => {
      heroEl.classList.add('zoomed');
      heroHoverTimeout = setTimeout(() => {
        const heroImg = gs.player.heroImage ? `hero-cards/${gs.player.heroImage}` : null;
        if (heroImg) {
          const popup = document.getElementById('card-image-popup');
          const popupImg = document.getElementById('popup-img');
          popupImg.src = heroImg;
          popup.classList.add('active');
        }
      }, 2000);
    });
    heroEl.addEventListener('mouseleave', () => {
      heroEl.classList.remove('zoomed');
      clearTimeout(heroHoverTimeout);
      document.getElementById('card-image-popup').classList.remove('active');
    });

    container.insertBefore(heroEl, container.firstChild);
  }
}
