/* ================================================================
   i18n.js — English/Greek translations and language switching
   ================================================================ */

const I18N = {
  en: {
    aiOpponent: '👾 AI Opponent',
    you: '👨‍🎯 You',
    hp: 'HP',
    mana: 'Mana',
    deck: 'Deck',
    endTurn: 'End Turn',
    playAgain: 'Play Again',
    yourTurn: 'Your Turn',
    aiTurn: "AI's Turn",
    turnLabel: 'Turn',
    victoryTitle: '🏆 VICTORY!',
    victorySub: 'You defeated the AI opponent!',
    defeatTitle: '💀 DEFEAT',
    defeatSub: 'The AI has bested you. Try again!',
    loadingCards: 'Loading mythical cards...',
    gameStarted: 'Game started! You draw 3 cards. Click a card to play it.',
    aiThinking: 'AI is thinking...',
    timesUp: "Time's up!",
    notYourTurn: 'Not your turn!',
    notEnoughManaFor: 'Not enough mana for',
    needMana: 'need',
    boardFull: 'Your board is full!',
    selected: 'Selected',
    clickEnemyToAttack: 'Click an enemy minion or hero to attack.',
    isFrozen: 'is frozen and can\'t attack!',
    alreadyAttacked: 'has already attacked this turn.',
    mustAttackTaunt: 'Must attack a taunting minion first!',
    attacksAIFor: 'attacks AI for',
    attacksYouFor: 'attacks you for',
    entersBattlefield: 'enters the battlefield.',
    youPlay: 'You play',
    aiPlays: 'AI plays'
    ,aiAttacks: 'AI'
    ,attacks: 'attacks'
    ,burnsEnemies: 'burns! 2 damage to all enemies.'
    ,rebornWithOne: 'is reborn with 1 HP!'
    ,returnsToHand: 'returns to hand!'
    ,skeletonsRise: 'Skeletons rise from the dead!'
    ,introTitle: 'Mythos Convergence'
    ,introSubtitle: 'A strategic mythology card battle.'
    ,rulesTitle: 'How to Play'
    ,rule1: 'Each player starts with 20 health and 3 cards.'
    ,rule2: 'Play cards using mana and build your board (max 7 minions).'
    ,rule3: 'Attack enemy minions or the enemy hero during your turn.'
    ,rule4: 'Reduce the enemy hero to 0 health to win.'
    ,startGame: 'Start Game'
    ,pause: 'Pause'
    ,resume: 'Resume'
    ,gamePaused: 'Game paused.'
  },
  el: {
    aiOpponent: '👾 Αντίπαλος AI',
    you: '👨‍🎯 Εσύ',
    hp: 'Ζωή',
    mana: 'Μάνα',
    deck: 'Τράπουλα',
    endTurn: 'Τέλος Γύρου',
    playAgain: 'Παίξε Ξανά',
    yourTurn: 'Η Σειρά Σου',
    aiTurn: 'Σειρά AI',
    turnLabel: 'Γύρος',
    victoryTitle: '🏆 ΝΙΚΗ!',
    victorySub: 'Νίκησες τον αντίπαλο AI!',
    defeatTitle: '💀 ΗΤΤΑ',
    defeatSub: 'Ο AI σε νίκησε. Προσπάθησε ξανά!',
    loadingCards: 'Φόρτωση μυθικών καρτών...',
    gameStarted: 'Το παιχνίδι ξεκίνησε! Τράβηξες 3 κάρτες. Πάτησε μια κάρτα για να την παίξεις.',
    aiThinking: 'Ο AI σκέφτεται...',
    timesUp: 'Ο χρόνος τελείωσε!',
    notYourTurn: 'Δεν είναι η σειρά σου!',
    notEnoughManaFor: 'Δεν έχεις αρκετό μάνα για',
    needMana: 'χρειάζεται',
    boardFull: 'Το πεδίο σου είναι γεμάτο!',
    selected: 'Επιλέχθηκε',
    clickEnemyToAttack: 'Πάτα έναν εχθρικό υπηρέτη ή ήρωα για επίθεση.',
    isFrozen: 'είναι παγωμένος και δεν μπορεί να επιτεθεί!',
    alreadyAttacked: 'έχει ήδη επιτεθεί σε αυτόν τον γύρο.',
    mustAttackTaunt: 'Πρέπει πρώτα να επιτεθείς σε υπηρέτη με Πρόκληση!',
    attacksAIFor: 'επιτίθεται στον AI για',
    attacksYouFor: 'σου επιτίθεται για',
    entersBattlefield: 'μπαίνει στο πεδίο μάχης.',
    youPlay: 'Παίζεις',
    aiPlays: 'Ο AI παίζει'
    ,aiAttacks: 'AI'
    ,attacks: 'επιτίθεται σε'
    ,burnsEnemies: 'καίει! 2 ζημιά σε όλους τους εχθρούς.'
    ,rebornWithOne: 'αναγεννιέται με 1 Ζωή!'
    ,returnsToHand: 'επιστρέφει στο χέρι!'
    ,skeletonsRise: 'Σκελετοί σηκώνονται από τους νεκρούς!'
    ,introTitle: 'Mythos Convergence'
    ,introSubtitle: 'Μια στρατηγική μάχη καρτών μυθολογίας.'
    ,rulesTitle: 'Πώς Παίζεται'
    ,rule1: 'Κάθε παίκτης ξεκινά με 20 ζωή και 3 κάρτες.'
    ,rule2: 'Παίξε κάρτες με μάνα και χτίσε το πεδίο σου (μέχρι 7 υπηρέτες).'
    ,rule3: 'Επιτέσου σε εχθρικούς υπηρέτες ή στον εχθρικό ήρωα στον γύρο σου.'
    ,rule4: 'Μείωσε τον εχθρικό ήρωα σε 0 ζωή για να κερδίσεις.'
    ,startGame: 'Έναρξη Παιχνιδιού'
    ,pause: 'Παύση'
    ,resume: 'Συνέχεια'
    ,gamePaused: 'Το παιχνίδι είναι σε παύση.'
  }
};

let currentLanguage = localStorage.getItem('lang') || 'en';

function t(key) {
  return (I18N[currentLanguage] && I18N[currentLanguage][key]) || I18N.en[key] || key;
}

function setLanguage(lang) {
  currentLanguage = lang === 'el' ? 'el' : 'en';
  localStorage.setItem('lang', currentLanguage);
  updateStaticTexts();
  if (typeof render === 'function') render();
}

function updateStaticTexts() {
  const aiName = document.getElementById('ai-name');
  const playerName = document.getElementById('player-name');
  const aiDeckLabel = document.getElementById('ai-deck-label');
  const playerDeckLabel = document.getElementById('player-deck-label');
  const endTurnBtn = document.getElementById('btn-end-turn');
  const playAgainBtn = document.getElementById('btn-play-again');
  const introTitle = document.getElementById('intro-title');
  const introSubtitle = document.getElementById('intro-subtitle');
  const rulesTitle = document.getElementById('rules-title');
  const rulesList = document.getElementById('rules-list');
  const startGameBtn = document.getElementById('btn-start-game');
  const pauseBtn = document.getElementById('btn-pause');

  if (aiName) aiName.textContent = t('aiOpponent');
  if (playerName) playerName.textContent = t('you');
  if (aiDeckLabel) aiDeckLabel.textContent = t('deck') + ':';
  if (playerDeckLabel) playerDeckLabel.textContent = t('deck') + ':';
  if (endTurnBtn) endTurnBtn.textContent = t('endTurn');
  if (playAgainBtn) playAgainBtn.textContent = t('playAgain');
  if (introTitle) introTitle.textContent = t('introTitle');
  if (introSubtitle) introSubtitle.textContent = t('introSubtitle');
  if (rulesTitle) rulesTitle.textContent = t('rulesTitle');
  if (startGameBtn) startGameBtn.textContent = t('startGame');
  if (pauseBtn) pauseBtn.textContent = (typeof gs !== 'undefined' && gs.isPaused) ? t('resume') : t('pause');

  if (rulesList) {
    rulesList.innerHTML = `
      <li>${t('rule1')}</li>
      <li>${t('rule2')}</li>
      <li>${t('rule3')}</li>
      <li>${t('rule4')}</li>
    `;
  }

  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === currentLanguage);
  });
}

window.t = t;
window.setLanguage = setLanguage;
window.updateStaticTexts = updateStaticTexts;