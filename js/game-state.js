/* ================================================================
   game-state.js — Game State, Utilities & Deck Building
   
   Holds the global game state object and provides utility functions
   for shuffling, creating card instances, theme lookups, and deck generation.
   ================================================================ */

// Global game state — all mutable game data lives here
let gs = {
  player: { health:20, mana:0, maxMana:1, deck:[], hand:[], board:[], heroImage: '' },
  ai:     { health:20, mana:0, maxMana:1, deck:[], hand:[], board:[], heroImage: '' },
  turn: 'player',           // whose turn it is
  phase: 'main',            // main | aiThinking
  attackerId: null,         // id of player's board card selected to attack with
  turnNumber: 1,
};

let nextCardId = 1; // unique ID counter for board cards

/* --- Utility Functions --- */

/** Write a message to the game log area */
function log(msg) {
  document.getElementById('message-log').textContent = msg;
}

/** Fisher-Yates shuffle — mutates array in place */
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/** Create a card instance from a template with unique ID */
function createCardInstance(template) {
  return {
    id: nextCardId++,
    name: template.name,
    manaCost: template.manaCost,
    attack: template.attack,
    health: template.health,
    maxHealth: template.health,
    typeLine: template.typeLine,
    mythology: template.mythology,
    rarity: template.rarity,
    abilities: template.abilities || [],
    image: template.image,
    canAttack: false,   // summoning sickness (unless Rush/Charge)
    frozen: false,      // can't attack while frozen
    stealthed: false,   // immune to abilities (not used in combat)
    taunt: false,       // enemies must attack this first
    hasAttacked: false, // already used attack this turn
  };
}

/** List of available hero images */
const HERO_IMAGES = [
  'Hero-Odin-NorseMythology.png',
  'Hero-Ra-EgyptianMythology.png',
  'Hero-TheJadeEmperor-ChineseMythology.png',
  'Hero-Zeus-GreekMythology.png',
  'Hero-Amaterasu-JapaneseMythology.png',
  'Hero-TheDagda-CelticMythology.png',
  'Hero-Ishtar-MesopotamianMythology.png',
  'Hero-Shiva-HinduMythology.png'
];

/** Map mythology string to CSS theme class */
function getThemeClass(mythology) {
  const map = {
    'Greek': 'theme-greek',
    'Egyptian': 'theme-egyptian',
    'Chinese': 'theme-chinese',
    'Norse': 'theme-norse',
    'Celtic': 'theme-celtic',
    'Japanese': 'theme-japanese',
    'Mesopotamian': 'theme-mesopotamian',
    'Hindu': 'theme-hindu',
    'Aztec': 'theme-aztec',
    'African': 'theme-african',
    'NativeAmerican': 'theme-native',
    'Inuit': 'theme-inuit'
  };
  return map[mythology] || 'theme-default';
}

/** Find a card by ID across all zones (board, hand, deck) */
function findCardById(id) {
  const all = [...gs.player.board, ...gs.ai.board, ...gs.player.hand, ...gs.ai.hand];
  return all.find(c => c.id === id) || null;
}

/** Find the original template matching a card by name+stats */
function findTemplateFor(card) {
  for (const tmpl of CARD_TEMPLATES) {
    if (tmpl.name === card.name && tmpl.manaCost === card.manaCost) return tmpl;
  }
  // Fallback
  return { name:'Skeleton', manaCost:0, attack:1, health:1, mythology:'Unknown', ability:'', abilityDesc:'', art:'💀' };
}

/* --- Deck Building --- */

/** Build a random 20-card deck from the card templates.
 *  Picks ~12 unique templates, adds 1-2 copies each, fills remaining with randoms. */
function buildDeck() {
  const shuffled = shuffle([...CARD_TEMPLATES]);
  let deck = [];

  // Pick ~12 unique templates, add 1-2 copies each
  for (const tmpl of shuffled.slice(0, 12)) {
    const count = Math.random() < 0.4 ? 2 : 1;
    for (let i = 0; i < count && deck.length < 20; i++) {
      deck.push(createCardInstance(tmpl));
    }
  }

  // Fill remaining with random cards
  while (deck.length < 20) {
    const tmpl = CARD_TEMPLATES[Math.floor(Math.random() * CARD_TEMPLATES.length)];
    deck.push(createCardInstance(tmpl));
  }

  return shuffle(deck);
}
