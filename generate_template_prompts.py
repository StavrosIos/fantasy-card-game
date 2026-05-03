#!/usr/bin/env python3
"""Generate card frame template .txt files for a mythology-based card game.

These templates describe the card FRAME/BORDER only — no specific character,
no artwork, just the ornamental frame with empty slots for image, text box,
mana cost, attack and health. You generate the frame first, then overlay
your character artwork + text later via Python or HTML."""

import os

OUTPUT_DIR = "card_templates"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def make_frame_template(name, mana_cost_slot_pos, artwork_box_desc, text_box_desc,
                        stats_bar_desc, frame_style):
    """Generate a card frame template prompt."""
    return f"""A single, professionally designed empty fantasy trading card FRAME displayed in a straight-on, flat view, perfectly centered and fully visible with no perspective distortion. The card is completely empty — no character artwork, no name, no text content — just the ornamental frame structure with clearly defined empty slots.

The card has a clean neutral background for easy cropping and compositing.

{frame_style}

At the top of the card is a clearly defined horizontal bar area for the card name, with a circular slot at the top-right corner for the mana cost icon. The name bar is empty and blank.

Below the name bar is a large rectangular artwork slot — completely empty white/neutral space where character artwork will be placed later. The artwork area has a clean border matching the card frame design.

Below the artwork slot is a narrow horizontal type line bar — empty and blank, where creature type text will be added later.

Beneath that is a clearly separated rectangular text box area — completely empty white/neutral space where card ability text will be added later. The text box has a subtle inner border and clean sharp edges.

At the bottom of the card is a polished horizontal stats bar with two circular slots: one on the left for Attack value and one on the right for Health value. Both circles are empty and blank.

The entire layout is clean, balanced, and symmetrical with consistent spacing. All frame elements are crisp and well-defined. No blur, no distortion, no warped text, no artwork inside the slots.

Style tags: high fantasy, trading card game, ultra-detailed, sharp focus, professional UI design, clean layout, print-ready, empty frame template
"""


# ============================================================
# GREEK MYTHOLOGY FRAMES (4 styles)
# ============================================================
greek_frames = [
    ("Greek_Marble_Gold_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with ornate golden Greek key (meander) pattern borders",
     "A rectangular text box below the artwork with a subtle Greek key border pattern in gold",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), decorated with golden laurel wreath motifs",
     """The card frame is made of polished white marble with gold inlay. The outer border features an intricate Greek key (meander) pattern in gold. The corners are adorned with golden acanthus leaf carvings. The frame has a slight 3D beveled edge effect giving it depth. The color palette is white marble, gold, and deep blue accents. The frame has a divine, celestial Greek temple aesthetic with subtle glowing golden energy lines running through the marble surface."""),

    ("Greek_Bronze_Warrior_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with bronze and dark stone border panels",
     "A rectangular text box below the artwork with a dark bronze inner frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as bronze shield emblems",
     """The card frame is made of polished bronze with dark stone inlay. The outer border features embossed Greek warrior helmet and shield motifs at regular intervals. The corners have golden eagle head ornaments. The frame has a battle-worn metallic texture with subtle scratches and patina. The color palette is bronze, dark grey stone, and crimson red accents. The frame has a martial, heroic Greek warrior aesthetic with angular geometric patterns."""),

    ("Greek_Olympus_God_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with radiant golden sunburst borders",
     "A rectangular text box below the artwork with a glowing golden energy border",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden divine energy",
     """The card frame is made of luminous celestial gold with translucent crystal panels. The outer border radiates outward like a sunburst with golden light rays emanating from the center. Thunderbolt motifs decorate each corner. The frame has a divine glow effect with subtle animated-looking energy lines. The color palette is brilliant gold, white light, and electric blue accents. The frame has a supreme god-of-Olympus aesthetic with ethereal light effects."""),

    ("Greek_Temple_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple Doric column border design",
     "A rectangular text box below the artwork with a clean stone-textured frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), simple stone-carved circles",
     """The card frame is made of light grey marble with minimal gold decoration. The outer border features simplified Doric column capitals at the top and bottom edges. The corners have small olive leaf motifs carved in stone. The frame has a clean, classical Greek architectural aesthetic with subtle stone texture. The color palette is light grey marble, pale gold, and soft green accents."""),
]

# ============================================================
# EGYPTIAN MYTHOLOGY FRAMES (4 styles)
# ============================================================
egyptian_frames = [
    ("Egyptian_Gold_Papyrus_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with golden Egyptian hieroglyphic border panels",
     "A rectangular text box below the artwork with a golden ankh-patterned inner border",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as golden scarab beetle emblems",
     """The card frame is made of solid gold with lapis lazuli inlay. The outer border features intricate Egyptian hieroglyphs carved in gold running continuously around the perimeter. The corners are adorned with golden falcon heads (Horus) facing outward. The top center has a glowing solar disk motif. The frame has a rich, luxurious ancient Egyptian temple aesthetic with detailed gold relief work. The color palette is brilliant gold, deep blue lapis lazuli, and emerald green accents."""),

    ("Egyptian_Obsidian_Jackal_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with black obsidian and gold border panels",
     "A rectangular text box below the artwork with a dark stone inner frame and gold hieroglyph accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as black obsidian discs with gold rims",
     """The card frame is made of polished black obsidian with thin gold trim. The outer border features a repeating pattern of Egyptian eye of Horus symbols in gold. The corners have jackal-headed (Anubis) silhouettes in gold leaf. The frame has a mysterious, underworld tomb aesthetic with subtle purple magical glow emanating from the hieroglyphs. The color palette is black obsidian, gold, and deep purple accents."""),

    ("Egyptian_Sun_Disk_God_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with radiant golden sun disk and winged scarab borders",
     "A rectangular text box below the artwork with a golden papyrus-textured inner frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden solar rays",
     """The card frame is made of brilliant gold with a large sun disk (Ra) motif at the top center. The outer border features golden winged scarab beetles at regular intervals. The frame has a radiant, divine Egyptian sun god aesthetic with golden light rays emanating from the top. The color palette is brilliant gold, warm amber, and bright orange accents."""),

    ("Egyptian_Sandstone_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple sandstone border design",
     "A rectangular text box below the artwork with a stone-textured frame and faint hieroglyphic patterns",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), carved into stone",
     """The card frame is made of warm sandstone with minimal gold decoration. The outer border features simplified Egyptian lotus flower and papyrus plant motifs carved into the stone surface. The corners have small Ankh symbols. The frame has a clean, ancient Egyptian temple wall aesthetic with subtle sandstone texture and weathering. The color palette is warm tan sandstone, pale gold, and soft turquoise accents."""),
]

# ============================================================
# CHINESE MYTHOLOGY FRAMES (4 styles)
# ============================================================
chinese_frames = [
    ("Chinese_Jade_Dragon_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with ornate jade and gold dragon-scale border panels",
     "A rectangular text box below the artwork with a jade-green inner frame and golden cloud patterns",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as golden yin-yang discs",
     """The card frame is made of translucent imperial jade with gold inlay. The outer border features a coiling golden Chinese dragon wrapping around the entire perimeter, its scales detailed and shimmering. The corners have golden phoenix ornaments. The top center has a flaming pearl of wisdom motif. The frame has an imperial Chinese palace aesthetic with intricate gold filigree work on jade background. The color palette is deep emerald jade, brilliant gold, and crimson red accents."""),

    ("Chinese_Porcelain_Warrior_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with blue-and-white porcelain border panels",
     "A rectangular text box below the artwork with a porcelain-textured inner frame and painted cloud motifs",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as porcelain medallions",
     """The card frame is made of white porcelain with traditional blue Chinese painted patterns. The outer border features hand-painted Chinese landscape scenes (mountains, rivers, clouds) in cobalt blue. The corners have golden dragon head ornaments. The frame has an elegant Chinese porcelain vase aesthetic with delicate brush-painted details. The color palette is white porcelain, cobalt blue, and gold accents."""),

    ("Chinese_Heavenly_Empire_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with golden celestial palace border design",
     "A rectangular text box below the artwork with a golden cloud-patterned inner frame and red lacquer accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden celestial energy",
     """The card frame is made of gold and red lacquer with jade inlay. The outer border features golden Chinese cloud patterns (xiangyun) and flaming pearl motifs. The corners have golden guardian lion (foo dog) heads. The top center has a golden imperial crown motif. The frame has a majestic Chinese heavenly palace aesthetic with rich red and gold imperial colors. The color palette is imperial red, brilliant gold, and jade green accents."""),

    ("Chinese_Bamboo_Scroll_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple bamboo scroll border design",
     "A rectangular text box below the artwork with a parchment-textured frame and bamboo border accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), simple carved wood circles",
     """The card frame is made of light bamboo wood with parchment paper accents. The outer border features carved bamboo stalk patterns in a repeating sequence. The corners have small lotus flower carvings. The frame has a serene Chinese scholar's garden aesthetic with natural wood grain texture. The color palette is warm bamboo brown, parchment cream, and soft green accents."""),
]

# ============================================================
# NORDIC/NORSE MYTHOLOGY FRAMES (4 styles)
# ============================================================
norse_frames = [
    ("Norse_Runic_Iron_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with iron and rune-etched border panels",
     "A rectangular text box below the artwork with a runic inner frame and Norse knotwork border",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as iron rings with rune inscriptions",
     """The card frame is made of dark forged iron with silver rune inscriptions. The outer border features a continuous band of Norse runes (Elder Futhark) glowing with faint blue magical energy. The corners are adorned with interlocking Norse knotwork in silver. The top center has a stylized Valknut symbol. The frame has a rugged Viking Age aesthetic with hammer-textured iron surface and subtle crackle effects. The color palette is dark iron grey, silver runes, and icy blue accents."""),

    ("Norse_Viking_Sword_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with battle-worn steel and leather border panels",
     "A rectangular text box below the artwork with a dark leather-textured inner frame and metal rivet accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as shield boss emblems",
     """The card frame is made of polished steel with dark leather wrapping along the edges. The outer border features embossed Viking longship and wolf motifs in steel relief. The corners have interlocking dragon head ornaments (like the Oseberg ship carvings). The frame has a battle-hardened Viking warrior aesthetic with visible hammer marks and steel texture. The color palette is steel grey, dark brown leather, and bronze accents."""),

    ("Norse_Rainbow_Bifrost_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with rainbow energy border design",
     "A rectangular text box below the artwork with a glowing Asgardian inner frame and golden Norse patterns",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by rainbow energy",
     """The card frame is made of golden Asgardian metal with rainbow crystal inlay. The outer border features the colors of the Bifrost rainbow flowing continuously around the perimeter like liquid light. The corners have golden winged helmet ornaments. The top center has a stylized Yggdrasil world tree motif in gold. The frame has a divine Norse celestial aesthetic with shimmering rainbow light effects. The color palette is golden Asgardian metal, rainbow crystal colors, and bright white light accents."""),

    ("Norse_Stone_Runestone_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple runestone border design",
     "A rectangular text box below the artwork with a stone-textured frame and carved rune accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), carved into stone surface",
     """The card frame is made of grey granite with carved rune markings. The outer border features simplified Norse runic alphabet symbols carved into the stone surface. The corners have basic interlocking knotwork patterns. The frame has a weathered Viking runestone aesthetic with natural stone texture and moss accents. The color palette is grey granite, dark green moss, and pale gold accents."""),
]

# ============================================================
# CELTIC MYTHOLOGY FRAMES (4 styles)
# ============================================================
celtic_frames = [
    ("Celtic_Knotwork_Gold_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with intricate Celtic knotwork gold border panels",
     "A rectangular text box below the artwork with a golden spiral and knotwork inner frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as golden Celtic torc discs",
     """The card frame is made of polished gold with emerald inlay. The outer border features an incredibly intricate Celtic knotwork pattern (triskele, triquetra, and interlacing) in continuous flowing design. The corners have elaborate Celtic spiral carvings in gold. The top center has a golden Celtic cross motif. The frame has an ancient Irish high-cross aesthetic with detailed gold filigree and enamel work. The color palette is brilliant gold, deep emerald green, and bronze accents."""),

    ("Celtic_Oak_Warrior_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with carved oak wood and bronze border panels",
     "A rectangular text box below the artwork with a dark oak-textured inner frame and bronze spiral accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as carved wooden discs with bronze rims",
     """The card frame is made of dark polished oak wood with bronze metal fittings. The outer border features carved Celtic spiral and zoomorphic patterns in the wood surface. The corners have bronze interlocking animal head ornaments. The frame has a mystical Irish forest druid aesthetic with natural wood grain and weathered bronze patina. The color palette is dark oak brown, bronze, and forest green accents."""),

    ("Celtic_Sidhe_Fairy_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with ethereal fairy-gold border design",
     "A rectangular text box below the artwork with a glowing fairy-light inner frame and Celtic spiral patterns",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden fairy dust",
     """The card frame is made of luminous pearlescent material with gold filigree. The outer border features flowing Celtic knotwork that appears to glow with inner fairy light. The corners have golden leaf and flower ornaments (oak, shamrock, hawthorn). The top center has a golden Celtic sun wheel motif. The frame has an otherworldly Irish fairy realm aesthetic with shimmering ethereal light effects and subtle sparkle. The color palette is pearlescent white, gold fairy-light, and soft green accents."""),

    ("Celtic_Stone_Cromlech_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple standing stone border design",
     "A rectangular text box below the artwork with a stone-textured frame and carved spiral accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), carved into stone surface",
     """The card frame is made of grey weathered stone with moss growth. The outer border features carved Celtic spiral and triskele symbols into the stone surface. The corners have simple megalithic geometric patterns. The frame has an ancient Irish passage tomb (Newgrange) aesthetic with natural stone texture and moss. The color palette is grey stone, green moss, and pale gold accents."""),
]

# ============================================================
# JAPANESE MYTHOLOGY FRAMES (4 styles)
# ============================================================
japanese_frames = [
    ("Japanese_Kimono_Silk_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with ornate gold-leaf and lacquer border panels",
     "A rectangular text box below the artwork with a gold-leaf inner frame and traditional Japanese pattern (seigaiha waves or asanoha hemp leaf)",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as golden mon (family crest) discs",
     """The card frame is made of black lacquer with gold leaf decoration. The outer border features traditional Japanese patterns (seigaiha waves, asanoha hemp leaf, or shippu wind swirls) in gold leaf. The corners have golden chrysanthemum ornaments. The top center has a golden Japanese sun disk motif (inspiration for the flag). The frame has an elegant Edo-period kimono and lacquerware aesthetic with rich black and gold contrast. The color palette is deep black lacquer, brilliant gold leaf, and crimson red accents."""),

    ("Japanese_Samurai_Armor_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with lacquered armor plate border design",
     "A rectangular text box below the artwork with a dark lacquered inner frame and metal rivet accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as kabuto helmet visor emblems",
     """The card frame is made of dark lacquered armor plates with gold metal fittings. The outer border features overlapping scale (scale) pattern like samurai armor, each plate individually lacquered. The corners have golden dragon or tiger head ornaments (like armor helmet decorations). The frame has a battle-ready samurai aesthetic with lacquer sheen and metal texture. The color palette is black/dark red lacquer, gold fittings, and silver accents."""),

    ("Japanese_Heavenly_Palace_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with celestial golden border design",
     "A rectangular text box below the artwork with a glowing golden inner frame and cloud patterns (hisagi)",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden celestial energy",
     """The card frame is made of luminous gold with pearl and ruby inlay. The outer border features golden Japanese cloud patterns (kumomon) flowing continuously around the perimeter. The corners have golden phoenix (houou) ornaments. The top center has a golden eight-way tomoe symbol. The frame has a heavenly Takamagahara (Japanese celestial realm) aesthetic with shimmering golden light. The color palette is brilliant gold, pearl white, and ruby red accents."""),

    ("Japanese_Torii_Gate_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple torii gate border design",
     "A rectangular text box below the artwork with a wooden-textured frame and shimenawa rope border accent",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), simple wooden carved circles",
     """The card frame is made of natural wood with vermilion paint accents. The outer border features simplified torii gate silhouette patterns in vermilion red. The corners have small shimenawa (sacred rope) decorations. The frame has a serene Japanese shrine aesthetic with natural wood grain and vermilion paint. The color palette is vermilion red, natural wood brown, and white paper accents."""),
]

# ============================================================
# MESOPOTAMIAN MYTHOLOGY FRAMES (4 styles)
# ============================================================
mesopotamian_frames = [
    ("Mesopotamian_Lapis_Gold_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with gold and lapis lazuli border panels",
     "A rectangular text box below the artwork with a golden cuneiform-patterned inner frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as golden cylinder seal emblems",
     """The card frame is made of solid gold with deep blue lapis lazuli and red carnelian inlay. The outer border features continuous cuneiform wedge-shaped inscriptions in gold on a lapis background. The corners have golden winged disk (Ashur symbol) ornaments. The top center has a stylized star of Ishtar motif in lapis and gold. The frame has an ancient Mesopotamian palace wall aesthetic with rich royal burial quality like the Royal Tombs of Ur. The color palette is brilliant gold, deep blue lapis lazuli, and red carnelian accents."""),

    ("Mesopotamian_Bronze_Ziggurat_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with bronze stepped border design like a ziggurat",
     "A rectangular text box below the artwork with a bronze-textured inner frame and cuneiform accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as bronze disc emblems",
     """The card frame is made of polished bronze with glazed brick inlay. The outer border features stepped ziggurat tier patterns ascending toward the top. The corners have bronze bull-lion hybrid (lamassu) head ornaments. The frame has an ancient Babylonian temple aesthetic with metallic bronze texture and colorful glazed brick details. The color palette is bronze, blue-green glazed brick, and gold accents."""),

    ("Mesopotamian_Creation_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with cosmic golden border design",
     "A rectangular text box below the artwork with a glowing golden inner frame and celestial cuneiform patterns",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden cosmic energy",
     """The card frame is made of luminous gold with multi-colored gem inlay. The outer border features golden cuneiform symbols representing the Enuma Elish creation story arranged in a continuous band. The corners have golden primordial god (Anu, Enlil, Enki, Ea) symbol ornaments. The top center has a golden cosmic mountain motif. The frame has a divine Mesopotamian creation myth aesthetic with rich gold and gemstone colors. The color palette is brilliant gold, deep blue, emerald green, and ruby red accents."""),

    ("Mesopotamian_Clay_Tablet_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with clay tablet border design",
     "A rectangular text box below the artwork with a clay-textured frame and cuneiform impressions",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), impressed into clay surface",
     """The card frame is made of light brown clay with cuneiform impressions. The outer border features wedge-shaped cuneiform symbols pressed into the clay surface in a continuous band. The corners have basic geometric impressed patterns. The frame has an ancient Sumerian clay tablet aesthetic with natural clay texture and weathering. The color palette is warm tan clay, dark brown cuneiform impressions, and pale gold accents."""),
]

# ============================================================
# HINDU MYTHOLOGY FRAMES (4 styles)
# ============================================================
hindu_frames = [
    ("Hindu_Cosmic_Gold_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with ornate gold and multi-gem border panels",
     "A rectangular text box below the artwork with a golden mandala-patterned inner frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as golden lotus disc emblems",
     """The card frame is made of brilliant gold with ruby, sapphire, emerald, and diamond inlay. The outer border features an intricate golden mandala pattern with concentric geometric and floral designs. The corners have golden lotus flower ornaments in full bloom. The top center has a golden Om (Aum) symbol surrounded by a lotus halo. The frame has a divine Hindu cosmic aesthetic with rich gold and multi-colored gemstone work inspired by South Indian temple jewelry. The color palette is brilliant gold, ruby red, sapphire blue, and emerald green accents."""),

    ("Hindu_Temple_Stone_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with carved stone temple border design",
     "A rectangular text box below the artwork with a stone-textured inner frame and painted deity motifs",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), carved into stone surface",
     """The card frame is made of polished sandstone with colorful paint accents. The outer border features carved Hindu deity figures and celestial beings (apsaras, gandharvas) in stone relief. The corners have carved lotus and kalasha (holy pot) ornaments. The frame has a South Indian Dravidian temple gopuram aesthetic with detailed stone carving and vibrant paint. The color palette is warm sandstone, colorful temple paint (red, green, gold), and dark stone shadows."""),

    ("Hindu_Cosmic_Dance_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with cosmic fire ring border design",
     "A rectangular text box below the artwork with a glowing golden inner frame and cosmic mandala patterns",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by cosmic fire energy",
     """The card frame is made of golden metal with a ring of stylized cosmic fire surrounding the entire border. The outer border features Nataraja (cosmic dance) pose silhouettes in gold at regular intervals. The corners have golden elemental symbols (fire, water, earth, air). The top center has a golden third eye motif. The frame has a divine Shiva Tandava cosmic dance aesthetic with dynamic fire and energy effects. The color palette is golden fire, deep blue cosmic background, and orange flame accents."""),

    ("Hindu_Palm_Leaf_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with palm leaf manuscript border design",
     "A rectangular text box below the artwork with a palm-leaf-textured frame and painted miniature motifs",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), simple carved wood circles",
     """The card frame is made of dried palm leaf material with painted borders. The outer border features traditional Hindu miniature painting motifs (flowers, peacocks, elephants) in natural pigments. The corners have simple painted lotus motifs. The frame has an ancient Indian palm leaf manuscript (Ollekhuta) aesthetic with natural fiber texture. The color palette is tan palm leaf, natural pigment colors (indigo, ochre, green), and gold paint accents."""),
]

# ============================================================
# AZTEC/MAYAN MYTHOLOGY FRAMES (4 styles)
# ============================================================
aztec_frames = [
    ("Aztec_Jade_Gold_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with gold and jade border panels",
     "A rectangular text box below the artwork with a golden Aztec calendar-patterned inner frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as jade and gold disc emblems",
     """The card frame is made of solid gold with brilliant green jade inlay. The outer border features the Aztec sun stone calendar face motifs repeated around the perimeter in gold relief. The corners have golden eagle warrior helmet ornaments. The top center has a golden sun disk with Aztec day sign symbols. The frame has a rich Tenochtitlan temple aesthetic with gold and jade work inspired by Moctezuma's treasure. The color palette is brilliant gold, vivid green jade, and turquoise accents."""),

    ("Aztec_Jaguar_Warrior_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with jaguar-pelt and obsidian border panels",
     "A rectangular text box below the artwork with a dark jaguar-pelt-textured inner frame and obsidian blade accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as obsidian mirror discs",
     """The card frame is made of dark material with jaguar pelt texture and obsidian blade fittings. The outer border features repeating Aztec jaguar warrior helmet motifs in gold. The corners have obsidian mirror ornaments (used for divination). The frame has a fierce Aztec military aesthetic with dark tones and sharp obsidian edges. The color palette is dark brown/black jaguar pelt, gold fittings, and obsidian grey accents."""),

    ("Aztec_Calendar_Sun_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with Aztec sun stone border design",
     "A rectangular text box below the artwork with a golden calendar-patterned inner frame and Aztec day sign accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden calendar energy",
     """The card frame is made of gold and stone with the Aztec sun stone (Piedra del Sol) as the central design element. The outer border features the four previous sun/eras (Nahui-Ollin, Nahui-Ehecatl, Nahui-Tleya, Nahia-Atl) carved in stone relief. The corners have golden Aztec day sign symbols (Calli, Tochtli, Acatl, Ozomatli). The top center has the face of Tonatiuh (Aztec sun god) in gold. The frame has a monumental Aztec calendar aesthetic with rich stone and gold work. The color palette is gold, grey stone, red paint accents, and jade green."""),

    ("Aztec_Stone_Temple_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple stone temple border design",
     "A rectangular text box below the artwork with a stone-textured frame and carved Aztec serpent motifs",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), carved into stone surface",
     """The card frame is made of grey volcanic stone (tezontle) with minimal decoration. The outer border features simplified Aztec serpent (coatl) motifs carved into the stone surface. The corners have basic geometric stepped fret patterns. The frame has an ancient Aztec temple wall aesthetic with natural volcanic stone texture. The color palette is grey/red volcanic stone, dark brown shadows, and pale gold accents."""),
]

# ============================================================
# OTHER MYTHOLOGIES FRAMES (4 styles each)
# ============================================================

# African (Akan/Anansi)
african_frames = [
    ("African_Gold_Kente_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with vibrant Kente cloth pattern border panels",
     "A rectangular text box below the artwork with a golden Adinkra-patterned inner frame",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as golden Adinkra symbol discs",
     """The card frame is made of rich gold with vibrant Kente cloth pattern inlay. The outer border features traditional Akan Kente cloth geometric patterns in bright colors (gold, red, green, blue, black) woven into the design. The corners have golden Adinkra symbols (Gye Nyame, Sankofa). The top center has a golden Akan goldweight ornament. The frame has a rich West African royal aesthetic with vibrant textile patterns and gold work. The color palette is brilliant gold, Kente cloth colors (red, green, blue, yellow), and deep brown accents."""),

    ("African_Wood_Carving_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with carved wood border design",
     "A rectangular text box below the artwork with a dark wood-textured inner frame and carved pattern accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), carved into wood surface",
     """The card frame is made of dark polished African hardwood with carved motifs. The outer border features traditional African mask and figure carving patterns in relief. The corners have stylized animal head carvings (antelope, lion, elephant). The frame has a West African wooden sculpture aesthetic with natural wood grain and dark patina. The color palette is dark hardwood brown, natural wax sheen, and earth tone paint accents."""),

    ("African_Sahel_Gold_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with golden Sahelian border design",
     "A rectangular text box below the artwork with a glowing golden inner frame and African geometric patterns",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by golden energy",
     """The card frame is made of luminous gold with terracotta and bead inlay. The outer border features golden West African geometric patterns inspired by Ashanti gold weights (abrammuo). The corners have golden African spirit figure ornaments. The top center has a golden sun and moon motif. The frame has a majestic Mali Empire aesthetic with rich gold trade route quality. The color palette is brilliant gold, terracotta orange, and deep indigo accents."""),

    ("African_Beaded_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with beaded border design",
     "A rectangular text box below the artwork with a woven-texture inner frame and bead pattern accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as beaded circles",
     """The card frame is made of woven material with colorful beadwork border. The outer border features traditional African beadwork patterns in geometric sequences (Zulu or Maasai inspired). The corners have small beaded flower ornaments. The frame has a traditional African craft aesthetic with colorful beadwork and natural fiber texture. The color palette is multicolored beads (red, blue, green, yellow, white), natural fiber brown, and gold bead accents."""),
]

# Native American
native_american_frames = [
    ("NativeAmerican_Turquoise_Silver_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with silver and turquoise border panels",
     "A rectangular text box below the artwork with a silver-stamped inner frame and Navajo pattern accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as turquoise and silver disc emblems",
     """The card frame is made of polished sterling silver with large turquoise stone inlay. The outer border features traditional Navajo squash blossom and concha belt patterns in silver relief. The corners have turquoise stone ornaments with silver backing. The top center has a golden sun and eagle motif in silver and turquoise. The frame has a Southwestern Native American jewelry aesthetic with high-quality silversmithing and gemstone work. The color palette is bright silver, vivid turquoise blue-green, and deep red coral accents."""),

    ("NativeAmerican_Basket_Woven_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with woven basket border design",
     "A rectangular text box below the artwork with a woven-texture inner frame and natural dye pattern accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as woven circles",
     """The card frame is made of tightly woven natural fibers with dyed pattern accents. The outer border features traditional Native American basket weave patterns in natural and plant-dyed colors. The corners have woven geometric corner ornaments. The frame has a Southwestern basketry aesthetic with natural fiber texture and earth tone colors. The color palette is natural tan fiber, plant-dyed red, black, and cream accents."""),

    ("NativeAmerican_Totem_Cedar_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with Pacific Northwest formline border design",
     "A rectangular text box below the artwork with a carved-wood inner frame and formline painting accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by carved totem energy",
     """The card frame is made of red cedar wood with black and red formline painting. The outer border features Pacific Northwest Coast Native American formline design (ovoids, U-shapes, and flowing lines) painted in black and red. The corners have carved thunderbird and orca ornaments. The top center has a golden eagle motif in formline style. The frame has a Pacific Northwest totem pole aesthetic with rich wood grain and bold painted designs. The color palette is red cedar brown, black formline paint, and vermilion red accents."""),

    ("NativeAmerican_Featured_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple leather and feather border design",
     "A rectangular text box below the artwork with a leather-textured frame and quillwork accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), simple carved wood circles",
     """The card frame is made of tanned leather with quillwork border. The outer border features traditional porcupine quillwork geometric patterns in natural dyed colors. The corners have small feather ornaments tied with sinew. The frame has a Plains Native American craft aesthetic with natural leather texture and quillwork detail. The color palette is tan leather, natural quill colors (red, yellow, blue, black), and white bone accents."""),
]

# Inuit
inuit_frames = [
    ("Inuit_Serpentone_Caribou_Legendary", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with serpentine stone and caribou horn border panels",
     "A rectangular text box below the artwork with a stone-carved inner frame and bone inlay accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as carved stone discs",
     """The card frame is made of dark green serpentine stone with caribou horn and bone inlay. The outer border features traditional Inuit soapstone carving motifs (ringed seal, polar bear, caribou) in low relief. The corners have carved bone ornaments shaped like traditional Inuit knife handles. The top center has a golden northern lights (aurora borealis) motif in enamel. The frame has an Arctic Inuit stone sculpture aesthetic with smooth polished stone and natural horn texture. The color palette is dark green serpentine, white bone, and deep blue enamel accents."""),

    ("Inuit_Ivory_Arctic_Uncommon", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with ivory and leather border design",
     "A rectangular text box below the artwork with an ivory-textured inner frame and leather strap accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), styled as ivory carvings",
     """The card frame is made of polished walrus ivory with dark leather wrapping. The outer border features carved Inuit animal figures (seal, whale, polar bear) in continuous relief. The corners have small bone toggle ornaments. The frame has a traditional Inuit ivory carving aesthetic with smooth warm ivory surface and leather accents. The color palette is warm ivory white, dark brown leather, and blue stone bead accents."""),

    ("Inuit_Aurora_Boreal_Rare", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with northern lights energy border design",
     "A rectangular text box below the artwork with a glowing aurora inner frame and Inuit silhouette accents",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), surrounded by aurora energy",
     """The card frame is made of dark stone with colorful northern lights enamel inlay. The outer border features the colors of the aurora borealis (green, blue, purple, pink) flowing like liquid light around the perimeter. The corners have carved Inuit spirit figure ornaments in bone. The top center has a golden Inuit moon spirit (Sila) motif. The frame has an Arctic night sky aesthetic with shimmering aurora light effects. The color palette is dark stone, aurora green/blue/purple enamel, and bone white accents."""),

    ("Inuit_Soapstone_Common", "Positioned at the top-right corner of the card",
     "A large rectangular artwork slot positioned in the upper-middle section of the card, with simple soapstone border design",
     "A rectangular text box below the artwork with a soapstone-textured frame and carved animal motifs",
     "A horizontal stats bar at the bottom with two circular slots for Attack (left) and Health (right), carved into soapstone",
     """The card frame is made of soft grey-green soapstone with minimal carving. The outer border features simplified Inuit animal silhouettes (ringed seal, bird) carved into the stone surface. The corners have basic geometric patterns. The frame has a traditional Inuit soapstone carving aesthetic with smooth stone texture. The color palette is grey-green soapstone, dark carved shadows, and pale bone accents."""),
]

# ============================================================
# GENERATE ALL TEMPLATE FILES
# ============================================================

all_templates = []

for myth_name, frames in [
    ("Greek", greek_frames),
    ("Egyptian", egyptian_frames),
    ("Chinese", chinese_frames),
    ("Norse", norse_frames),
    ("Celtic", celtic_frames),
    ("Japanese", japanese_frames),
    ("Mesopotamian", mesopotamian_frames),
    ("Hindu", hindu_frames),
    ("Aztec", aztec_frames),
    ("African", african_frames),
    ("NativeAmerican", native_american_frames),
    ("Inuit", inuit_frames),
]:
    for frame_data in frames:
        all_templates.append((myth_name, frame_data))

# Write all template files
count = 0
for myth_name, (name, mana_pos, artwork_desc, text_box_desc, stats_desc, frame_style) in all_templates:
    content = make_frame_template(name, mana_pos, artwork_desc, text_box_desc, stats_desc, frame_style)
    filepath = os.path.join(OUTPUT_DIR, f"{name}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Successfully generated {count} card frame template files in '{OUTPUT_DIR}/'")
print()

# Print summary by category
from collections import Counter
categories = Counter(t[0] for t in all_templates)
print("Templates by category:")
for cat, cnt in sorted(categories.items()):
    print(f"  {cat}: {cnt} templates")