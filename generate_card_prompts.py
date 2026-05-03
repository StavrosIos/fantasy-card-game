#!/usr/bin/env python3
"""Generate 100 fantasy card prompt .txt files for a mythology-based card game."""

import os

OUTPUT_DIR = "card_prompts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Base template function
def make_card(name, mana_cost, type_line, artwork_desc, abilities, attack, health):
    return f"""A single, professionally designed fantasy trading card displayed in a straight-on, flat view, perfectly centered and fully visible with no perspective distortion. The card features an ornate, high-quality fantasy frame with sharp rectangular borders, polished metallic accents, and symmetrical layout, set against a clean neutral background for easy cropping.

At the top of the card, a clearly defined title bar displays the name: "{name}", with a mana cost of {mana_cost} shown in a distinct icon at the top-right corner.

The central artwork shows {artwork_desc} Style is highly detailed digital painting, vibrant color palette with professional trading card game quality.

Below the artwork is a clean type line reading:
"{type_line}"

Beneath that is a clearly separated text box with sharp, readable typography containing two abilities:

{abilities[0]}
{abilities[1]}

At the bottom of the card is a polished stats bar displaying:
Attack {attack} (left) and Health {health} (right)

The entire layout is clean, balanced, and symmetrical with consistent spacing. All text is crisp, correctly spelled, and fully legible. No blur, no distortion, no warped text.

Style tags: high fantasy, trading card game, ultra-detailed, sharp focus, professional UI design, digital painting, vibrant lighting, clean layout, print-ready"""

# Card data: (name, mana_cost, type_line, artwork_desc, [ability1, ability2], attack, health)
cards = [
    # === GREEK MYTHOLOGY (15 cards) ===
    ("Athena, Goddess of Wisdom", 7, "God — Greek",
     "the Greek goddess Athena standing tall in gleaming golden armor with a helmet adorned with white feather crests. She holds a glowing spear and a shield bearing Medusa's head. Her piercing grey eyes radiate wisdom. Behind her, a grand Greek temple with marble columns rises into golden light. Olive branches and glowing symbols of wisdom float around her.",
     ["Divine Strategy: Draw 2 cards", "Shield of Aegis: Prevent 5 damage to your hero"],
     6, 6),

    ("Zeus, King of the Gods", 10, "God — Greek",
     "the supreme Greek god Zeus towering above Mount Olympus in a flowing white and gold robe. Lightning bolts crackle around his clenched fists, illuminating a stormy sky. His thick white beard and blazing electric blue eyes command power. Thunderclouds swirl above as multiple lightning bolts descend from the heavens.",
     ["Thunderbolt: Deal 5 damage to all enemy minions", "Divine Rule: Gain 3 Armor at the start of your turn"],
     8, 8),

    ("Hades, Lord of the Underworld", 9, "God — Greek",
     "the dark god Hades seated upon a black obsidian throne in the Underworld. He wears a dark hooded cloak with glowing purple energy emanating from within. The Helm of Darkness rests upon his brow. Spectral chains and shadowy souls swirl around him. His two-headed hound Cerberus looms behind the throne with burning red eyes.",
     ["Soul Drain: Steal 3 health from an enemy minion", "Dark Dominion: All Deathrattle cards cost 1 less"],
     7, 9),

    ("Poseidon, God of the Seas", 8, "God — Greek",
     "the mighty sea god Poseidon rising from massive ocean waves, his muscular form draped in seaweed and golden armor. He wields a trident that crackles with blue energy. Massive waves crash around him, and sea creatures leap from the water. Dolphins swim through the spray as storm clouds gather overhead.",
     ["Tidal Wave: Deal 3 damage to all enemy minions", "Ocean's Blessing: Restore 5 health to your hero"],
     7, 7),

    ("Ares, God of War", 6, "God — Greek",
     "the fierce god Ares charging into battle in crimson-red armor covered in battle scars. He wields a massive blood-stained sword overhead, roaring with fury. Flames of war burn around him as fallen warriors and broken shields litter the battlefield behind him. His red cape billows dramatically in the wind.",
     ["War Cry: Give all friendly minions +2 Attack", "Bloodlust: Deal 3 damage to your hero for +4 Attack"],
     8, 5),

    ("Hermes, Messenger of the Gods", 3, "God — Greek",
     "the swift messenger god Hermes flying through the air with golden winged sandals and a winged petasos hat. He carries the caduceus staff that glows with magical energy. His agile athletic form wears a flowing green tunic. Swirling winds and golden sparkles trail behind him as he moves at impossible speed.",
     ["Swift Strike: Attack an enemy minion immediately", "Divine Speed: Draw a card each turn"],
     4, 3),

    ("Apollo, God of Light", 7, "God — Greek",
     "the golden god Apollo standing radiant in flowing white and gold robes, his long blond hair shimmering like sunlight. He draws back a golden bow that emits brilliant beams of light. The sun disk glows behind him as his chariot of fire waits in the sky. Golden rays illuminate the entire scene.",
     ["Solar Beam: Deal 4 damage to a minion", "Healing Light: Restore 4 health to your hero"],
     5, 6),

    ("Artemis, Goddess of the Hunt", 5, "God — Greek",
     "the fierce huntress goddess Artemis in a short brown leather hunting outfit, drawing her silver bow with perfect aim. A glowing crescent moon hovers behind her. Her loyal hunting deer stands beside her with antlers that glow softly. Forest shadows and moonlight create a mystical atmosphere around her.",
     ["Hunter's Mark: Deal 3 damage to a random enemy", "Pack Tactics: Your other minions get +1 Attack"],
     5, 4),

    ("Hephaestus, God of the Forge", 6, "God — Greek",
     "the mighty god Hephaestus in his great volcanic forge, his muscular form covered in soot and scars. He wields a massive hammer that glows red-hot from striking molten metal. Sparks and flames erupt everywhere as he crafts a divine weapon. Molten lava flows around his feet.",
     ["Forge Strike: Give a minion +3 Attack and Battlecry", "Infernal Anvil: Summon a 2/1 Construct"],
     4, 7),

    ("Aphrodite, Goddess of Love", 4, "God — Greek",
     "the beautiful goddess Aphrodite rising from the sea on a giant seashell, her body glowing with ethereal light. She wears a flowing translucent white gown that shimmers with pearl and gold. Pink rose petals swirl around her as Cupid flies nearby with his golden bow. Hearts of light float in the air.",
     ["Charm: Convert an enemy minion to your side", "Beauty of the Gods: Restore 3 health each turn"],
     3, 5),

    ("Medusa, the Gorgon", 4, "Creature — Monster",
     "the terrifying gorgon Medusa with her serpentine hair of writhing green and black snakes, each snake hissing with fangs bared. Her pale green skin glows in the moonlight, and her eyes emit a powerful petrifying glow. Stone fragments float around her as victims of her gaze turn to stone. She wears tattered ancient Greek armor.",
     ["Petrifying Gaze: Turn a minion to stone", "Snake Bite: Deal 2 damage to all enemies"],
     3, 5),

    ("Minotaur, Labyrinth Beast", 5, "Creature — Monster",
     "the massive Minotaur standing in the dark stone corridors of the Labyrinth, its bull-headed form towering over everything. It wields a double-bladed bronze axe dripping with blood. Its muscular body is covered in dark brown fur, and its glowing red eyes burn with rage. Stone walls of the labyrinth surround it.",
     ["Charge: Attack immediately when played", "Labyrinth Trap: Deal 2 damage to attackers"],
     6, 5),

    ("Hydra, Many-Headed Terror", 7, "Creature — Beast",
     "the terrifying multi-headed Hydra rising from a dark swamp, its five massive serpent heads hissing and snapping. Each head breathes a different colored poison — green, purple, blue, red, and black. Its scaly emerald body coils through the murky water as frogs and fish flee in terror. Swamp gas bubbles rise around it.",
     ["Regeneration: Restore 3 health at start of turn", "Venomous Bite: Deal 2 damage to a random enemy"],
     5, 7),

    ("Pegasus, Winged Stallion", 3, "Creature — Beast",
     "the magnificent white Pegasus soaring through a brilliant blue sky with its powerful silver-winged form catching the sunlight. Its flowing mane and tail shimmer like pearl, and its hooves leave trails of golden sparkles. Below, a vast Greek landscape of mountains and valleys stretches out.",
     ["Fly: Can only be blocked by flying minions", "Aerial Assault: Deal 2 damage on attack"],
     4, 3),

    ("Titan Prometheus", 9, "Creature — Titan",
     "the mighty Titan Prometheus chained to a rocky mountain peak, his giant muscular form glowing with stolen divine fire. Flames erupt from his chest as he holds a torch of eternal flame aloft. Eagles circle above in the stormy sky. The fire he stole from the gods illuminates the dark landscape below.",
     ["Fire Gift: Deal 3 damage to all enemies", "Immolation: Takes 2 damage each turn but deals 2 back"],
     7, 8),

    # === EGYPTIAN MYTHOLOGY (15 cards) ===
    ("Ra, God of the Sun", 10, "God — Egyptian",
     "the great sun god Ra floating above the desert in his golden falcon-headed form, wearing the solar disk crown with a sacred cobra. His massive wings of gold and crimson spread across the sky. The sun disk behind him radiates blinding golden light that illuminates the entire desert landscape below.",
     ["Solar Flare: Deal 6 damage to all enemy minions", "Daywalker: Gains +2 Attack during your turn"],
     8, 8),

    ("Anubis, God of the Dead", 7, "God — Egyptian",
     "the jackal-headed god Anubis standing in his black obsidian temple of mummification. His sleek black jackal head gleams with golden eyes, and his body is draped in linen wrappings adorned with hieroglyphs. He holds the golden scales of judgment as souls of the dead float around him in spectral form.",
     ["Weigh Heart: Destroy a minion if its attack is higher than 5", "Undead Army: Summon a 1/3 Skeleton"],
     6, 7),

    ("Osiris, God of the Afterlife", 8, "God — Egyptian",
     "the mummified god Osiris seated upon a golden throne in the Hall of Judgment. His green skin symbolizes rebirth, and he wears the tall white crown of Upper Egypt. He holds a crook and flail crossed over his chest. Golden light emanates from the afterlife realm behind him as spectral wings spread above.",
     ["Resurrection: Bring back a destroyed minion", "Divine Judgment: Deal 3 damage to all non-Egyptian gods"],
     5, 9),

    ("Isis, Goddess of Magic", 6, "God — Egyptian",
     "the powerful goddess Isis floating in a starlit sky, her golden headdress with the hieroglyph of the throne glowing brightly. She wears a sleek form-fitting gown of lapis lazuli blue and gold, her arms raised as magical energy swirls around her in glowing golden spirals. The phoenix of rebirth rises behind her.",
     ["Magic Mastery: Copy an enemy minion's ability", "Healing Touch: Restore 5 health to a friendly minion"],
     4, 6),

    ("Horus, God of the Sky", 8, "God — Egyptian",
     "the falcon-headed god Horus soaring through the bright blue sky with his massive golden wings spread wide. His sleek falcon head gleams with fierce determination, and he wears the double crown of Egypt. Solar energy crackles around his talons as he dives through clouds of gold and blue.",
     ["Sky Strike: Deal 4 damage to a minion", "All Seeing Eye: Reveal enemy's hand"],
     7, 6),

    ("Set, God of Chaos", 7, "God — Egyptian",
     "the fierce and menacing chaos god Set in his mysterious Seth animal form with a long snout and square ears, standing amid a raging sandstorm. His red cloak billows as lightning cracks around him in the desert sky. The serpent Apophis coils beneath his feet, and broken pillars of ancient Egypt rise from the sand.",
     ["Chaos Wave: Deal 2 damage to everything", "Sandstorm: Destroy all 1-cost minions"],
     7, 6),

    ("Bastet, Goddess of Cats", 4, "God — Egyptian",
     "the graceful cat goddess Bastet in her feline form with the head of a sleek golden cat and a woman's athletic body. She wears an elaborate golden collar and headdress, holding a sharp silver dagger. Her glowing green eyes gleam in the moonlight as shadowy cats gather around her feet.",
     ["Cat's Grace: Dodge the next attack", "Nine Lives: Survives death once per game"],
     3, 4),

    ("Sobek, God of the Nile", 6, "God — Egyptian",
     "the massive crocodile-headed god Sobek rising from the murky waters of the Nile, his scaly green body covered in golden Egyptian armor. His jaws are wide open showing rows of razor-sharp teeth, and he wields a sharp bronze blade. Reeds and papyrus plants line the riverbank behind him.",
     ["River Terror: Deal 3 damage to a random enemy", "Ambush: +2 Attack when attacking from behind"],
     6, 5),

    ("Thoth, God of Knowledge", 5, "God — Egyptian",
     "the wise ibis-headed god Thoth standing in the great library of Alexandria, his long curved beak pointed at ancient papyrus scrolls. He holds a writing palette and reed brush that glow with magical energy. Golden hieroglyphs float in the air around him as books and scrolls fill the shelves behind him.",
     ["Ancient Knowledge: Draw 3 cards", "Wisdom: Reduce all your card costs by 1"],
     3, 5),

    ("Sekhmet, Goddess of War", 6, "God — Egyptian",
     "the fierce lioness-headed goddess Sekhmet in her battle form, wearing golden armor and a sun disk crown. Her lion head snarls with fury as she wields a staff topped with the ankh. Flames of destruction erupt around her as the desert sand burns red in the sunlight of Ra's disk.",
     ["Rage of Sekhmet: Deal 4 damage to a minion", "Plague: Enemies take 1 damage each turn"],
     7, 4),

    ("Scarab, Sacred Beetle", 1, "Creature — Beast",
     "the mystical golden scarab beetle glowing with ancient Egyptian magic, its polished green shell reflecting hieroglyphic symbols. It pushes a tiny glowing orb of solar energy across dark stone. Small Egyptian temple bricks surround it, and golden dust sparkles in the air.",
     ["Rebirth: Return to hand when destroyed", "Solar Power: +1 Attack for each card played"],
     1, 2),

    ("Sphinx, Riddle Guardian", 5, "Creature — Beast",
     "the majestic great Sphinx with the body of a lion and the head of a human wearing a nemes headdress, standing guard before an ancient pyramid at sunset. Its golden fur gleams in the orange light, and its wise eyes glow with ancient knowledge. Sand dunes stretch endlessly behind it.",
     ["Riddle: Guess the card or take 3 damage", "Guardian: +2 Attack when defending"],
     4, 6),

    ("Mummy, Cursed Warrior", 3, "Creature — Undead",
     "the terrifying ancient mummy warrior rising from a dark tomb, its golden burial wrappings unraveling to reveal decayed green skin beneath. Hieroglyphic curses glow in purple on its linen bandages. It wields a curved khopesh sword, and golden tomb dust swirls around it in the dim torchlight.",
     ["Curse: Enemy minions lose 1 Attack", "Decay: Deals 1 damage when it dies"],
     2, 4),

    ("Pharaoh, Ruler of Egypt", 8, "Creature — Human",
     "the mighty Pharaoh standing on the balcony of a grand Egyptian palace, wearing the full royal regalia — the nemes headdress, false beard, and multiple gold necklaces. He holds a scepter and flag of power. Golden pyramids and massive temple columns rise behind him under a starlit desert sky.",
     ["Royal Decree: Choose one — Draw 2, Gain 3 Armor, or Deal 4", "Crown of Egypt: All Egyptian cards cost 1 less"],
     6, 7),

    ("Ankhu, Key of Life", 2, "Artifact — Relic",
     "the golden ankhu cross (key of life) floating in mid-air, glowing with warm amber and emerald magical energy. Ancient Egyptian hieroglyphs pulse along its surface as golden light radiates outward. Dark stone temple walls with carved gods surround it in the mystical background.",
     ["Life Force: Restore 4 health to your hero", "Blessing: Minions you summon cost 1 less"],
     0, 0),

    # === CHINESE MYTHOLOGY (15 cards) ===
    ("Jade Emperor, Ruler of Heaven", 10, "God — Chinese",
     "the majestic Jade Emperor seated upon a throne of emerald and gold in the heavenly palace above the clouds. He wears elaborate imperial robes embroidered with dragons and phoenixes, his long black beard flowing gracefully. Golden halos of divine light surround him as celestial attendants bow before him.",
     ["Heaven's Decree: Control all minion attacks", "Immortality: Cannot be destroyed by damage"],
     8, 10),

    ("Dragon, Symbol of Power", 9, "Creature — Dragon",
     "the magnificent Chinese dragon coiling through golden clouds in the sky, its long serpentine body covered in emerald green scales with flowing golden whiskers and razor-sharp claws. Its three beard streams behind it as it breathes a stream of golden fire. Mountains and pagodas are visible far below through the clouds.",
     ["Fire Breath: Deal 4 damage to a lane", "Flight: Can attack immediately"],
     8, 7),

    ("Fenghuang, Phoenix of China", 7, "Creature — Beast",
     "the magnificent Chinese phoenix Fenghuang soaring through a sky painted in sunset colors of red, gold and orange. Its plumage is a stunning combination of crimson, gold and emerald feathers flowing in elegant curves. It carries flames of eternal life in its beak as golden sparks trail behind it.",
     ["Rebirth: Revive with 3 health when destroyed", "Flame Wing: Deal 2 damage to all enemies"],
     5, 6),

    ("Monkey King, Great Sage", 7, "Creature — Human",
     "the legendary Monkey King Sun Wukong in golden dragon scale armor with his iconic golden fillet around his head. He wields his massive Ruyi Jingu Bang golden staff that can change size. His monkey face shows fierce determination as golden clouds swirl around him with battle energy crackling.",
     ["Shape Shift: Transform into any minion in hand", "Staff Swing: Deal 3 damage and draw a card"],
     6, 6),

    ("Nuwa, Creator Goddess", 8, "God — Chinese",
     "the beautiful goddess Nuwa with the body of a human and the tail of a golden serpent, standing among the stars of the celestial realm. She holds a giant square carpenter's tool in one hand and a rectangular tool in the other, symbols of creating the world. Five colored divine stones float around her.",
     ["Creation: Summon a 2/2 Spirit", "Mend Heaven: Restore 6 health to your hero"],
     4, 8),

    ("Lei Gong, God of Thunder", 6, "God — Chinese",
     "the fierce thunder god Lei Gong with the body of a white bird and human face, wearing golden armor with wings. He strikes two hammers together creating massive bolts of blue lightning that illuminate the dark stormy sky. Clouds swirl around him as rain and hail fall upon the earth below.",
     ["Thunder Strike: Deal 5 damage to a minion", "Storm Call: Summon a 2/1 Lightning Spirit"],
     5, 5),

    ("Tortoise Dragon, Ancient Wisdom", 5, "Creature — Beast",
     "the ancient turtle-dragon hybrid rising from a mystical jade-colored lake, its shell covered in glowing golden Chinese characters of ancient wisdom. Its dragon head and tail contrast with the turtle's scaly green shell. Lotus flowers bloom around it as mist rises from the sacred waters.",
     ["Ancient Wisdom: Draw 2 cards", "Shell Defense: +3 Health, -1 Attack"],
     3, 7),

    ("Koi Fish, Rising Dragon", 2, "Creature — Beast",
     "the beautiful orange and white koi fish swimming upstream through a waterfall of sparkling jade water. Golden scales shimmer in the sunlight as it leaps toward a glowing dragon gate above. Cherry blossom petals float on the water surface, and green bamboo lines the riverbank.",
     ["Ascension: Becomes a 6/6 Dragon at turn 5", "Swift Swim: +2 Attack on your turn"],
     1, 3),

    ("Troll, Cave Dweller", 4, "Creature — Giant",
     "the massive green-skinned Chinese cave troll standing in a dimly lit underground cavern filled with glowing crystals. Its brutish face shows sharp yellowed teeth and a broken nose, wearing rough hide armor. It wields a massive stone club dripping with cave water. Stalactites and glowing purple crystals surround it.",
     ["Cave In: Deal 2 damage to all minions", "Stone Skin: +2 Health"],
     4, 5),

    ("Fa Wang, Fire Demon King", 8, "Creature — Demon",
     "the terrifying red-skinned demon king Fa Wang standing atop a mountain of burning bones, wearing ornate dark golden armor with flowing crimson cape. Three flaming demon swords orbit around him as a massive pillar of fire erupts behind his horned head. The sky above is filled with ash and embers.",
     ["Hellfire: Deal 3 damage to all enemies", "Demon Lord: All demons get +2 Attack"],
     7, 6),

    ("Panda, Sacred Beast", 3, "Creature — Beast",
     "the adorable yet majestic giant panda sitting cross-legged in a misty bamboo forest, meditating with golden chi energy glowing around its paws. Its black and white fur is pristine, and a small golden Buddhist bell hangs from a bamboo branch above. Sunlight filters through the green bamboo canopy.",
     ["Meditation: Restore 2 health each turn", "Bamboo Feast: Gain +1 Health per turn"],
     2, 4),

    ("Opportunity Fox, Nine Tails", 6, "Creature — Beast",
     "the mystical nine-tailed fox with nine flowing tails of pure white fur tipped in golden light, standing beneath a full moon. Its beautiful fox face has intelligent amber eyes, and its body is adorned with ancient Chinese talismans. Blue spirit flames dance around it as cherry blossoms fall.",
     ["Illusion: Copy a random enemy card", "Fox Fire: Deal 2 damage to all enemies"],
     4, 5),

    ("Warrior Guan Yu", 7, "Creature — Human",
     "the legendary warrior god Guan Yu riding his red horse into battle, wielding his massive 49-kilogram green dragon blade. He wears ornate green and gold armor with a flowing green cape, his long black beard streaming in the wind. His loyal horse gallops through a battlefield of dust and arrows.",
     ["Loyalty: +2 Attack for each friendly minion", "Dragon Blade: Deal 4 damage to a minion"],
     7, 5),

    ("Temple Guardian", 4, "Creature — Spirit",
     "the stone temple guardian statue coming to life, its massive granite form covered in moss and ancient Chinese carvings. Golden eyes glow from within its stone face as it raises a massive stone pillar to strike. Incense smoke swirls around the ancient temple steps behind it.",
     ["Stone Wall: Cannot be attacked directly", "Smash: Deal 2 damage when played"],
     3, 6),

    ("Lantern Bearer", 2, "Creature — Spirit",
     "the gentle ghostly spirit floating above the misty ground, holding a glowing golden paper lantern that illuminates its translucent white form. It wears flowing Han dynasty robes, and its long black hair drifts in the ethereal wind. Fireflies and spirit lights surround it in the dark mystical forest.",
     ["Guiding Light: Reveal enemy deck", "Spirit Touch: Deal 1 damage, draw a card"],
     2, 2),

    # === NORDIC/NORSE MYTHOLOGY (15 cards) ===
    ("Odin, Allfather", 10, "God — Norse",
     "the mighty Odin standing on the fields of Asgard, his single golden eye blazing with wisdom and power. He wears a wide-brimmed blue hat and flowing dark cloak, leaning on his spear Gungnir. Two ravens Huginn and Muninn circle above him, and the nine realms of Norse mythology glow behind him.",
     ["Raven's Wisdom: Draw 3 cards", "Gungnir's Throw: Deal 4 damage to any target"],
     8, 8),

    ("Thor, God of Thunder", 8, "God — Norse",
     "the mighty Thor charging into battle with his red hair and beard flowing wildly, wielding Mjolnir that crackles with blue lightning. He wears his signature red cape and iron gloves, his muscular form clad in chainmail armor. Lightning splits the sky as the rainbow Bifrost burns behind him.",
     ["Mjolnir Strike: Deal 5 damage to a minion", "Thunderous Charge: +2 Attack when attacking"],
     7, 7),

    ("Loki, God of Mischief", 6, "God — Norse",
     "the cunning Loki standing with a sly grin, his green and gold asymmetrical outfit matching his dual nature. His sharp features glow with magical energy as golden runes swirl around him. He holds a serpent's tail in one hand, and behind him, the world tree Yggdrasil twists through misty darkness.",
     ["Trickery: Copy an enemy minion's ability", "Shapeshift: Change form to any 3-cost minion"],
     5, 4),

    ("Freyja, Goddess of Love and War", 7, "God — Norse",
     "the stunning goddess Freyja riding a chariot pulled by two massive golden cats across the battlefield. She wears her famous falcon cloak of feathers and the necklace Brisingamen that glows with golden light. Her flowing red hair streams behind her as she throws a spear of war magic.",
     ["Valkyrie Call: Summon two 1/2 Valkyries", "Falcon Cloak: Fly and deal 2 damage"],
     5, 6),

    ("Fenrir, the Great Wolf", 7, "Creature — Beast",
     "the enormous wolf Fenrir howling at the blood-red moon of Ragnarok, its massive fur-covered body towering over the landscape. Each tooth is the size of a sword, and drool burns like acid where it hits the ground. The magical golden chain Gleipnir binds one of its paws as lightning strikes behind it.",
     ["Ragnarok: Deal 3 damage to everything when it dies", "Howl of Doom: Enemy minions lose 1 Attack"],
     6, 6),

    ("Raven, Odin's Messenger", 1, "Creature — Beast",
     "the sleek black raven perched on a weathered rune stone, its glossy feathers gleaming with golden magical energy. Its intelligent eye seems to see all things as ancient Norse runes glow faintly on the stone beneath its talons. Misty Nordic mountains rise in the background.",
     ["Scout: Reveal enemy's hand", "Fly: Can attack immediately"],
     1, 1),

    ("Valkyrie, Chooser of the Slain", 5, "Creature — Spirit",
     "the beautiful warrior maiden Valkyrie flying through stormy Nordic skies, wearing shining silver armor with a flowing red cape. She wields a spear and carries a golden horn, her wings of light spreading from her back. Fallen warriors float around her as she chooses souls for Valhalla.",
     ["Choose the Slain: Revive a friendly deathrattle minion", "Sky Dive: Deal 3 damage on attack"],
     4, 5),

    ("Troll, Mountain Dweller", 4, "Creature — Giant",
     "the massive green-skinned Norse troll standing in a snowy mountain cave, its brutish form covered in animal furs and rough stone armor. It wields a massive boulder as a weapon, its crooked teeth snapping. Ice crystals and snow swirl around the dark cave entrance behind it.",
     ["Stone Throw: Deal 3 damage to a minion", "Regenerate: Restore 2 health each turn"],
     4, 5),

    ("Dwarf, Master Smith", 3, "Creature — Dwarf",
     "the stout dwarf blacksmith standing in his fiery underground forge beneath Mount Eitri, his muscular arms covered in soot and scars. He wields a hammer that glows red-hot, striking a divine weapon on an anvil. Golden sparks fly everywhere as molten lava flows around his feet.",
     ["Forge: Give a minion +2 Attack", "Mjolnir Craft: Summon a 1/1 Construct"],
     2, 3),

    ("Yggdrasil, World Tree", 6, "Artifact — Relic",
     "the colossal world tree Yggdrasil stretching from the heavens to the underworld, its massive trunk covered in golden Norse runes. Golden leaves shimmer as roots of light extend into nine different realms visible around it. A golden dragon coils around the trunk, and misty clouds swirl at its base.",
     ["Nine Realms: Draw 1 card each turn", "Ancient Roots: +2 Health per turn"],
     0, 8),

    ("Frost Giant, Jotun", 6, "Creature — Giant",
     "the towering frost giant standing in an icy Nordic glacier, its massive blue-tinged body covered in ice crystals and fur. It wields a spear made of pure glacial ice that crackles with freezing energy. Snow and ice shards fly around it as the frozen wasteland stretches to endless icy horizons.",
     ["Frost Strike: Deal 2 damage and freeze", "Ice Body: +3 Health, cannot be damaged first turn"],
     5, 6),

    ("Rune Priest", 4, "Creature — Human",
     "the mysterious Norse rune priest standing in a circle of glowing blue runes carved into ancient stone, his long white beard flowing over fur robes. He raises a glowing rune stone that emits brilliant blue light as magical energy swirls around him. Runes float in the air forming ancient Norse symbols.",
     ["Rune Magic: Deal 3 damage to a minion", "Blessing: Give a minion +1 Attack and Shield"],
     3, 4),

    ("Berserker, Frenzy Warrior", 3, "Creature — Human",
     "the wild Norse berserker warrior roaring in battle frenzy, his bare muscular chest covered in blood and runic tattoos. His eyes glow red with rage as he wields two battle axes, his fur loincloth and wild red hair adding to his savage appearance. Fallen enemies and broken shields surround him.",
     ["Frenzy: +3 Attack but take 2 damage each turn", "War Cry: All friendly warriors get +1 Attack"],
     5, 3),

    ("Sleipnir, Eight-Legged Steed", 4, "Creature — Beast",
     "the magnificent eight-legged Norse horse Sleipnir galloping through the sky on clouds of gold and blue, its grey coat gleaming with magical energy. Its four powerful legs on each side move in impossible harmony as it leaps between the realms. Golden sparkles trail from its hooves.",
     ["Realm Walker: Can attack any lane", "Swift Gallop: +2 Attack, Fly"],
     4, 4),

    ("Mimir, God of Wisdom", 5, "Creature — Spirit",
     "the ancient head of Mimir floating in a mystical pool of golden liquid, his single wise eye glowing with cosmic knowledge. Roots and vines wrap around his weathered head as golden runes float in the liquid below. The well of wisdom shimmers with ancient magic beneath a starlit Nordic sky.",
     ["Wisdom of Mimir: Draw 2 cards, lose 1 health", "Ancient Knowledge: Reduce all costs by 1"],
     2, 3),

    # === CELTIC MYTHOLOGY (10 cards) ===
    ("Lugh, Long-Armed God", 8, "God — Celtic",
     "the mighty Celtic god Lugh standing in golden armor with his impossibly long arm extended, wielding the great spear Nuada that glows with solar energy. He wears a Celtic torc and flowing green cloak, his face showing both wisdom and battle fury. The Celtic sun wheel burns behind him in a golden sky.",
     ["Master of All: Gain all warrior abilities", "Spear of Light: Deal 5 damage to any target"],
     7, 7),

    ("Celtic Warrior, Shield Wall", 4, "Creature — Human",
     "the fierce Celtic warrior standing in a shield wall formation, his muscular form covered in blue woad paint and tribal tattoos. He wields a massive Celtic sword and round shield decorated with intricate spiral patterns. Green Irish countryside stretches behind him under stormy skies.",
     ["Shield Wall: +2 Attack while defending", "Celtic Fury: Deal 1 damage to attackers"],
     4, 4),

    ("Selkie, Sea Spirit", 3, "Creature — Spirit",
     "the beautiful selkie sea spirit rising from the misty Irish coast, her seal skin draped around her flowing form like a shimmering silver cloak. Her ethereal face glows with ocean magic as seaweed and pearls adorn her hair. The Celtic sea crashes against dark rocks behind her under a moonlit sky.",
     ["Sea Song: Restore 3 health to your hero", "Seal Form: Become untargetable for one turn"],
     2, 4),

    ("Celtic Dryad, Forest Guardian", 5, "Creature — Spirit",
     "the ancient Celtic dryad standing in a mystical Irish forest of giant oak trees, her body made of living bark and vines with flowers blooming from her hair. Golden fairy light surrounds her as Celtic spirals glow on the ancient standing stones behind her. Moss and ferns cover the forest floor.",
     ["Nature's Wrath: Deal 2 damage to all enemies", "Root Bind: Freeze a minion for one turn"],
     3, 6),

    ("Celtic Dragon, Emerald Beast", 7, "Creature — Dragon",
     "the majestic Celtic dragon coiling through emerald green mist in the Irish otherworld, its scales a brilliant jade green with gold Celtic knotwork patterns. Its fierce eyes glow golden as it breathes green fire across the mystical landscape. Ancient Celtic standing stones and misty mountains surround it.",
     ["Celtic Fire: Deal 3 damage to all enemies", "Otherworld: Cannot be targeted first turn"],
     6, 6),

    ("Morrigu, War Goddess", 7, "God — Celtic",
     "the terrifying Morrigan goddess in her triple form — maiden, mother, and crone — standing on a Celtic battlefield. She wears dark armor with a wolf pelt, her red hair flowing like blood. Black crows circle above as she raises her spear of war. The Celtic otherworld gate glows behind her.",
     ["War Dance: All your minions get +2 Attack", "Crow Form: Deal 4 damage, become untargetable"],
     6, 6),

    ("Celtic Fairy, Sidhe", 2, "Creature — Spirit",
     "the tiny luminous Celtic fairy (sidhe) floating in an enchanted Irish forest clearing, her delicate wings shimmering with golden pixie dust. She wears a dress of petals and leaves, her pointed ears peeking through flowing silver hair. Glowing mushrooms and fireflies illuminate the mystical woodland.",
     ["Pixie Dust: Deal 1 damage to a random enemy", "Fairy Magic: Draw a card"],
     1, 2),

    ("Celtic Giant, Fomorian", 6, "Creature — Giant",
     "the massive one-eyed Celtic sea giant the Fomorian rising from the stormy Irish Sea, his green scaly body covered in barnacles and seaweed. He wields a massive stone club with one enormous hand, his single yellow eye glowing with ancient fury. Waves crash around his massive legs.",
     ["Sea Smash: Deal 4 damage to a minion", "Tidal Crush: Destroy a random enemy minion"],
     6, 5),

    ("Celtic Hero, Cuchulainn", 7, "Creature — Human",
     "the legendary Celtic hero Cuchulainn in his war riastrachation, his body contorted with battle fury. His single eye protrudes from his head, his woad paint glowing blue, and his spear Gae Bulg gleams with magical energy. His wolf hound leaps beside him on the misty Celtic battlefield.",
     ["Warp Rage: +4 Attack but -2 Health", "Gae Bulg: Deal 5 damage to a minion"],
     8, 4),

    ("Celtic Cauldron, Dagda's Gift", 3, "Artifact — Relic",
     "the enormous Celtic cauldron of Dagda sitting on stone legs in a misty Irish grove, its bronze surface covered in glowing Celtic knots and spirals. Golden steam rises from within as magical energy pulses from its depths. Ancient Celtic carvings glow on the standing stones around it.",
     ["Endless Feast: Restore 5 health to your hero", "Magic Brew: Summon a random 2-cost minion"],
     0, 0),

    # === JAPANESE MYTHOLOGY (10 cards) ===
    ("Amaterasu, Sun Goddess", 10, "God — Japanese",
     "the radiant sun goddess Amaterasu standing in her golden heavenly palace, her long flowing black hair shimmering with solar light. She wears elegant white and gold kimono robes as golden rays of sunlight emanate from her form. Cherry blossoms float around her in the celestial realm of Takamagahara.",
     ["Heaven's Light: Deal 5 damage to all evil minions", "Solar Radiance: Restore 3 health each turn"],
     8, 8),

    ("Ryu, Dragon of Japan", 9, "Creature — Dragon",
     "the majestic Japanese dragon Ryu coiling through stormy clouds over Mount Fuji, its long serpentine body covered in crimson red scales with flowing golden whiskers. Its fierce dragon face has glowing amber eyes as it breathes blue spirit fire. Cherry blossoms and lightning fill the dramatic sky.",
     ["Spirit Fire: Deal 4 damage to a lane", "Dragon Flight: Fly and deal 2 on attack"],
     8, 7),

    ("Oni, Japanese Ogre", 5, "Creature — Giant",
     "the terrifying red-skinned Oni ogre standing in a dark Japanese forest, its massive muscular body covered in scales and tiger-skin loincloth. Two large horns protrude from its head, and it wields an iron kanabo club dripping with blood. Its fierce face shows sharp fangs as ghostly flames flicker around it.",
     ["Club Smash: Deal 4 damage to a minion", "Oni Rage: +3 Attack at night"],
     6, 5),

    ("Kami of the Forest", 4, "Creature — Spirit",
     "the ancient forest kami appearing as a glowing white deer with golden antlers covered in blooming flowers, standing in a mystical Japanese forest. Shinto shimenawa rope hangs from the ancient trees around it as golden light filters through the cherry blossom canopy. Spirit fireflies illuminate the sacred grove.",
     ["Forest Blessing: Restore 3 health to all friends", "Nature's Call: Summon a 1/2 Forest Spirit"],
     3, 4),

    ("Tengu, Mountain Warrior", 6, "Creature — Spirit",
     "the powerful red-faced Tengu warrior standing on a misty Japanese mountain peak, its long nose and crimson face gleaming in the moonlight. It wears traditional yamabushi robes and wields a royal scepter that glows with wind magic. Golden clouds swirl around the mountain temple behind it.",
     ["Wind Slash: Deal 3 damage to all enemies", "Mountain Flight: Fly"],
     5, 5),

    ("Kitsune, Fox Spirit", 4, "Creature — Beast",
     "the mystical nine-tailed fox spirit Kitsune sitting beneath a full moon in an ancient Japanese garden, its pristine white fur glowing with magical energy. Its nine tails fan out behind it like golden flames, and its intelligent amber eyes gleam with ancient wisdom. Torii gates line the path behind it.",
     ["Illusion: Copy an enemy card", "Fox Fire: Deal 2 damage to all enemies"],
     4, 3),

    ("Samurai, honorable Warrior", 6, "Creature — Human",
     "the noble Japanese samurai standing in full black and gold lacquered armor with a flowing red cape, his katana drawn and gleaming in the sunset. His face is hidden behind an intimidating dragon mask as cherry blossoms swirl around him. A traditional Japanese castle stands in the background.",
     ["Honor: +2 Attack if your health is higher", "Katana Strike: Deal 3 damage to a minion"],
     5, 5),

    ("Kappa, Water Imp", 2, "Creature — Beast",
     "the small green-skinned kappa water imp standing in a shallow Japanese stream, its dish-shaped water bowl on its head filled with shimmering liquid. It wears a traditional Japanese loincloth and holds a cucumber in its webbed hands. Water lilies and bamboo line the stream banks.",
     ["Water Splash: Deal 1 damage to all enemies", "Cucumber Trick: Draw a card"],
     2, 1),

    ("Yokai, Shadow Spirit", 5, "Creature — Demon",
     "the eerie yokai shadow spirit floating in a dark Japanese temple at night, its ghostly white form shaped like a floating kimono with no visible body. Its face shows a haunting spectral smile as it holds an ancient paper lantern. Shadows and candlelight create mysterious patterns on the temple walls.",
     ["Shadow Walk: Cannot be targeted first turn", "Fear: Enemy minions deal 1 less damage"],
     3, 5),

    ("Tanuki, Shape-shifting Racoon", 3, "Creature — Beast",
     "the jolly tanuki raccoon dog sitting under a large leaf like an umbrella, its round body wearing a traditional Japanese straw hat and sash. It holds a golden sake flask in one paw and a money bag in the other, with magical leaves swirling around it. A beautiful Japanese garden lies behind.",
     ["Shape Shift: Transform into a 3-cost minion", "Sake Party: Restore 2 health to your hero"],
     2, 3),

    # === MESOPOTAMIAN MYTHOLOGY (10 cards) ===
    ("Ishtar, Goddess of War and Love", 8, "God — Mesopotamian",
     "the stunning Mesopotamian goddess Ishtar floating above ancient Babylon, her golden form adorned with elaborate jewelry and a tiered horned headdress. She wields a sharp war axe in one hand and a rose in the other. Lions of gold flank her as the ziggurats of Babylon rise into a starry sky.",
     ["War and Love: Deal 3 damage or restore 3 health", "Lion's Roar: Give all minions +2 Attack"],
     6, 7),

    ("Gilgamesh, King of Heroes", 8, "Creature — Human",
     "the legendary half-god king Gilgamesh standing in golden armor made of scales, his muscular form covered in heroic scars. He wields a massive bronze sword and lion-skin shield, his long blond hair flowing freely. The walls of Uruk stretch behind him as lions roam the Mesopotamian plains.",
     ["Hero's Might: +2 Attack for each enemy defeated", "Immortal Blood: Restore 3 health when below half"],
     7, 7),

    ("Tiamat, Mother of Monsters", 9, "Creature — Dragon",
     "the terrifying primordial dragon Tiamat rising from the salt ocean, her massive body half animal and part divine with five fierce beast heads — lion, bear, dog, eagle, and scorpion. Her scaled body coils through stormy Mesopotamian skies as lightning illuminates her terrifying form.",
     ["Primordial Breath: Deal 4 damage to all lanes", "Monster Birth: Summon a random 2-cost beast"],
     7, 8),

    ("Lamassu, Protective Spirit", 5, "Creature — Spirit",
     "the massive protective Lamassu spirit standing before the great gates of Nineveh, its body of a bull with the head of a human wearing a horned crown and flowing beard. Golden eagle wings spread wide as intricate cuneiform carvings glow on its bronze body. Ancient Mesopotamian architecture surrounds it.",
     ["Divine Protection: Prevent 5 damage to your hero", "Wing Shield: +2 Health for all friendly minions"],
     4, 7),

    ("Enuma Elish, Creation Song", 6, "Spell — Ritual",
     "the ancient Mesopotamian creation story visualized as golden cuneiform symbols floating in a cosmic void of swirling blue and gold energy. The primordial gods Apsu and Tiamat emerge from the waters of creation as golden light forms the heavens and earth. Stars and galaxies swirl in the background.",
     ["Create World: Summon a 4/4 Creation Spirit", "Ancient Power: Reduce all costs by 2 this turn"],
     0, 0),

    ("Scorpion Man, Scorpius", 4, "Creature — Beast",
     "the fearsome scorpion man Scorpius standing in the Mesopotamian underworld, his muscular human torso rising from a massive scorpion body with a thick stinger tail. His scorpion head gleams with golden armor plating as dark energy crackles from his pincers. Skulls and bones litter the underworld floor.",
     ["Venom Stinger: Deal 3 damage, poison", "Underworld: +2 Attack in dark areas"],
     4, 4),

    ("Enkidu, Wild Man", 5, "Creature — Beast",
     "the wild man Enkidu standing in the Mesopotamian plains, his body covered in thick brown fur with goat hooves for feet. His fierce face shows wild determination as he wrestles a lion beside him. Golden grass and ancient trees stretch across the vast open landscape under a bright sky.",
     ["Wild Strength: Deal 3 damage to a minion", "Nature's Bond: +1 Attack for each beast"],
     5, 4),

    ("Ziggurat, Temple of Heaven", 3, "Artifact — Structure",
     "the massive stepped ziggurat temple of Mesopotamia rising into a starry sky, its tiered structure made of glazed blue and gold bricks with cuneiform inscriptions. Incense smoke rises from the top shrine where golden flames burn eternally. The ancient city of Ur stretches below.",
     ["Heaven's Touch: Draw 1 card each turn", "Sacred Ground: Minions here get +1 Attack"],
     0, 4),

    ("Dumuzi, Shepherd God", 3, "God — Mesopotamian",
     "the gentle shepherd god Dumuzi standing in a lush Mesopotamian garden, wearing flowing white robes and a golden crown of reeds. He holds a staff that sprouts flowers, and sheep graze peacefully behind him. Golden sunlight illuminates the fertile crescent landscape with blooming gardens.",
     ["Shepherd's Call: Summon a 1/3 Lamb", "Abundance: Restore 2 health each turn"],
     2, 4),

    ("Ningirsu, God of War", 7, "God — Mesopotamian",
     "the mighty Sumerian war god Ningirsu in massive bronze armor with a lion's helmet, wielding a great mace that crackles with storm energy. He stands in a chariot pulled by lions as the battlefield of ancient Sumer burns behind him. Thunderclouds and golden lightning fill the sky.",
     ["War Mace: Deal 4 damage to a minion", "Storm Charge: +2 Attack when charging"],
     6, 6),

    # === HINDU MYTHOLOGY (10 cards) ===
    ("Vishnu, Preserver of the Universe", 10, "God — Hindu",
     "the supreme god Vishnu floating in the cosmic ocean of creation, his four arms holding the conch shell, discus, lotus flower, and mace. His blue skin glows with divine light as he wears golden jewelry and a crown. The infinite cosmic universe with galaxies swirls behind him.",
     ["Preserve Universe: Restore 5 health to all friends", "Discus Throw: Deal 4 damage to any target"],
     8, 10),

    ("Shiva, Destroyer of Evil", 9, "God — Hindu",
     "the fierce god Shiva dancing the cosmic Tandava in the center of a ring of fire, his blue skin glowing with divine energy. His third eye opens in the center of his forehead as the sacred Ganges river flows from his matted hair. The trident (trishul) spins around him as Mount Kailash burns in the background.",
     ["Cosmic Dance: Deal 3 damage to everything", "Third Eye: Destroy any minion once per game"],
     8, 7),

    ("Ganesha, Elephant God", 5, "God — Hindu",
     "the beloved elephant-headed god Ganesha sitting in a lotus position, his large human body with an elephant head adorned in golden jewelry and sacred threads. He holds a modak sweet in one hand and breaks his tusk with the other. Colorful flowers and sacred symbols surround him in a temple setting.",
     ["Wisdom: Remove one obstacle — destroy any minion", "Modak Blessing: Restore 3 health to your hero"],
     4, 6),

    ("Hanuman, Monkey God", 7, "Creature — Beast",
     "the mighty monkey god Hanuman soaring through the sky on golden wings of divine energy, his muscular form covered in golden fur. He wields a massive golden mace overhead as the sacred Ram name glows on his chest. Mountains and clouds stretch below him in the vast Indian sky.",
     ["Divine Strength: +4 Attack when below half health", "Mace Swing: Deal 3 damage to all enemies"],
     7, 6),

    ("Devi, Great Goddess", 8, "God — Hindu",
     "the fierce goddess Devi in her warrior form riding a lion, wielding eight arms each holding a divine weapon from the gods. Her golden skin glows with power as she wears elaborate red and gold sari with a fierce determined expression. The demon Mahishasura falls beneath her lion's claws.",
     ["Divine Weapons: Deal 2 damage to all enemies", "Mother's Blessing: All Hindu cards cost 1 less"],
     6, 7),

    ("Naga, Serpent Spirit", 4, "Creature — Beast",
     "the majestic multi-headed Naga serpent rising from a mystical Indian lake, its emerald green scales gleaming with precious gemstones embedded in its hood. Its five cobra heads fan out in a protective canopy, each eye glowing with ancient magical energy. Lotus flowers and golden water surround it.",
     ["Venom: Deal 2 damage to all enemies on attack", "Serpent Coils: +1 Attack per Naga played"],
     3, 5),

    ("Apsara, Celestial Dancer", 3, "Creature — Spirit",
     "the beautiful celestial Apsara dancer performing in the heavenly courts of Svarga, her golden body adorned with flowing silk and elaborate jewelry. She wears a shimmering sari of pearl and gold as divine flowers rain down around her. Musical instruments float in the air as angels watch from golden clouds.",
     ["Enchanting Dance: Charm an enemy minion", "Celestial Grace: +1 Attack and Health"],
     2, 3),

    ("Asura, Demon Lord", 7, "Creature — Demon",
     "the massive Asura demon lord standing in his dark fortress, his blue-green muscular form covered in dark armor and fierce tattoos. Three eyes burn with rage on his face as he wields a massive trident dripping with dark energy. Flames and smoke fill the demonic realm behind him.",
     ["Demon Power: +2 Attack for each demon played", "Chaos Strike: Deal 3 damage, take 2 damage"],
     6, 6),

    ("Garuda, Bird God", 6, "Creature — Beast",
     "the mighty Garuda bird god soaring through the Indian sky, his golden eagle body with powerful wings of brilliant gold and crimson. His human torso gleams with divine armor as he carries a massive golden mace. The sun glints off his feathers as mountains and clouds stretch below.",
     ["Solar Dive: Deal 4 damage to a minion", "Divine Flight: Fly and cannot be blocked"],
     5, 5),

    ("Brahma, Creator of All", 9, "God — Hindu",
     "the four-headed god Brahma sitting upon a golden lotus flower in the cosmic void of creation, his four heads looking in all directions. He holds the Vedas, a water pot, prayer beads, and a spoon as golden light of creation emanates from him. The first flowers of existence bloom around him.",
     ["Creation: Summon a random 3-cost minion", "Four Vedas: Draw 2 cards each turn"],
     5, 8),

    # === AZTEC / MAYAN MYTHOLOGY (10 cards) ===
    ("Quetzalcoatl, Feathered Serpent", 9, "God — Aztec",
     "the magnificent feathered serpent god Quetzalcoatl coiling through the sky above Aztec pyramids, its body half golden eagle and half jade serpent. Brilliant green and gold feathers flow along its serpentine body as it breathes wind magic. The great temple of Tenochtitlan rises below under a starry sky.",
     ["Wind Storm: Deal 3 damage to all enemies", "Feathered Flight: Fly and deal 2 on attack"],
     7, 8),

    ("Huitzilopochtli, Sun God of War", 8, "God — Aztec",
     "the fierce Aztec sun and war god Huitzilopochtli standing in golden armor with a turquoise serpent spear, his blue body adorned with gold and jade. Hummingbird feathers decorate his headdress as blood drips from the temple steps below him. The Aztec sun burns brilliantly behind him.",
     ["Sun Sacrifice: Deal 4 damage to a minion", "War Dance: All Aztec minions get +2 Attack"],
     7, 6),

    ("Aztec Warrior, Eagle Knight", 5, "Creature — Human",
     "the fierce Aztec eagle warrior knight standing in full costume with a jaguar pelt helmet shaped like an eagle's head and golden eagle feather wings. He wields a macuahuitl obsidian sword and wears ornate gold jewelry. The great Aztec pyramid of Tenochtitlan rises behind him.",
     ["Obsidian Blade: Deal 3 damage to a minion", "Eagle Spirit: +2 Attack during the day"],
     5, 4),

    ("Mayan Ball Player", 3, "Creature — Human",
     "the athletic Mayan ball player in full ceremonial jade armor standing on the ancient stone ball court, his hip cushion made of carved jade gleaming. He holds a rubber ball that glows with magical energy as stone Mayan gods watch from the stands. Jungle canopy surrounds the court.",
     ["Ball Throw: Deal 3 damage to a minion", "Jade Armor: +2 Health"],
     3, 3),

    ("Aztec Skull, Totopotstli", 2, "Creature — Undead",
     "the decorated Aztec skull Totopotstli sitting on a stone altar covered in gold and jade ornaments, its eye sockets glowing with purple magical energy. Marigold petals and cop incense smoke surround it as the Aztec calendar stone rests beneath. Dark temple walls close in behind.",
     ["Death Touch: Deal 1 damage, heal 1 health", "Skull Count: +1 Attack per skull destroyed"],
     2, 1),

    ("Mayan Jaguar Priest", 5, "Creature — Human",
     "the mysterious Mayan jaguar priest standing in a dim jungle temple, wearing a full jade jaguar helmet and spotted pelt robe. His glowing green eyes peer from the shadows as he holds a sacred cenote water vessel. Jade carvings and hieroglyphs glow on the temple walls around him.",
     ["Jaguar Pounce: Deal 3 damage to a minion", "Night Stalker: +2 Attack at night"],
     4, 4),

    ("Xolotl, Dog of the Dead", 4, "Creature — Beast",
     "the muscular dog-headed god Xolotl standing at the entrance to the Aztec underworld Mictlan, his canine form covered in golden tattoos and jade ornaments. His fierce eyes glow as he guides souls with a bone staff. Fireflies and marigold flowers light the path through the dark realm.",
     ["Soul Guide: Draw a card when a minion dies", "Underworld Guard: +2 Attack vs spirits"],
     3, 4),

    ("Mayan Hero Twins", 6, "Creature — Human",
     "the two Mayan hero twins Hunahpu and Xbalanque standing side by side in ceremonial ball player armor, one holding a maize staff and the other a fire drill. Their faces glow with divine energy as the ball court of Xibalba (underworld) opens behind them with skeletal watchers.",
     ["Twin Strike: Deal 2 damage to two random enemies", "Resurrection: Both return if one is destroyed"],
     5, 5),

    ("Aztec Sun Stone", 4, "Artifact — Relic",
     "the massive Aztec sun stone calendar floating in mid-air, its circular surface covered in intricate carved glyphs and symbols of Aztec time cycles. Golden light pulses from the center face of Tonatiuh the sun god as sacred fire burns around its edges. Dark temple stones surround it.",
     ["Time Cycle: Extra turn at the end of this one", "Calendar Power: Play two cards next turn"],
     0, 0),

    ("Coatlicue, Mother of Gods", 7, "God — Aztec",
     "the terrifying Aztec mother goddess Coatlicue standing in her serpent form, her skirt made entirely of intertwined snaking serpents with a necklace of hands and eyes. Her two serpent heads at the neck represent breath and death, and her face shows a serene yet fearsome expression. Volcanic mountains rise behind her.",
     ["Serpent Mother: Summon a 2/3 Serpent", "Earthquake: Deal 3 damage to all minions"],
     5, 8),

    # === OTHER MYTHOLOGIES (10 cards) ===
    ("Anansi, Spider God of Stories", 4, "God — African (Akan)",
     "the trickster spider god Anansi sitting at the center of a massive cosmic web that connects all stories, his large spider body wearing colorful African cloth. Golden threads of tales and legends weave through the web around him as African village life plays out below in miniature scenes.",
     ["Web of Tales: Copy an enemy card", "Trickster: Swap stats with a random minion"],
     3, 4),

    ("Amaterasu's Mirror", 3, "Artifact — Relic",
     "the sacred Yata no Kagami bronze mirror of Japan floating in a golden void, its polished surface reflecting divine light that illuminates the heavens. Intricate gold and silver patterns decorate the circular mirror as sacred paper streamers hang from its handle. Heavenly cherry blossoms float around it.",
     ["True Reflection: Reveal all enemy cards", "Divine Light: Deal 2 damage to demons"],
     0, 0),

    ("Dragon Phoenix Reunion", 5, "Spell — Blessing",
     "the Chinese dragon and phoenix meeting in a brilliant display of cosmic balance, the green golden dragon coiling around the crimson gold phoenix as they circle each other in the clouds. Golden and red energy merges between them creating a symbol of perfect harmony as celestial flowers bloom.",
     ["Harmony: Give all minions +2/+2", "Union: Summon a 4/4 Dragon Phoenix"],
     0, 0),

    ("Bifrost Guardian", 4, "Creature — Spirit",
     "the mighty Bifrost rainbow bridge guardian standing at the edge of Asgard, his massive armored form glowing with the colors of the rainbow bridge. He wields a spear that crackles with rainbow energy as the colorful Bifrost stretches across the sky behind him. Golden Asgardian halls rise above.",
     ["Rainbow Strike: Deal 3 damage to a minion", "Bridge Guard: +1 Attack per realm crossed"],
     4, 4),

    ("Kamui, Ainu Spirit", 5, "Creature — Spirit",
     "the mysterious Ainu kamui spirit appearing as a luminous white bear with golden antlers and flowing silver fur, standing in the misty mountains of Hokkaido. Sacred shimenawa ropes hang from ancient trees as spirit fire illuminates the pristine wilderness. Snow falls gently around it.",
     ["Spirit Bear: Deal 2 damage to all enemies", "Ainu Blessing: Restore 3 health to your hero"],
     4, 5),

    ("Thunderbird, Native American", 8, "Creature — Beast",
     "the enormous Thunderbird soaring across the sky above the North American plains, its massive wingspan creating clouds and lightning with each flap. Its eagle form gleams in golden sunlight as bolts of blue lightning crackle from its beak and talons. Native American mountains and canyons stretch below.",
     ["Lightning Storm: Deal 5 damage to all enemies", "Sky Lord: Fly and deal 3 on attack"],
     7, 7),

    ("Cernunnos, Horned God", 6, "God — Celtic",
     "the ancient Celtic horned god Cernunnos sitting cross-legged in a mystical forest, his antler crown of golden deer horns branching majestically. His muscular form is covered in gold torcs and bracelets as a serpent and ram flank him on either side. Animals gather around him in the sacred grove.",
     ["Lord of Beasts: All beasts get +2 Attack", "Nature's Gift: Restore 2 health per turn"],
     4, 6),

    ("Sedna, Goddess of the Sea", 5, "God — Inuit",
     "the Inuit sea goddess Sedna rising from the dark Arctic ocean, her lower body a massive seal tail covered in blue scales. Her long black hair flows with seaweed and pearls, her face showing both sorrow and power. Arctic icebergs and northern lights glow above the frozen waters.",
     ["Ocean's Wrath: Deal 3 damage to all minions", "Deep Sea: Freeze enemies for one turn"],
     4, 6),

    ("Muspellfire Giant", 7, "Creature — Giant",
     "the massive fire giant Surtr standing at the fields of Ragnarok, his enormous form made entirely of molten rock and burning flame. He wields the flaming sword of Muspell that burns brighter than the sun. Lava flows around his feet as the world burns in the Norse apocalypse behind him.",
     ["World Fire: Deal 4 damage to everything", "Flame Sword: +3 Attack, takes 1 damage per turn"],
     8, 6),

    ("Cosmic Turtle, World Bearer", 6, "Creature — Beast",
     "the enormous cosmic turtle swimming through the void of creation, its massive ancient shell covered in glowing symbols from all mythologies. Golden constellations and stars swirl around it as the world rests upon its broad back. Ethereal cosmic mist and nebulae fill the background.",
     ["World Shell: +4 Health, immune to damage first turn", "Ancient Wisdom: Draw 1 card each turn"],
     4, 8),
]

# Generate all files
for card in cards:
    name = card[0].replace(" ", "_")
    content = make_card(*card)
    filepath = os.path.join(OUTPUT_DIR, f"{name}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated {len(cards)} card prompt files in '{OUTPUT_DIR}/'")