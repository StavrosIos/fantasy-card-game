/* ================================================================
   cards.js — Card Database (Templates)
   
   Cards inspired by the generated card images in /workspace/../cards/
   and /workspace/card-grid/. Clean abilities replace AI gibberish.
   
   6 archetypes, each with a color theme:
     Fire Mage    — red/orange border
     Ice Sorcerer  — blue/cyan border
     Undead        — purple border
     Forest Beast  — green border
     Knight        — gold border
     Vampire       — dark red border
   ================================================================ */

const CARD_TEMPLATES = [
   // --- FIRE MAGE cards (theme: red/orange) ---
   { name:"Ignis, the Arsonist", manaCost:3, attack:2, health:3, archetype:"Fire Mage", ability:"Burn", abilityDesc:"On death: Deal 2 damage to all enemy minions.", art:"🔥", image:"cards/Ignis_the_Arsonist.png" },
   { name:"Pyre, the Young", manaCost:2, attack:2, health:2, archetype:"Fire Mage", ability:"Fireball", abilityDesc:"Battlecry: Deal 1 damage to a random enemy.", art:"🔥", image:"cards/Pyre_the_Young.png" },
   { name:"Emberclaw Dragon", manaCost:5, attack:2, health:3, archetype:"Fire Mage", ability:"Inferno", abilityDesc:"Battlecry: Deal 2 damage to all enemy minions.", art:"🐉", image:"cards/Emberclaw_Dragon.png" },
   { name:"Fleshforged Garmat", manaCost:4, attack:3, health:1, archetype:"Fire Mage", ability:"Flame Rush", abilityDesc:"Charge. Battlecry: Deal 1 damage to your hero.", art:"🔥", image:"cards/Fleshforged_Garmat.png" },
   { name:"Stormvoyager Mage", manaCost:3, attack:1, health:2, archetype:"Fire Mage", ability:"Gust", abilityDesc:"Battlecry: Deal 1 damage to all enemy minions.", art:"🌪️", image:"cards/Stormvoyager_Mage.png" },

   // --- ICE SORCERER cards (theme: blue/cyan) ---
   { name:"Anya, Frostbinder", manaCost:4, attack:4, health:5, archetype:"Ice Sorcerer", ability:"Freeze", abilityDesc:"Battlecry: Freeze a random enemy minion.", art:"❄️", image:"cards/Anya_Frostbinder.png" },
   { name:"Rimeheart", manaCost:3, attack:2, health:4, archetype:"Ice Sorcerer", ability:"Chill", abilityDesc:"Battlecry: Reduce an enemy minion's attack by 1.", art:"🧊", image:"cards/Rimeheart.png" },
   { name:"Arctic Chronosnaker", manaCost:5, attack:3, health:1, archetype:"Ice Sorcerer", ability:"Return", abilityDesc:"Deathrattle: Return this card to your hand.", art:"🐍", image:"cards/Arctic_Chronosnaker.png" },
   { name:"Glacill", manaCost:4, attack:2, health:3, archetype:"Ice Sorcerer", ability:"Cleave", abilityDesc:"Battlecry: Deal 1 damage to all other minions.", art:"🧊", image:"cards/Glacill.png" },
   { name:"Silomto", manaCost:3, attack:2, health:4, archetype:"Ice Sorcerer", ability:"Summon Ice", abilityDesc:"Battlecry: Summon a 1/2 Frost Elemental.", art:"🧊", image:"cards/Silomto.png" },

   // --- UNDEAD / SKELETON cards (theme: purple) ---
   { name:"Skullspitter", manaCost:2, attack:2, health:1, archetype:"Undead", ability:"Cleave", abilityDesc:"Battlecry: Deal 1 damage to all other minions.", art:"💀", image:"cards/Skullspitter.png" },
   { name:"Legion of Bones", manaCost:4, attack:0, health:3, archetype:"Undead", ability:"Swarm", abilityDesc:"Battlecry: Summon two 1/1 Skeletons.", art:"💀", image:"cards/Legion_of_Bones.png" },
   { name:"Crypt Lich", manaCost:5, attack:2, health:3, archetype:"Undead", ability:"Drain", abilityDesc:"Battlecry: Deal 2 damage to enemy hero, heal 2.", art:"🦇", image:"cards/Crypt_Lich.png" },
   { name:"Skalpitter", manaCost:3, attack:4, health:1, archetype:"Undead", ability:"Pierce", abilityDesc:"Charge. Battlecry: Deal 1 damage to your hero.", art:"💀", image:"cards/Skalpitter.png" },
   { name:"Undying Guardian", manaCost:4, attack:3, health:5, archetype:"Undead", ability:"Reborn", abilityDesc:"Deathrattle: Return to hand with 1 HP.", art:"🛡️", image:"cards/Undying_Guardian.png" },

   // --- FOREST BEAST cards (theme: green) ---
   { name:"Graveword Behemoth", manaCost:5, attack:4, health:2, archetype:"Forest Beast", ability:"Regen", abilityDesc:"At end of turn: Heal this minion 1 HP.", art:"🐻", image:"cards/Graveword_Behemoth.png" },
   { name:"Venomfang Broodling", manaCost:1, attack:1, health:1, archetype:"Forest Beast", ability:"Poison", abilityDesc:"Deals 1 extra damage when attacking.", art:"🕷️", image:"cards/Venomfang_Broodling.png" },
   { name:"Contime", manaCost:3, attack:2, health:2, archetype:"Forest Beast", ability:"Poison", abilityDesc:"Deals 1 extra damage when attacking.", art:"🐸", image:"cards/Contime.png" },
   { name:"Gritemur", manaCost:2, attack:3, health:3, archetype:"Forest Beast", ability:"Taunt", abilityDesc:"Enemies must attack this minion first.", art:"🦎", image:"cards/Gritemur.png" },
   { name:"Forest Hunter", manaCost:1, attack:2, health:2, archetype:"Forest Beast", ability:"Rush", abilityDesc:"Can attack immediately upon playing.", art:"🏹", image:"cards/Forest_Hunter.png" },

   // --- KNIGHT cards (theme: gold) ---
   { name:"Ironfang", manaCost:4, attack:3, health:2, archetype:"Knight", ability:"Taunt", abilityDesc:"Enemies must attack this minion first.", art:"⚔️", image:"cards/Ironfang.png" },
   { name:"Melact Gondlan", manaCost:3, attack:2, health:4, archetype:"Knight", ability:"Shield", abilityDesc:"Battlecry: Gain +1 Health.", art:"🛡️", image:"cards/Melact_Gondlan.png" },
   { name:"Shadowsticher", manaCost:2, attack:3, health:3, archetype:"Knight", ability:"Heal", abilityDesc:"Battlecry: Restore 2 HP to your hero.", art:"🗡️", image:"cards/Shadowsticher.png" },
   { name:"Voidcaller Acolyte", manaCost:3, attack:1, health:3, archetype:"Knight", ability:"Drain", abilityDesc:"Battlecry: Restore 2 HP to your hero.", art:"🔮", image:"cards/Voidcaller_Acolyte.png" },
   { name:"Silvayus, Healer", manaCost:3, attack:0, health:4, archetype:"Knight", ability:"Heal", abilityDesc:"At end of turn: Restore 1 HP to your hero.", art:"✨", image:"cards/Silvayus_Healer.png" },

   // --- VAMPIRE cards (theme: dark red) ---
   { name:"Bloodreaver", manaCost:3, attack:2, health:2, archetype:"Vampire", ability:"Drain", abilityDesc:"Battlecry: Deal 1 dmg to enemy hero, heal 2.", art:"🧛", image:"cards/Bloodreaver.png" },
   { name:"Nightstalker", manaCost:2, attack:3, health:1, archetype:"Vampire", ability:"Stealth", abilityDesc:"Cannot be targeted by abilities.", art:"🦇", image:"cards/Nightstalker.png" },
   { name:"Vespera, Blood Queen", manaCost:6, attack:4, health:5, archetype:"Vampire", ability:"Drain", abilityDesc:"Battlecry: Deal 2 dmg to enemy hero, heal 2.", art:"🧛", image:"cards/Vespera_Blood_Queen.png" },
];
