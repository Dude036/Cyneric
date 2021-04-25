#!/usr/bin/python
# coding: utf-8
Trinkets = [
    'A miniature, tame mimic',
    'A carved marble elephant',
    'A small round cactus with two eyes',
    'A pocket book of dwarven poetry',
    'A bronze box containing a tiny wooden owl',
    'A solid blue metal sphere, one inch in diameter, with three parallel grooves around the circumference',
    'A pouch containing ten dried peas',
    'A ceramic puzzle cube, with each face divided into four independently rotating squares enameled with astronomical signs',
    'A square of bear-beetle leather, a creature unique to the misty woods of Cix',
    'A sheet of vellum on which is crudely painted a herbal plant that you have yet to identify',
    'A petrified frog',
    'A twenty-sided die',
    'A cut yellow chrysanthemum that never dies',
    'A palm-sized iron cage: the door doesn\'t shut properly, as the tiny lock was broken from the inside',
    'A blob of grey goo, slippy but safe to touch, kept in a ceramic pot',
    'A dried sky lily, from the tip of the Godshead, an impossibly high mountain',
    'A glowing blue-green line, six inches long, but with no discernible radius',
    'A pretty conch shell',
    'A scrap of paper on which is written, in Goblin, "My dearest Bess,"',
    'A keychain holding the head of a broken key',
    'An echo pearl from the depths of the Vibration Lake',
    'A toy crossbow',
    'Lip balm',
    'A fossil of an extinct many-limbed critter',
    'A brass prosthetic nose',
    'A corkscrew',
    'A dried poison gland of a jaggedfish',
    'A bronze gear on which is etched the word "Moon"',
    'A map of a labyrinth, on which is penciled a line that starts at the centre but fails to connect to the entrance',
    'A cube of ice that never melts',
    'A square of ironsilk sewn by the geargrubs of ancient Siclari',
    'An ivory knitting needle',
    'A peacock feather',
    'A travel set of paints: someone has used up all the black',
    'A wig of short platinum-blonde hair',
    'A child\'s charm bracelet',
    'A small bar of orichalcum, a metal only mentioned in ancient literature',
    'A deed to a ruined tower',
    'An invitation to a formal ball to be held in two years time',
    'A smoking pipe carved from granite',
    'A vial of scented oil',
    'A preserved basilisk eye',
    'A torn page on which is written "Death! / Plop / The barges down in the river flop / Flop, plop / Above, beneath"',
    'An intricate knot that nobody seems to know how to tie or untie – sailors believe it to be bad luck',
    'Pages ripped out of an accounting journal of a local merchant',
    'A ring with a poison reservoir for slipping into drinks and a tiny razor edge for cutting purse-strings',
    'A glass globe of swirling green goop, no openings',
    'A bundle of ragged "treasure maps" drawn by inventive local children',
    'A sliver from a spear said to have pierced the armpit of a saint',
    'A portfolio of pressed flowers',
    'A small handbook of foreign coins, for travelers to identify denominations',
    'A slightly out of date guidebook to foreign inns, taverns, and transportation',
    'Six useless wooden tokens previously issued by a traitor-prince as currency',
    'Two false fingernails painted with mysterious symbols',
    'A set of cosmetic tools for cleaning the ears',
    'A harmless stage dagger with retracting blade and blood-compartment',
    'A floating glass orb that follows you around and makes whirring sounds',
    'A goblin-made key that can lock any door, but unlock none',
    'A translucent coin, minted in an unknown land',
    'A bronze ring engraved with dark symbols that was supposedly buried with a legendary necromancer long ago',
    'A ring carved with the unfinished insignia to a defunct secret organization',
    'A thimble on which is an enamel painting of a turtle',
    'A puzzle box holding 10 fingernail clippings',
    'A pair of badly worn hairdressing scissors',
    'A wax hand shaped to hold a large cup',
    'A measuring tape, marked in ink at 23 inches',
    'A seashell that is silent when held up to your ear',
    'A coprolite',
    'One piece of unknown paper currency with no obvious denomination',
    'A bootlace entwined with gold thread',
    'A dented sheriff\'s badge',
    'A tiny bubble level that is calibrated incorrectly',
    'A belt buckle',
    'A letter of complaint to a toy shop owner',
    'A decorative leather stud',
    'A penny whistle that plays the same note no matter which holes are covered',
    'A ticket admitting an adult and child onto a thing called a "semiotic tram"',
    'A small glass vial holding three eyelashes',
    'A tub of putty',
    'A leather shoe made for a dog',
    'A doll head with no hair and poorly applied makeup',
    'A pewter spork',
    'Illustrated instructions on how to make a paper hat',
    'A clear glass dish with four round notches around the outside edge',
    'A wire circlet that bestows upon its wearer perfect posture',
    'A small hand-sized box covered with numbered buttons',
    'An empty whiskey tumbler that causes any liquid poured into it to become bourbon',
    'A book of flumph grammar',
    'A hunk of metal which appears to be several gears jammed together at unnatural and impossible angles: attempting to turn it causes it to emit a horrible shrieking sound',
    'A crystal prism that refracts shadow instead of light',
    'A smokeless and odorless candle',
    'A flat disc of layered metal and prismatic glass with a hole in the centre',
    'An ornate pewter tankard made without a bottom',
    'A wooden device designed to be gripped in two hands; two levers protrude from the top, and two triggers from the underside',
    'Two perfectly identical pine cones',
    'A sponge that can absorb 60 gallons of ale (and only ale)',
    'A pepper grinder containing an unlimited supply of pepper unless opened, at which point it becomes half empty',
    'A poorly cultivated bonsai juniper in a glazed ceramic pot',
    'An oval-shaped soapstone tablet inscribed with a short list of religious prohibitions',
    'A wooden doll with a door that opens to reveal a slightly smaller, identical, doll; this one is empty, perhaps there are still smaller dolls that are missing?',
    'A stone figure of a snake that changes positions after every full moon',
    'A silver key of unknown origins on a leather cord as a pendant that emits strange magical energy',
    'The right half of a broken bronze circlet with a light leafy pattern that when placed on your head, stays in place as though the other half was still there',
    'A small silver rod which when rolled between your hands emits sounds as though a lute were being played by a master softly nearby',
    'A music box that can only be heard by someone who as wound it at least once',
    'A small stone cube that, when tapped with a rod of metal, looks as though it were made of that metal for a few seconds',
    'A wooden sphere with a white marking that always faces the sun, and a black marking that always faces the moon',
    'An opaque jar that cannot be opened or broken, no matter how hard you try',
    'A journal that details the great adventures of a hero you have never heard of, complete with vivid descriptions of nonsensical creatures and terms, all written in messy handwriting, but with impressive diction',
    'A tiny sack that, when opened, is full of sand, but feels as heavy as a large stone when lifted',
    'A puppet in the likeness of someone you distantly know, that echoes your movements when you (and only you) place it on the ground',
    'An iron rod that bends in unusual ways when you look directly at it, but rights itself when you look away',
    'A book that perfectly records the holder\'s dreams when held while sleeping',
    'A tin pot that is just the right size for you to wear as a helmet',
    'A marble sculpture of a tiny elf holding a lute seated on a chair that plays music every so often',
    'A piece of pure white cloth that never gets dirty',
    'A hat that never gets wet',
    'A mask that copies its wearer\'s facial expressions',
    'A humanoid skull with ethereal green orbs in its eye sockets',
    'A wineskin that only holds wine Any other liquid pours out after a few seconds',
    'A leather belt that, when worn, glows with faint blue light',
    'A tiny javelin with an ornately carved shaft that always returns when thrown, exactly halfway between you and the person closest to you',
    'A sphere of crystal with a tiny shard of obsidian at the exact centre',
    'A flask that freezes any liquids stored in it at midnight, and unfreezes them at noon',
    'A book with words that change every time it is read',
    'A chain that feels warm when its holder is standing directly beside an awakened tree',
    'A cube with tiny animals wandering on each face that change when they cross onto a different face',
    'The preserved hand of a famous noble that moves when pointed at the ground',
    'A terribly written novel whose plot seems to match events that have happened in your life',
    'A recount of a famous battle that contradicts what is commonly thought about that battle, written by a great sage who was present',
    'A crown made out of ice that never melts',
    'A piece of string that always emits smoke',
    'A rod of indeterminate metal that changes its length at random every other day',
    'The hilt of a dagger that was used to assassinate a king, with an onyx on the end that glows ominously on nights with a full moon',
    'A stone carved to look like a head that occasionally speaks, asking questions that change every time',
    'A stick that glows brightly when held by an undead creature',
    'A flute that, when played, makes the sound of a random instrument, though never a flute',
    'An invitation to an event that has already ended',
    'A copper ring that feels abnormally light',
    'A turban that, when worn, makes your steps feel very light',
    'A cube of glass with mysterious runes etched on each corner',
    'A towel with a set of instructions embroidered on it that clearly state to wear it on the head in case of mind flayer attack',
    'A rose that, when placed in a bouquet with exactly 5 other flowers, glows brightly, and seems to move',
    'A set of brass wind chimes that only chime when hung on a rod of precious metal',
    'A grotesque statuette of a humanoid with rat-like features',
    'A drawing of a spider with twelve legs being used as a mount by a crudely drawn hobgoblin without a head, with a set of poems on the back written in poor Common',
    'The badge of a powerful organisation, with writing etched on the back that defames that group',
    'The diary of a prison guard with half of the pages written in a different language',
    'A handbook of etiquette for nobles of an empire that fell',
    'A translation guide for a fictional language',
    'The head of a pickaxe that was used in a lost gold mine, with names carved in Dwarvish runes along the sides',
    'A wooden plank that refuses to burn',
    'A detailed guide on the anatomy of rocs',
    'A muddy book with a single phrase repeated over and over',
    'A surprisingly realistic replica of a rakshasa hand',
    'A stone rod with a tin coating that has worn through in several places',
    'A compass that points towards the nearest bottle of rum',
    'A stone that feels very heavy, yet floats effortlessly',
    'A map with no key or locations, only red circles with lines connecting them',
    'A shard of glass that floats a tiny distance off of the ground when near an open flame',
    'A diagram of a forest on an island with no named artist',
    'An orb that glows with a flash of green light at noon',
    'A locket with a strange rune carved inside',
    'A green coat with numerous pockets, each with a separate piece of a moustache trimming kit inside',
    'A silver plate that feels rough, though it were made from coarse stone, but never feels painful to touch',
    'A figurine of a fiend, so lifelike it seems like it might come to life and attack any second',
    'A sapling that cannot be placed into soil, but never dies and has a single sweet fruit on its branches that grows back after one day when picked',
    'A red coat that makes you feel colder when it is worn',
    'A vial of tree sap',
    'A rod of metal that produces tiny sparks from a red marking when a black button on the other end is pressed',
    'A wooden cane that, when placed on the ground, stands perfectly straight, and cannot be tipped over',
    'A bottle of red liquid that sparkles ever so slightly under direct moonlight, with a faded blue label that cannot be read',
    'A sack of shed dragon claws',
    'A feather with a piece of red string tied on the end of the shaft',
    'An engagement ring that belonged to one of your parents',
    'A book that you faintly remember from your childhood that you thought was lost for many years',
    'An odd stone that seems to permeate energy',
    'A sword sized for a child',
    'A vial of water from a hot spring',
    'A squat metal tin full of brown powder that always feels cold to the touch, regardless of the temperature',
    'A glove worn by someone you deeply admire',
    'A shard of crystal that glows when near places dedicated to a certain deity, and glows brighter the closer you are',
    'A tome from an abandoned library',
    'A gear that refuses to mesh with any other',
    'A box of nuts that feel like they are made from metal, but can be eaten as though they were normal',
    'A tree branch with an odd symbol',
    'A yew wood figurine of a satyr with wings, carrying a willow wood staff',
    'A suit of armour made from oak wood, sized for a doll, painted in vivid red and black',
    'A stone with odd indentations, that seem to spell out a message of some kind',
    'A vial of mysterious pale blue liquid that slithers back in when poured out, and has a pleasant floral scent',
    'A jug that turns liquids stored in it into milk after a few minutes',
    'A seed that never grows when planted, but looks very similar to an acorn with a few green lumps',
    'A waxy white flower that constantly moves as though a gust of wind were blowing it around',
    'A robe with a tag on the inside that reads "to my dearest pupil," given to you by someone you deeply respect',
    'A tome filled with cryptic writings, all in Common, but with confusing terminology',
    'A beige jar of red ointment without a label',
    'A famous calligrapher\'s personal brush',
    'A band of iron that shines brilliantly despite being completely rusted',
    'A small cylinder of stone that smells faintly of blood',
    'A tunic that smells of saltwater and bears the emblem of an established land-locked nation on the front',
    'A curious looking pair of goggles with the words "Property of Ice! DON\'T TOUCH!" scrawled into the side',
    'A small blue cube that faintly glows for some unknown reason',
    'A small orb with water and a small living jellyfish inside',
    'A cat figurine',
    'A hat that has a secret space on the inside which is the size of a small pouch and very hard to locate',
    'A bar of scented soap that bubbles',
    'A book of lore, that is hollow inside',
    'A belt buckle stolen from a noble or a king',
    'A slip of parchment with the phrase "I am not dead" written on it',
    'A small fist-sized cube that occasionally makes strange noises',
    'An unusually sharp spoon',
    'The symbol of a powerful religion, covered in soot that stays no matter how much it is cleaned',
    'The diary of a philanderer that contains detailed descriptions of common monsters',
    'A gigantic snake\'s tooth that has an unsettling aura about it',
    'An unusually small humanoid skull',
    'A bit of rock from a headstone',
    'A tiny bag of yellowish powder',
    'A small indestructible talking skull that tends to mumble racist slurs whenever it sees an elf',
    'A box of black licorice',
    'A strangely shaped bone',
    'An iron ring that, when worn, makes the wearer feel calm',
    'A group of small glassy spheres, all attached to each other in such a way that they form a rough pyramidal shape',
    'An empty bottle that once held the blood of a demon',
    'A tiny glass vial that contains a portion of the ashes of a statue of a god that was destroyed by marauders',
    'A detailed guide to making pickled foods',
    'A mask in the shape of a lion\'s head that moves from side to side occasionally when worn, yet the wearer experiences no change',
    'An axehead that appears to have been snapped off',
    'A palm-sized greenish stone with the carved image of a dragon on one side, and a humanoid on the other',
    'The head of a mummy',
    'A flask of giant\'s blood',
    'A miniature shield',
    'A sea shell with a strange rune carved into it',
    'A corn husk doll which dances under its own power when music is played nearby',
    'An arm band in the shape of a snake, with emeralds for eyes',
    'A tiny, fossilized ammonite made into a necklace',
    'An old coin, showing a hare on one side and the moon on the reverse',
    'The banner of a noble house',
    'A bird carved out of lapis lazuli',
    'A small pouch filled with the teeth of various shark species',
    'A tiny painting showing a vulture carrying a bone in its beak',
    'A fist-sized stone that glows slightly and feels incredibly hot to the touch',
    'An ingot of copper with an unusual hue',
    'A small notebook full of drawings',
    'A fist sized turtle shell',
    'A drawing of a flower that looks different when viewed from an angle',
    'A perfectly flat wheel made from terracotta',
    'The journal of a philosopher, full of wise sayings and anecdotes',
    'A malevolent-looking raven skull that has been charred black',
    'A small glass case containing several glossy butterfly wings',
    'A preserved frog that moves and croaks like a living frog, but to even an untrained eye is undeniably deceased',
    'A mahogany box of religious scrolls',
    'A guide to changing bowstrings full of grammatical errors',
    'A ceramic troll statuette with no arms, just legs',
    'A glass bottle that shines like gold',
    'An iron door-handle that makes menacing noises when underground',
    'A sliver ring that feels very slippery',
    'An ornately carved figurine of a giant made from bone',
    'A rusted fork',
    'A shoe made from crystal',
    'A piece of tree bark that is coated in blood',
    'A small oak wood box of vibrantly-coloured powders, each colour in its own tiny drawer',
    'A silver hand mirror with a dragon etched onto the back',
    'A tine of a deer\'s antler',
    'A miniature teapot and teacup',
    'A bejeweled statuette of a knight that is a replica of a famous sculpture',
    'A box of small orange cylinders that break and burn easily',
    'A stone carving of a piece of bacon',
    'A horn that has been cut cleanly in half',
    'A thin tube of iron filings with the seal of a noble house on both ends',
    'A small clay pig toy',
    'A small metal can that contains black colored pudding If touched, the pudding leaves a slight stinging sensation to the hand',
    'A necklace strung with tiny snail shells',
    'Half of a coin with unusual markings engraved on both sides that cut off where the other half would connect',
    'A sack full of pieces of half-eaten bread',
    'A small bottle labeled "otyugh perfume" that really stinks',
    'An odd lump of metal that smells like sweat and rotten fish',
    'A fist-sized green seed covered in brown spines',
    'A fist-sized metal frog or toad (your choice)',
    'A glass figurine in the shape of a lobster',
    'A wooden spoon, carved from a bigger spoon',
    'A jeweled goblet that will never, ever spill its contents',
    'An amulet that, when worn, makes you look older when you are injured',
    'A bowl covered in ornate designs depicting hill giants in combat with dwarves',
    'A copper badge that you have never seen before in your life, though it has your name on it',
    'The preserved finger of a giant that you once knew',
    'A set of ceramic castles that have a space for a candle in the middle When the candle is lit the castle looks like it has lights on in the windows',
    'A perfectly reflective ball with a magnetic stick which allows it to be used to look around corners',
    'A laurel of flowers which never wilt or die',
    'A purple amulet in the shape of a pig\'s head',
    'A magically shrunken goblin in a tiny cage',
    'A copper lighter that never runs out of fluid',
    'A fist-sized sphere; half of which is blue while the other half is red',
    'A pair of gloves that seem unusually warm to the touch',
    'A severed ape arm covered in black fur',
    'A vine covered in thorns that writhes around occasionally',
    'A petrified goat skull',
    'A brown mushroom of extraordinary size',
    'A drawing of a bird that you have never seen before',
    'A tiny piece of metal that floats on water',
    'A tiny stone orb that hangs in the air for a bit when you throw it',
    'An iron cuirass far too large to be worn by a humanoid',
    'An extremely large leaf that causes food that it touches to become very bitter',
    'A single leather boot with unknown markings on the bottom',
    'A leather pouch that contains a single wooden token depicting a crab',
    'A belt with a buckle made from an unusually twisted piece of copper',
    'An eyeball carved from stone that occasionally moves around, as though looking for something',
    'A piece of rope that is always too short to be useful',
    'A d8 die that looks to have been split in half by a large axe',
    'A carved wooden statuette of a hawk',
    'A tiny box that contains a model chair',
    'An eerily lifelike wooden bear figurine that is never found where you left it',
    'A small section of a snakeskin belt that seems to slither when it touches the ground',
    'A tiny carved skull with jewels in its eyes You have a feeling like someone is watching you whenever you hold it',
    'A bottle of rum that never runs out',
    'A cloak that always flaps gently, as if pushed by a slight breeze',
    'A split piece of unknown wood, decorated to look as if it once was a piece of a druidic focus',
    'A small mirror in which your reflection remains, crying hideously whenever you look at it',
    'A small rodent\'s heart Still beating',
    'A tiny, tame earth elemental that is afraid of beetles',
    'A book that gives you a headache whenever you try to read it You are still unsure of what knowledge or story it holds',
    'A tankard that is always full of a wretched black fluid If tipped, the fluid runs endlessly',
    'An obsidian dagger that reflects shadow as a monochrome rainbow',
    'An undead fly tied to an invincible foot long piece of thread',
    'A small gem that changes color and detail to any object it touches',
    'A miniature platinum lightning bolt that vibrates and zooms around when a storm is coming',
    'A deck of cards with unknown runes on each card',
    'A creepy idol of a black dragon with red jewels as eyes, whenever someone looks at the idol eyes their eyes flash red',
    'A miniature shield painted with gold designs, when you clutch it you feel slightly more confident',
    'A lava stone carved to look like a flame, it gives off endless heat',
    'A set of golden letters that move around when nothing sees them, creating random words',
    'A vial of red liquid that moves up or down depending on the current danger',
    'Extremely hard to see moon stone fragments that make small laughing noises when you can\'t find them',
    'A piece of taffy that always reappears when you eat it',
    'A large pitcher of liquid that seems to always change flavor',
    'A small marble that randomly changes color',
    'A small crystal that shakes very violently when wet',
    'Some random objects such as bones or stones that always come back together when destroyed',
    'A clear piece of fabric that hovers unless you pull it down',
    'A marble that changes size when you aren\'t looking Sometimes something that is touching it changes size slightly too, but changes back in 10 seconds',
    'A page with unknown runes depicting and ancient spell but unreadable no matter what',
    'A glass eye that spins to look at things other people are looking at',
    'A vial shaped like a cylinder Any liquid put inside gets tainted blue and gains a slight taste like blue raspberry',
    'An expired potion of growth, now only makes you get slightly bigger when you take a sip, tastes like powdered iron for some apparent reason',
    'An expired potion of darkvision, now just makes everything bright when you take a sip, tastes like dry carrots for some apparent reason',
    'Some frog legs made of ivory that bounce around randomly',
    'A bar of titanium that feels squishy and soft to touch',
    'A book with a harmonious story, however whenever you turn the last page it takes you back to the middle of the story so you don\'t know how it ends',
    'A clockwork device that\'s button won\'t press no matter what you do',
    'A lens that reverses the color of things seen through it, black becomes white, cyan becomes orange, red becomes blue, and so on',
    'The blade of a huge axe that feels insanely heavy to any creature smaller than Huge, but creatures that are Huge or larger think it is as light as a feather',
    'A small worm statue that causes any creature that touches it to shrink by 1d4 inches over 1d4 minutes Touching the statue again returns the creature to normal size',
    'A green tonic labeled "growth" If anything drinks it they grow an inch each second for 1d4 minutes, then shrink 1 foot each second until they return to normal size Their equipment changes size too but doesn\'t increase damage',
    'A bloody hand that grips onto things and doesn\'t let go',
    'Some vials of liquid that create moss on anything they touch This moss keeps growing and will eventually cover the whole thing Then the moss withers and flakes off',
    'A packet of mints that cause the eater to change color for 1d6 hours',
    'A set of thieves tools that are bent and broken yet they still work perfectly',
    'A miniature brain made of coral',
    'The branch of a tree that caught fire when you were nearby',
    'A picture that has a field in it, as time goes, the picture changes and adds things like people and houses to itself',
    'The eye of a cat, for some reason it commonly looks around at anything powerful',
    'An acorn that makes ringing noises and shakes violently when touched',
    'A hammer from a long gone blacksmith Sometimes at night you can see the hammer float and pound any weapons nearby',
    'A glass sphere containing ooze, still alive; it sometimes causes green acidic liquid to gush out of the sphere',
    'A crystal dagger, it is engraved with the symbol of a flaming skull with a rune covered ring around it',
    'A wizard'
    's journal, recounting the tales of many arcane experiments',
    'A red gemstone shaped like a heart',
    'A purple gemstone shaped like a cage',
    'A piece of coal vaguely shaped like a head',
    'A pouch full of a fine black substance of unknown origin',
    'A gem that can summon a dim orb of light that does nothing but follow the summoner for a while',
    'A ceramic tile with a silvery sheen',
    'An incredibly heavy bone with countless words inscribed into it',
    'A small jar that has a lid attached to it When the lid is closed, it turns its contents into fresh milk',
    'An incomplete book that adds to itself constantly',
    'A merchant'
    's scale that is covered in blood stains',
    'A hat that drenches the wearer in a viscous orange fluid',
    'A vial of blood from an unknown creature',
    'A child'
    's severed finger, still fresh, and periodically twitching',
    'A small painting of a skeleton in noble'
    's clothes',
    'A ring carved from the sternum of a serial killer'
    's most beloved victim',
    'The hilt of a broken greatsword When held with both hands, blood runs down along the remnants of the blade',
    'The left glove of a well-known murderer You periodically find yourself wearing it',
    'A small jar of sugar that makes all food and drink taste of salmon',
    'A stuffed bear given to you by a child that wouldn'
    't speak',
    'A bundle of differently colored strands of hair',
    'A small box containing bloody teeth and fingernails The box has the word "Mother" inscribed on the top',
    'A tiny hat that makes you feel very confident whilst wearing it',
    'An old piece of parchment reading "Fredrick, Why?"',
    'A rat'
    's skull with a beautiful, yet unidentifiable family crest carved into it',
    'An apple with a single bite taken out of it It does not decay, it tastes terrible, and you can'
    't bring yourself to throw it out',
    'A miniature painted wooden elephant with a single ivory tusk, the other one is snapped off with a jagged break',
    'A magical tome When the spells inside are cast, the effect is never the same, are extremely stupid, and the spells cast aren'
    't what'
    's written in the tome',
    'A piece of frayed rope about a foot long The ends are slightly burned',
    'A war veteran'
    's glass eye',
    'A deformed human infant'
    's skull',
    'A ceramic jar containing rice grains When opened, a foul odor emanates from the jar',
    'A necklace adorned with a wooden medallion depicting a crudely-painted smiling face',
    'A sacrificial dagger that cuts into your palm whenever you grip the hilt',
    'A terrible love novel written by a hack author For whatever reason, you love the story, even though you know it'
    's terrible',
    'A whistle that causes all that hear it to feel incredibly nauseous',
    'An incredibly venomous snake that refuses to bite you, however, it likes to wrap itself around your arm',
    'An ancient hero'
    's heart, bound in linen and kept in a clay jar',
    'A ring which makes the wearer reek of rotting fish',
    'A pair of pants that supposedly belonged to a powerful necromancer',
    'A pewter spoon that was owned by a powerful, fat landlord',
    'A jar containing an alchemical salve that is labeled "Apply to soles once per week" However, the salve has solidified into a waxy mass',
    'A helmet forged to fit the head of a child',
    'A small, black-furred creature that wears a bone-carved mask It\'s kinda cute, but it always follows you, and remains just out of arms\' reach',
    'A crystal prison in which a lich\'s soul is trapped It is damaged, however, and the lich perpetually complains',
    'A small bottle of chalk tablets Unmarked, but scented with the smell of lilacs',
    'A folded paper frog When unfolded, you can read an uplifting message',
    'A bracelet braided from the ligaments of some large creature, with a charm carved from a humanoid tooth',
    'A piece of torn linen cloth worn soft by someone else\'s fingers Up close, you can see marks where embroidery has been picked away',
    'A small glass jar with a gilt-painted image of a minor goddess; empty with a waxy residue at the mouth',
    'A glass file; intended for the care of nails, claws or talons',
    'A string of rough, red beads that smell faintly of cinnamon',
    'A carved bone portrait of a famous pirate; the enamel has worn thin',
    'A small doll Someone thought it would be a good idea to carve its head from an apple; the face is brown, dry and wizened',
    'A wolf-hair paintbrush, perfect for calligraphy, though the binding is coming loose',
    'A walnut-sized terracotta jar containing traces of red makeup',
    'A fist-sized stone sphere that rolls after you when you put it down and walk away',
    'A box of odd beads that bear no resemblance to eyes, yet always seem to watch you',
    'A vial of dragon\'s blood',
    'A wooden cup that, when put to the ear, relays the sounds of a tavern party',
    'A violin that makes the player sound like an expert musician',
    'A book with a mysterious bloody stain on the back cover',
    'A waterskin that turns anything inside it into fresh, clean water',
    'A life-sized statue of a gnome',
    'A perfectly round snowball that never melts',
    'A broken table knife that can only be held by red-haired humanoids',
    'A 1-centimeter long perfectly functional crossbow',
    'A crystal pen that will only write with green ink',
    'A pair of silk trousers that are always a tad too big',
    'A small coin purse with gold inside that cannot be removed',
    'A wanted poster that bears the face of a terrified elf',
    'A bright orange, ceramic throwing star that will always miss its target',
    'A white metal goblet that grumbles angrily in Dwarvish when filled',
    'A set of blue marble earrings that glow faintly in the presence of pork',
    'A small humanoid skull that cackles every morning at the break of dawn',
    'A pair of scissors that only cuts eyebrow hair',
    'A silver coin with an engraved human that continuously waves to the holder',
    'A cast iron pot with a love letter carved into the side',
    'A bag that is full of rainbow-coloured sand',
    'A leaf that will never blow away in the wind',
    'A single iron shackle that was once worn by a deaf musician',
    'A shirt button that changes shape every day',
    'A single leather shoe that can be worn on either foot',
    'A tiny oak barrel filled with even tinier apples that refills every full moon',
    'A wooden dagger that\'s shaped to resemble a sacrificial blade',
    'A purple banana that never rots and tastes like saltwater',
    'A short metal chain that doesn\'t make and sound when shaken',
    'A map with directions to an abandoned gnome\'s house',
    'A dragon\'s tooth that perpetually feels wet',
    'A loincloth that\'s far too long',
    'A mahogany dinner plate with the phrase \'POETRY IS DEAD\' carved into the bottom',
    'A small wooden box that contains a single, worn thimble',
    'A fully articulate plate gauntlet made out of unbreakable, unmelting chocolate',
    'A clear glass bottle that can be used as an eyeglass',
    'A child\'s leather vest with a small club logo on the back',
    'A codpiece with the entire Sylvan alphabet written on it',
    'A black feather that somehow weighs 40 pounds',
    'A salmon painting that repels mosquitoes',
    'A pair of socks that tickle the wearer',
    'A rolled-up scroll that displays the holder\'s exact height when opened',
    'A pair of marble chess pieces, black and white, that argue with each other',
    'A bandana that makes the wearer look 10 pounds lighter',
    'A rock that screams in fear when it\'s thrown',
    'A piece of parchment with an ink drawing of a centaur that always points north',
    'A green, metal orb that slowly orbits any obese humanoid it\'s thrown at',
    'A mouthpiece for an unknown musical instrument',
    'A single newt\'s eye in a glass jar',
    'A brass face mask that insults the wearer\'s outfit',
    'A small jar of nails that can only be driven by a glass hammerhead',
    'A closed lute case that incites extreme fear when someone tries to open it',
    'A sword scabbard that\'s full to the brim with tiny wooden swords',
    'A book that details a list of embarrassing childhood moments',
    'A guide to living with a house full of talking objects',
    'A fine, leather pouch that contains exactly 248 stone pebbles',
    'A cookbook that only holds the phrase \'Don\'t cook fairies\' scrawled in blood',
    'A thin sheet of cooking paper that\'s been folded into a swan',
    'A warm winter scarf knitted from skunk fur',
    'A stone slab that floats',
    'A backpack that makes eating sounds when items are put inside',
    'A small unbreakable string that spans 10 feet',
    'A decaying wooden knife inscribed by a child that reads "the ultimate blade of destruction"',
    'A small iron sculpture of a phoenix that fills you with peace due to it containing an aura of protection',
    'A miniature cannon made of glass that when heated release a large amount of smoke',
    'A pair of copper rimmed glasses that contain cracked lenses that slightly enhance your vision in the dark when worn',
    'A gigantic blade when used in combat of any kind it becomes immobile and unable to move at all otherwise it\'s as light as a feather',
    'An old doll you found in an abandoned manor The doll\'s eyes follow you and you usually have nightmares when you sleep near it even when you throw it away it comes right back to you',
    'A cane sword that refuses to be unsheathed unless on a full moon',
    'A black triangular pendant that gives off a rich king purple glow it is said to nullify pain but many believe not',
    'A diary that when shaken reveals a secret that a nearby entity knows although the secrets are almost always useless',
    'The soul of a hero long gone It does nothing except look pretty and follow you incessantly',
    'A strand of hair from a lower goddess',
    'A small wooden box containing a pair of small sentient clay men that wonder around aimlessly they magically return to the box when it is closed',
    'A shovel made from unusual blue metal',
    'A sickly green humanoid bone',
    'A tattered red cloak that patches itself up when its wearer is in a graveyard',
    'An odd cog that spins on its own every so often',
    'A stoppered bottle that contains a harmless undead spider',
    'A small drone carving that depicts a naked goblin scratching his hindquarters',
    'A wooden mask that makes the wearer see the people around them as unnaturally beautiful',
    'A letter addressed to you from a king that has been long dead It was sent recently',
    'A small dull dagger that refuses to sharpen',
    'A rusted coin that absorbs any oil it comes into contact with',
    'A long letter of complaint addressed to a teacher you once had written on it',
    'A glass jar that has about 12 living, miniature frogs inside of it',
    'Some candy that tastes faintly of pineapple, and never seems to go bad',
    'A broken piece of technology from the distant future it seems Nobody can tell the purpose of the device, and nothing seems to repair it',
    'A small doll with a cloak and toy dagger attached On the back of the doll, the letters "TDG" are written',
    'A drinking horn with an odd rune carved on it',
    'A tiny pink bottle that smells of roses when it is empty',
    'A hunting horn that sounds like a trumpet when blown into',
    'An owl feather quill that makes the holder always talk in the third person',
    'A leather glove that talks when worn It uses the wearer\'s fingers and thumb as a mouth',
    'A miniature treasure chest that yells at you to shut it when it\'s opened',
    'A wooden carving of an orc doing a handstand',
    'A metal rod that can\'t conduct electricity',
    'A small twig that doubles as the perfect toothpick, no matter who uses it',
    'A gnome\'s hair brush',
    'A small painting of a horse\'s rear end',
    'A mirror that breaks when someone smiles in it',
    'A cork for an old wine bottle that won\'t fit in any other bottle',
    'A copper coin that, when flipped, tells the flipper a fake fortune',
    'An erotic novel that\'s written backwards',
    'A boomerang that comes back when you least expect it to',
    'A pair of worn leather boots that won\'t move when someone wears them',
    'A small pot of horse glue that says \'NOT FOOD, SERIOUSLY\' on the side',
    'A drinking glass that spits out whatever\'s poured into it It then proceeds to tell off the person who filled it',
    'A spyglass that works backwards',
    'A centuries-old pack of rations that\'s perfectly preserved The food inside tastes like chicken',
    'A bowl of grapes that are harder than stone',
    'A pitcher full of goblin tears',
    'A legal deed for a house that doesn\'t exist',
    'A brass tube that acts as a portal to Mechanus It\'s impossible to put anything inside',
    'A dagger made of folded parchment',
    'A green wine bottle that can\'t break',
    'A tiny skeleton that animates and dances when music is played',
    'A prayer book to a made-up religion',
    'An object that can\'t be accurately described When someone tries to describe it, they\'re at a loss for words',
    'A bell that summons a fox from the nearest unoccupied space It does nothing but stare at the person who rang the bell for exactly three minutes and forty-two seconds, after which it runs off',
    'A box of twelve matching pieces of broccoli',
    'A live beehive full of bees They\'re not happy',
    'A tiny fairy in a jar that tells awful jokes',
    'A journal written by a very racist tiefling',
    'A bar of soap that smells like rotten meat',
    'A key that breaks when it\'s used on a door It doesn\'t open the door',
    'A wheel of blue cheese that\'s been dyed red',
    'A 300-page rulebook for rock-paper-scissors',
    'A tin of makeup that\'s the most absurd color of orange',
    'An apple that tastes like an orange',
    'A large, steel lock without a key',
    'A letter from an unknown sender It reads, \'I told you so!\' and the return address is simply labeled \'Feywild\'',
    'A slice of piping hot cherry pie, but it has no plate or utensils',
    'A carefully detailed drawing of a halfling toe',
    'A ruby that holds the soul of a long-dead evil sorcerer He constantly gives bad advice',
    'A ham and butter sandwich with lettuce, but the bread is made of cotton',
    'A teacup full of live, non-venomous spiders',
    'A costume mask made from a wolf\'s skull and pelt',
    'A backscratcher, downsized for use by gnomes',
    'A tattered blacksmith cap full of red dwarf hair',
    'A small roll of leather that\'s been cured with giant urine',
    'The hollowed-out shell of a large hermit crab',
    'A book full of jokes about dragons',
    'A lute made out of dry grass',
    'A quill that never runs out of ink, but changes its ink color every hour',
    'A repeating crossbow that won\'t fire bolts It will, however, fire toothpicks',
    'A silver piece that glows red when exposed to methane',
    'An iron ring inscribed with your name that perfectly fits your left index finger, and only yours',
    'A treasure map that leads to a beggar\'s dandelion garden',
    'A lovingly crafted travel tankard that makes all manners of drink taste of mead',
    'A small wooden box containing a blood-stained pommel and a detailed account of a judicial duel',
    'A flute in the shape of a skull made out of dead wood that whenever played makes the listeners feel scared',
    'A ring embedded with a topaz containing a soul of a clueless wizard He gives little to no insight into objects of intrigue',
    'A small sword from a figurine it is incredibly sharp and able to cut through steel if given the time, unfortunately, it\'s way too small to use properly',
    'A piece of bark from a fabled tree that never decays nor gets damaged it talks to you in a different language from a roster of 4 languages and it changes the language it speaks daily',
    'A handbook that details all the different creatures from another world though you have never seen nor heard of any of them before or has anyone else',
    'A tattered old hat you received from a beggar that when worn makes people want to avoid the wearer and or hurry past the wearer',
    'A a violin you found clutched in the hand of a dead old man whenever you play it regardless of the tune it makes people incredibly sad',
    'A small stone that feels like silk when you touch it',
    'Half of a medallion that emanates dark power untold by mortals yet something feels missing from it like it\'s missing half of itself',
    'Half of a medallion that emanates a sense of security and warmth yet something feels missing from it like it\'s missing half of itself',
    'A pocket sundial that only works in the moonlight',
    'The deed to an invisible hut — at least, that\'s what the merchant said',
    'A song that cannot be played on any mortal instrument no matter how hard you try',
    'A riddle so tough just the sight of it makes even the most intelligent person frustrated at how hard it is',
    'A a multitool with only one tool in it That tool being a magnifying glass that has the words "try to find the other tools" inscribed on it in Common The magnifying glass itself gives the one using it more insight into what they are looking at through it',
    'A ring that has "C\'est inutile" inscribe on it, for some reason it makes you feel special when you wear it',
    'A wand that when waved over anything that could be considered food makes it taste of mixed berries',
    'A plate made of strange clay whenever something is eaten off it a growling noise is heard from somewhere nearby',
    'Half of a cookie that, when eaten, causes another half of a cookie appears in an empty space nearby',
    'A sandwich bag that has the words "for panzer only" written on it Inside the bag is a sandwich so perfect and mouthwatering but no matter what you are forced away if you try to eat the sandwich or remove it from its bag',
    'A 3-foot cube box that causes bread placed in it for more than one minute to become toasted and buttered on one side',
    'A scroll case full of ash The lid has a tiny iron spike on the top',
    'A woodcutter\'s axe that refuses to cut anything but wood',
    'A small box with a button When pressed a repetitive 30-second tune will play If the button is held down button for 20 seconds, it imprints a new tune',
    'A jar containing two eyeballs peering with innocence at you with a label that reads "Lithians treasure" scribbled in crayon',
    'An eye patch of white stained leather with the word "Skipper" on the inside',
    'A silver ring with "Dax <3 Mariva" inscribed on the inside If you try and wear it, it slips off of your finger almost immediately',
    'A deed to a bear sanctuary in another land',
    'A locket containing a picture of an unrecognizable child',
    'A bracer that is too hot to touch',
    'A freezing cold gauntlet',
    'A map of an infinite labyrinth that is illegible',
    'A book of ideas that will never be used',
    'A miniature functioning siege set',
    'A book of smut',
    'A miniature canoe with what appears to be a dragonborn living on it',
    'A captain\'s hat with the name "sexy captain Alice" on the inside',
    'An unfinished nude drawing of a man with an eye patch',
    'A deflated rubber ball',
    'A pamphlet preaching Nameless The Double Fae Gnome',
    'A crude sketch of a goblin entitled Leanord',
    'A necklace made from seven owl feathers',
    'An unknown ancient relic that was forgotten through time',
    'A half-built sled',
    'A vial containing a small ember',
    'A bubblegum scented sword',
    'A bag of odd mushrooms',
    'A statuette made from a coprolite',
    'A book that details etiquette for acolytes of a major religion',
    'A wand sized for a kobold',
    'A whip crafted from ink-black leather',
    'A hag\'s hairpin',
    'A wrestling belt',
    'A whistle that, when blown, makes you feel certain that there\'s a horse not too far away from you',
    'A pair of undies with bats on them',
    'A crown made out of thirty broken spoons',
    'A cabbage that cannot be eaten',
    'A gold-painted rock',
    'A tiny lizard skull',
    'A pink scabbard that feels lighter than it actually is',
    'A map to your ancestral home',
    'A jester\'s hat',
    'A harlequin mask that makes you feel oddly sad when you wear it',
    'A pair of pumped up kicks',
    'A shooting star contained in a bag',
    'A coupon for a free hug from a king',
    'A tiny hand carved from amber that flies around you and pokes people',
    'A red boomerang that never comes backs to you',
    'A tiny bit of a dragon\'s scale',
    'A deed to a place that you made up',
    'A dented helmet that has an odd swirling design on the back',
    'A book of myths',
    'A cork that has a faint aroma of orange',
    'A mushroom that smells of butterscotch and rots',
    'A scabbard that smells of cheese',
    'A trumpet that plays a mocking tune whenever you fail at something You can\'t get rid of it',
    'A set of very erotic undergarments',
    'A jar full of petrified wasps',
    'A hat that belongs to a violent marauder lord',
    'A noble\'s journal, detailing his love affair with a goblin barmaid',
    'A rusty speculum',
    'A broken lute covered in bloodstains',
    'A portrait of an incredibly muscular man wearing a short dress',
    'A necromancer\'s reanimated pet frog',
    'A platinum piece that merchants seem frightful of',
    'A dagger that can\'t be removed from its sheath',
    'A miser\'s coin purse You just can\'t figure out how to untie the drawstrings',
    'A pebble, delicately carved to resemble a dwarven mine baron',
    'A flip book that depicts a cartoonish spine devil operating a riverboat',
    'A beautifully crafted doll that belonged to a knight named Beirand',
    'An undelivered letter addressed to a lord from the east It simply states "kill you" repeatedly',
    'A child\'s wooden sword, with the names of several children carved into the side It is completely bloodstained',
    'An opium pipe made from beautifully carved jade The name "Lawrence" is inscribed at the bottom',
    'A bit of slime in a jar When the jar is opened, the slime tries its hardest to stay as far into the jar as it can, and something tells you you shouldn\'t touch it',
    'A small bottle full of everlasting fire, when opened the sentient fire leaps onto whoever opened it and acts like a familiar; does not burn the owner, will attack anyone who threatens the owner of the fire',
    'A music box that when opened plays strange music extremely loud',
    'A journal with writing about the mass murder of orphans that lived at a temple, the murderer was never found; the writer seems to want revenge',
    'An explorer\'s journal that goes very in depth of his discoveries while in his own house',
    'A small, sticky substance that is unidentifiable Animals seem to enjoy eating it',
    'A box full of green shirts, dresses, hats, basically anything clothes as long as it\'s green Though, you have discovered a large pea in the corner of the box in the past',
    'A necklace of obviously fake black pearls',
    'Sheet music, with explicit instructions to play it using only sounds made by various animals instead of normal instruments',
    'A blanket that makes anyone sleeping under it snore heavily for one hour, before flying off their body',
    'A drum that makes someone within a 30 foot radius sneeze tremendously on every 7th beat',
    'A book that translates anything you say into any language you wish, however it also adds in several random words, completely changing the meaning of whatever you say',
    'A wise ghost that will give mildly helpful advice on occasion, but thinks its hilarious to play the bongos at inconceivable volume whenever you are trying to remain undetected',
    'An extremely vulgar pocket watch that only shuts up when you wrap it in a special cloth that is fragile and can never be replaced',
    'A lime-green sandal that is sized for a giant',
    'A dung beetle the size of a pony that refuses to do anything but follow you, and push a gigantic wad of dung',
    'A magic sphere that replays the most horrid-yet-catchy tune you have ever heard at random',
    'A squirrel that will occasionally bring you nuts, but will hide any small objects or string you posses nearby just as often',
    'An earring that will make you slightly more attractive to the opposite sex when pierced on your left buttock',
    'A cup that remains totally unmovable from where it was set unless there is absolutely no liquid left inside of it',
    'An elegant pair of shoes that make you run into walls on rare occasions',
    'A perfect cube of polished, solid dirt',
    'An artist\'s canvas that always appears to have mildly suggestive and socially unacceptable material portrayed on it, but is always masterfully done The artwork changes at random',
    'An endless, near-weightless bag, that produces only rubbish when you urgently need something specific from it Will only produce items you have stored in it otherwise, but always at random',
    'A ring that gives you the ability to command sheep in small numbers, but sheds dog hair in excessive amounts every 9 days',
    'A jack-in-the-box that will always produces a somewhat disturbing illusion that changes every time you use it',
    'A trusty sword of good steel that is haunted by several ornery, elderly, racist veterans of several different wars They are almost always present, and they all hate each other',
    'A walnut There seems to be magical properties to it maybe?',
    'A bag of salt You have tasted a small bit of it, and amazingly, you can taste the magic in the salt, though it doesn\'t seem holy',
    'A child-sized thumb You don\'t recall how you got it, but you\'re sure you knew somebody who was missing a thumb when you were younger',
    'An incredibly large ear that presumably belonged to a giant',
    'A small slip of paper that reads "Ce message n\'est pas pour vous, imbécile"',
    'The head of a polearm',
    'A bag containing three history books so out of date they\'re not even written in modern Common',
    'A long list of miscellaneous items There’s about 700 of them on the list',
    'A pint of milk that never goes bad, but always tastes like it\'s not quite right The pint bottle refills every day at the exact moment that the sun rises',
    'A one-man band comprised of a drum, an accordion, a harmonica, a tuba, cymbals, and a horn It seems to play whatever it wants though',
    'A broken dagger with the last part of a name inscribed on the remaining portion of the blade It reads "-dius"',
    'A small blue-black orb that when held up to the ear seems to emit the tiny screams of a thousand souls',
    'A hand mirror that holds the attention of anyone looking into it You feel absolutely fabulous',
    'A small device that when held right can be spun It has three protruding limbs and other than spinning seems to be of no particular interest',
    'A belt with a note accompanying it reading "This belt shall give power to those that wear it" It\'s buckle is missing and cannot be found',
    'A small slip of paper with wishes on it It will grant three wishes but will kill the person that makes the third wish Two wishes have already been used',
    'A sword made to harness the power of demon\'s blood It seems the blood has since been returned to its rightful owner',
    'A puzzle set that is missing a piece which never seems to be the same piece as last time',
    'A scroll on which is inscribed a childish insult that isn\'t very amusing',
    'A tiny cage containing a goblin that seems to hate you for something you apparently did to it despite never having seen or heard of this goblin until now',
    'A tiny book containing a list of ships that have docked but have never existed in real life or in fantasy literature',
    'A hardback blue book containing a list of every monster in the world and their exact demographics The book seems very old',
    'A metal butter container marked with the words "Property of Professor Chaos"',
    'A tin hat that is said to ward off creatures that steal your thoughts',
    'A leather-bound diary that when written in will make the ink disappear and answer back before once more disappearing',
    'An instruction manual that states what not to do in the events of potentially apocalyptic events',
    'Three green diamonds made of cloth that attach to each other when put near each other but separate when placed near water',
    'A cube made up of smaller cubes with images of even smaller cubes inside those cubes It seems to keep going on and on',
    'A fabric doll of a guard with an angry expression on it',
    'A tent that seems to get smaller and smaller with each use Who knows how small it can actually get',
    'A card game with monsters, traps, and spells on each card Playing one makes a small image of it appear and when played against another monster will attack one another',
    'A cube that plays a song from another time period It doesn\'t sound like anything that has existed so far',
    'A die with the classic six sides It seems each face shows a different outcome constantly and rolling it will reveal that outcome There seem to be an infinite number of potential outcomes',
    'Toothpicks made of razor blades and broken glass Who would even want to use this?',
    'A broken compass that seems to point away from your destination and doesn\'t seem to be able to be deceived',
    'A piece of chocolate that tastes bitter with a sweet aftertaste, it burns your tongue when tasted as well',
    'A weird brass pot that when opened reveals a hot steaming meal of great distaste to he who opens it',
    'A bag of weird living figurines of everyone you know, including yourself, and they seem to be unable to see you despite your ability to interact with them',
    'A weird yellow hat that belches into your ear when worn',
    'A vial of vomit that smells like roses for some odd reason',
    'A picture of the nastiest thing you have ever laid eyes on',
    'A box of jewels with an inscription on the box with the end scratched off It reads "Elements of" These jewels are powerful but seem to be unable to work',
    'A giant cupcake that has been half eaten',
    'A large sum of gold coins Upon closer inspection they are made of bone, without looking so closely you\'d never be able to tell they were fake',
    'A metal bucket with an old note in it It says "Gentleman This, is a bucket" followed by another note that says "dear god" followed by yet another that says "Wait, there\'s more" and finally one that simply says "NOoo" as if the person was in a state of disbelief',
    'A thin metal box with images of people you hate and six bags of tobacco for smoking',
    'A very scary painting of yourself that seems to age the longer you look at it It resets by morning',
    'A thing made of materials None of this looks familiar to you in any shape or form and makes you very uncomfortable',
    'A broken staff that partly disintegrates when it is touched, but always leaves some material behind',
    'A plush toy of an owl with a label attached to it that reads "Comet"',
    'A tiny wheel of cheese with a hole in the middle',
    'A loaf of bread made into the shape of a longsword that is stale',
    'A picture that shows a random location you ask about in the general area, though it usually shows you perverted things as if it had a mind of its own You feel its name is Jiraiya',
    'A cow leather belt that allows you to speak with cows, yet makes you sheepish in the presence of sheep',
    'A ring that seems to get smaller while you wear it',
    'A hammer that whispers to you seductively in your sleep and takes pleasure in being used You are usually creeped out by it',
    'A bottle that contains an odd green liquid that floats on water',
    'A leather pouch that contains seventeen sewing needles',
    'A letter that can barely be read, smudged by tears and withered by seawater, with the legible parts reading "Camereone\'ll bhapmedy-N"',
    'A baked clay figurine of a wide-eyed kobold with a bone in its mouth',
    'A rudimentary deck of playing cards made on the backs of "Wanted Person" leaflets',
    'A thick leather belt with impressions and engravings depicting the stages of a moon',
    'An old farmers almanac with pages cut to conceal small items inside',
    'A highly-polished, palm-sized steel orb that always rolls downhill',
    'A ship\'s flag that doesn\'t move in the wind',
    'The fantastical skull of a rare hornless unicorn or at least that\'s what the merchant who sold it to you claimed it was He wouldn\'t have lied to you now, would he?',
    'An otherwise ordinary skull, if not for the third eyehole nestled in the center of its forehead',
    'A scrimshaw depicting several northern nomads hunting a great elk, carved into the tooth of a saber-toothed tiger',
    'A black ring covered with some very faint, illegible etchings that glow with a red light when in darkness It feels somewhat warm to the touch when worn',
    'The last baby tooth of a young giant, who lost it long ago',
    'The skull of a wolf, peculiar for the rack of antlers sprouting from the top of its head',
    'A small, mechanical bear that fits in the palm of your hand It dances whenever music is played, yet no power source nor mechanism can be detected',
    'A small wooden top that refuses to stop spinning, despite your best efforts',
    'A sealed glass jar filled with a pale, reddish liquid A small, deformed humanoid floats in the middle of it, and you swear that you can see it twitch whenever you are not looking directly at it',
    'A note you found in your pocket one day instead of a pouch of coins It only says "IOU"',
    'An odd torch that produces a blue flame yet seemingly no heat or light At least it never goes out',
    'A set of exquisitely crafted dice, carved from the tusks of a mammoth Dwarvish runes replace the typical pips on the sides, and glow a faint blue',
    'A vial of purple fluid that, when poured onto an inanimate object of size small or tiny, will cause said object to become translucent in appearance for one hour',
    'An incredibly crude knife seemingly carved from a stone giant\'s toenail',
    'A silver ring with runic etchings In place of where a jewel would go, however, there is instead a small depression wherein rests an orb of green flame that never goes out but which also does not burn',
    'A walking stick shaped from a gnarled elm root A small branch is sprouting from it, tipped with several leaves',
    'A sealed Ship in a Bottle, enchanted by a wizard As you watch, the ship rocks back and forth as tiny waves crash about it',
    'A small bird unlike any you\'ve ever seen, trapped in a chunk of amber',
    'A tumorous mass of flesh that squelches along the ground behind you, aided by a sinewy mass of veins and arteries that act akin to tentacles',
    'A pewter armlet adorned with a pack of wolves engraved into its surface When you rub your fingers lightly over it, the sounds of distant howls echo through the air',
    'A gold stud earring that whispers completely useless facts into its wearer\'s ear',
    'A silver pocketwatch that can correctly tell the time on whatever plane it is currently on',
    'Small bits of nuts and fruit that seemingly never go bad and you cannot bring yourself to eat Reminds you of a pet bird you once had',
    'A blue flame in a jar that gives encouraging statements when you\'re feeling sad',
    'A old box that used to contain your favorite poem You\'re not quite sure where the poem went though you can remember having it just a few minutes ago',
    'A gold nugget that merchants never seem to want to buy You remember one merchant in particular who mumbled something about a curse after attempting to sell it to him, though you feel no effect',
    'A sad looking wooden idol It makes you and others around you feel sad just by looking at it',
    'Three pairs of shoes that each wouldn\'t even fit a baby',
    'Your favorite pair of socks They\'re worn down and aren\'t worth wearing anymore',
    'A painting about the size of your hand It depicts a crudely drawn man holding a flower Who drew this?',
    'A calendar with every day of the year labeled with the phrase "CLEAN CLEAN IT ALL" You never want to meet the person who did this',
    'The leg of a chair that broke off with a friend of yours sitting in it You remember using it as a fake weapon when you were young',
    'Five identical pieces of wood They\'re too perfect to use for anything',
    'A poorly crafted clay animal You can\'t quite tell which one it\'s supposed to be',
    'A chalice with the words "You drink too much" at the bottom of the cup',
    'The cowl of a renowned thief It seems to be cursed and you can\'t bring yourself to put it on',
    'The deed to a plot of land in the middle of the ocean',
    'A small box full of miniature instruments They all play quite beautifully in the hands of something that can play them',
    'A map of a place that doesn\'t exist You get a sinking feeling whenever you look at it',
    'A poster for a play for the deaf Everybody in the photo is wearing ridiculous masks to play different characters',
    'A painting of the most horrid, obscene thing you\'ve ever seen in your life The brushwork and composition are impeccable',
    'A book detailing the workings of a fake machine',
    'A mask of an unknown person His expressions seem too big for his face',
    'A fabled lockpick that supposedly never breaks It seems to have lost its power, however, as it had broken on the first use',
    'Three thousand tiny hats that you almost can\'t see You can only tell they\'re hats because you get a wizard to enlarge one for a short period of time',
    'A tiny figurine of a wolf that whines when left alone',
    'A miniature replica anchor that refuses to sink',
    'The equivalent of two hundred million gold pieces in orange pieces of paper They go to a game you played when you were little',
    'A piece of string about 3 inches in length with a tiny, crude-looking shoe tied to one end made of wood that, when pinched, shocks you harmlessly',
    'A clay bowl with a painting of a fingernail in it',
    'A box full of childhood possessions You can\'t seem to remember any of them',
    'A small card welcoming you to a famous city It has a letter on the back that\'s from a friend of yours explaining their experiences in the city',
    'A large, metal wheel of cheese that always smells like the ocean',
    'Three balls bound by a metal wire, one made of wood, one made of lead, and one made of flesh',
    'A shred of paper that partially reads "One for the dame, one fo-"',
    'A love letter written by a beggar from your hometown Funny, you don\'t remember being given this',
    'A small cheat sheet that went to a test from school It didn’t help much',
    'An old, rusty and dull sword It’s so dull it almost qualifies as a club',
    'Protective eyewear It’s a bit small for a human, but can fit perfectly on any other race, oddly enough',
    'A long-winded and ultimately misleading report on the growth of peanuts',
    'An almost lifelike painting of a bald, half-naked man holding fish in every appendage, including his mouth',
    'A collection of figurines of every kind of dragon',
    'An incomplete collection of cheese knives There’s about seventeen of them in the container',
    'A deck of cards that, when left alone for too long, will start shuffling and dealing themselves to all nearby people',
    'A die with 7 sides made of bone The side where \'7\' would be shown is instead replaced with a heart',
    'A miniature piano that can fit in the palm of your hand but still plays and sounds exactly like a full-sized one',
    'A petrified leaf',
    'The bloody pointed tooth of a famous vampire',
    'A loaf of bread you never ended up eating It hasn’t gotten moldy, somehow',
    'A small fluegelhorn that cannot be played correctly, even in the hands of a master',
    'Eighteen miniature cabbage heads They aren’t edible',
    'An unreadable note The only words you can make out are “get the body bag Seymour”',
    'A list of ingredients to make a potion that makes everything taste faintly of cauliflower',
    'The ashes of your paternal figure',
    'A singing bee It Doesn’t seem to mind being kept in a jar',
    'A white cloak that cannot be stained by any means',
    'A witch\'s undergarments',
    'A beautiful sundress made by a blind seamstress',
    'A collar that fits any creature it is placed on It\'s got the cutest little bell affixed to the front of it',
    'A completely normal silk glove that you absolutely should not ask any questions about',
    'A tiny dragon figurine that is animated when put in direct sunlight It\'s very friendly',
    'A painting of a baby that giggles when you look away from it',
    'A journal containing stories of the owner\'s adventures with a bugbear',
    'A singular playing card If you try to cheat with it, it laughs It’s the ace of diamonds',
    'A set of very powerful rattle snake magnets',
    'Five keys fused together in such a way that they could never open anything You have nightmares of being burned alive whenever you sleep near it',
    'A hypercube that dings lightly every eight days, eight hours, eight minutes, and eight seconds',
    'A small chalkboard that can never be written on but shows a random word If you ever try to erase it, a new word is shown',
    'A tiny stone angel in an unbreakable glass box It moves whenever you\'re not looking',
    'A brown, thousand-page book with the word resurrection written a thousand times on each page',
    'A random trinket that turns itself into another random trinket at every twenty-five hours',
    'A ball of clay that grows a new eye every 1d4 hours 1d4 hours later, that eye disappears No matter what, the eyes are always staring into yours',
    'A small golden bell with a red velvet ribbon and no ringer The bells chimes very faintly when in the presence of royalty',
    'A silver ring with an amethyst on it It feels calming to put it on',
    'Two sweet smelling branches Smelling them for too long makes you nauseous and gives you a headache',
    'A large skull of a were-chicken Who knows how he got like that?',
    'A tiny decorative anchor that glows slightly whenever a nearby creature teleports',
    'A brick that always feels slippery',
    'A large snow globe that houses a tiny kobold and his family',
    'A sacred chime that’s supposedly connected to faith and the gods',
    'A pair of leather gloves that can never get wet',
    'A singular strand of wire about three feet long It shocks you fequently, even through something like leather',
    'An old and blue greatsword There seems to be some magical properties attached to it, though it seems lifeless Perhaps something happened?',
    'Four jars with flaming butterflies inside When broken, the butterflies ignite whatever it was broken over',
    'A red feather that shines softly in the dark',
    'A ball that engulfs itself in harmless blue fire when thrown',
    'A gold-plated badge emblazoned with a symbol of fire',
    'A bowl filled with dim continual flames that change color when different powdered materials are added',
    'A humanoid poppet, made from twisted roots, with singed limbs',
    'A flute that, when played, forms illusory lines of fire which dance to the music around the player',
    'An ash wood walking stick',
    'A pouch of dust that when sprinkled onto a fire cause firework-like sparks and crackles',
    'A map of the sun',
    'A pair of boots that leave scorched footprints',
    'A bottle filled with morning light ember',
    'A pyrography quill that leaves flaming script on the parchment',
    'An old brass lamp in which an efreet once resided; his name is inscribed on the rim in Ignan script',
    'A chalice that makes the drinker’s blood glow with an inner fire for a few minutes afterward',
    'An ever-smoldering lump of coal',
    'A thin iron pinky ring, melted and charred but still wearable',
    'An ever-lit smoking pipe',
    'Pocket hand-bellows that were probably meant as a child\'s toy but are useful for starting fires none-the-less',
    'A pocketbook of flame identification called \'Tongues and Their Reading\' used to tell magical flames from natural ones and much more',
    'A candlestick with a jeweler\'s mark stamped into the base',
    'A ring that grows warm when near common magical items',
    'A dagger that was once owned by a man struck by a lightning bolt spell; it still flickers with (harmless) electricity',
    'A simple crown of woven rowan that glows faintly with unearthly light',
    'A wand that, when waved over a bowl, makes the food therein taste spicy',
    'A spoon that, when used to stir a drink, makes the beverage piping hot',
    'A shallow bowl that makes all spellcasters who eat or drink from it feel faintly nauseous',
    'A rock that may be absorbed into any point on the body and produced from another point at will',
    'A small compass that never points north, and sometimes points at strangers',
    'A strange purple dust that can be sprinkled on tiny objects, causing them to hover 5 feet off the ground for 1 minute',
    'A bobbin of thick string with which it is impossible to tie knots',
    'A blue sash cut from perfectly hydrophobic cloth',
    'A small, hollow metallic orb that vibrates when tapped While vibrating it prevents anyone in close proximity from sleeping It stops vibrating when tapped again',
    'A sheet of papyrus that captures a person’s portrait when a command word is spoken (reusable if the command word is known)',
    'A hand crank music box which plays a melody that causes listeners to think they are dreaming',
    'A chain of alternating silver and bronze links The silver links are ethereal, while the bronze links are not, but they can still interact with the other links',
    'A box and lid crafted from a strange, white, pliable material Foodstuffs sealed within remain fresh for two weeks',
    'An acacia wood spinning top which never topples When spun on flat wood, it carves elegant abstract engravings',
    'An invitation to a magician’s circle on a date that doesn’t quite make sense',
    'A stuffed jackdaw that occasionally blinks or cocks its head',
    'A titanium sewing needle that can only unweave thread',
    'An empty scabbard with an intricate design etched into the leather With enough study, it may be interpreted as a map that purports to leads to the location of the matching sword',
    'A 1-inch high pewter elf soldier, armed with a shield and longsword; the base reads “4 of 7”',
    'A bill of sale for two dozen magic morningstars, sold by Alvin Cogsbottom and purchased by Farbgarble (bugbear warlord)',
    'A pencil-on-paper schematic of a crossbow-like contraption of tubes, triggers and optics',
    'A blue blade shard that hums If a person holds the piece for long enough they will start hearing voices that urge him to kill and claim souls for it',
    'A pair of tailor’s shears that can cut through any kind of leather',
    'A curious talking ebony walking stick, well versed in history and swordplay',
    'An old, worn smith\'s hammer Its head is always hot to the touch',
    'A vial of oil labelled “Tomonari’s anointmente forr long swordes and other weppons of the disttinguished nobelemann”',
    'A woodcutter’s axe, the head of which shimmers like downwards-flowing water',
    'A quarterstaff with a small jade sphere affixed to one end When swung, the jade leaves a faint trail of color',
    'A perpetually wet whetstone',
    'A smooth river stone with shards of bone stuck into it If you look hard enough you can see that the bones are not of a humanoid but of a giant',
    'A strange rock hammer with a steelmark of Abyssal runes The runes read “HAIL TO THE KING OF THE ROCK”',
    'A rag intended to be wrapped around the scabbard of a sword It magically wicks blood and other liquids away from a sword as it is sheathed',
    'An impossibly sharp pen that will always be in the owner’s pocket when they reach into it',
    'A model bronze weapon rack with six detachable polearms Each is three inches long and decorated with a red horse-hair tassel',
    'A feathered arrow embedded in a frozen potato',
    'A halfling skull with a significant parietal slashing wound that also corroded the bone',
    'A pocket instruction manual depicting bizarre fighting stances of leaping, spinning and holding weapons by the wrong end',
    'A small stone cube with the coat of arms of a different family on each side',
    'A large, tattered flag with silver, green, and black stripes',
    'A mithral key about six inches long',
    'A spyglass, dented and bent in half However, because the inside is so reflective it can still be used',
    'A crown made of polished and carved ash with gold inlays',
    'A wooden cup, divided in half lengthwise with a sheet of aluminum',
    'A grappling hook with silken cord attached to the end One of the three hooks is broken, and another is bent almost in line with the body of the hook',
    'A small model of a castle that matches a real one exactly and changes to match new alterations',
    'A dagger\'s hilt The pommel is carved in the form of a lion',
    'A crown of tarnished silver Spikes are woven throughout it',
    'A long arrow, with the tip hollow as if it once contained a message',
    'A tattered painting of a royal family The faces are scratched out',
    'A small crystal goblet which makes an unusual ringing sound when tapped',
    'The blade of an ancient sword A mysterious coat of arms is carved into it',
    'A small stone block from a long-forgotten castle For some reason, gripping it puts you in a foul mood',
    'Ripped and torn mail links They seem to glow with a royal brilliance, but do not emit any actual light',
    'Half of a snapped oak flag-pole "We will fight to the last" is written in dried blood on one side',
    'A torn, warped copy of "Evard\'s Poetry- 100 Poems for the Aspiring Prince"',
    'Half of a signet ring It looks like it was once the stamp for an ancient royal seal',
    'A much-loved child\'s doll embroidered with gold thread It\'s been through a lot',
    'The perfect fitting bra, that always gets returned the very next day',
]

Gear = {
    'C': {
        'Abacus': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Ale (gallon)': {
            'Base Price': 20,
            'Class': 'Food & Drink & Lodging'
        },
        'Artisan Glue (gallon)': {
            'Base Price': 200,
            'Class': 'Tools & Skill Kits'
        },
        'Artisan Scissors': {
            'Base Price': 100,
            'Class': 'Tools & Skill Kits'
        },
        "Artisan's Outfit": {
            'Base Price': 100,
            'Class': 'Clothing'
        },
        "Artisan's Tools": {
            'Base Price': 500,
            'Class': 'Tools & Skill Kits'
        },
        'Backpack (empty)': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Barrel (empty)': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Basket (empty)': {
            'Base Price': 40,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Bedroll': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Belt Pouch (empty)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Birch Bark': {
            'Base Price': 1,
            'Class': 'Food & Drink & Lodging'
        },
        'Biscuit Bin': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Bit & Bridle': {
            'Base Price': 200,
            'Class': 'Mounts & Related Gear'
        },
        'Blanket (winter)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Block and Tackle': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Boiled Sweets': {
            'Base Price': 4,
            'Class': 'Food & Drink & Lodging'
        },
        'Bread (per loaf)': {
            'Base Price': 2,
            'Class': 'Food & Drink & Lodging'
        },
        'Broom': {
            'Base Price': 8,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Bucket (empty)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Bullfrog (Pair)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Bush (Small)': {
            'Base Price': 20,
            'Class': 'Commodities'
        },
        'Butter': {
            'Base Price': 5,
            'Class': 'Food & Drink & Lodging'
        },
        'Butter Churn': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Candle': {
            'Base Price': 1,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Candle Lantern': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Canvas (sq yd)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Canvas Apron': {
            'Base Price': 30,
            'Class': 'Clothing'
        },
        'Cart': {
            'Base Price': 1500,
            'Class': 'Transport'
        },
        'Cat': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Chain Barding (Large)': {
            'Base Price': 60000,
            'Class': 'Mounts & Related Gear'
        },
        'Chain Barding (Medium)': {
            'Base Price': 30000,
            'Class': 'Mounts & Related Gear'
        },
        'Chalk (1 piece)': {
            'Base Price': 1,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Chamber Pot': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Chest (empty)': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Chimney Brush Kit': {
            'Base Price': 80,
            'Class': 'Tools & Skill Kits'
        },
        'Chunk of Meat': {
            'Base Price': 30,
            'Class': 'Food & Drink & Lodging'
        },
        'Cider Press': {
            'Base Price': 100,
            'Class': 'Tools & Skill Kits'
        },
        'Clay Jug': {
            'Base Price': 3,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Clay Smoking Pipe': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Cleric's Vestments": {
            'Base Price': 500,
            'Class': 'Clothing'
        },
        'Cloth Apron': {
            'Base Price': 10,
            'Class': 'Clothing'
        },
        'Coal (5 lb)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Cold Weather Outfit': {
            'Base Price': 800,
            'Class': 'Clothing'
        },
        'Common Back Scratcher': {
            'Base Price': 3,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Bed Clothing': {
            'Base Price': 8,
            'Class': 'Clothing'
        },
        'Common Bowl': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Buckle': {
            'Base Price': 20,
            'Class': 'Clothing'
        },
        'Common Buttons (12)': {
            'Base Price': 5,
            'Class': 'Clothing'
        },
        'Common Casket': {
            'Base Price': 40,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Cloth Dye (10yd)': {
            'Base Price': 50,
            'Class': 'Tools & Skill Kits'
        },
        'Common Curtains': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Decorative Plant': {
            'Base Price': 2,
            'Class': 'Commodities'
        },
        'Common Dried Herbs': {
            'Base Price': 2,
            'Class': 'Commodities'
        },
        'Common Eating Utensils': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Eye Patch': {
            'Base Price': 2,
            'Class': 'Tools & Skill Kits'
        },
        'Common Flower Pot': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Foot Stool': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Glass Eye': {
            'Base Price': 5,
            'Class': 'Tools & Skill Kits'
        },
        'Common Gloves': {
            'Base Price': 4,
            'Class': 'Clothing'
        },
        'Common Hat/Headpiece': {
            'Base Price': 5,
            'Class': 'Clothing'
        },
        'Common Hide Blanket': {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Nuts (in shell)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Common Pelt (Medium)': {
            'Base Price': 500,
            'Class': 'Commodities'
        },
        'Common Pelt (Small)': {
            'Base Price': 50,
            'Class': 'Commodities'
        },
        'Common Pelt (Tiny)': {
            'Base Price': 8,
            'Class': 'Commodities'
        },
        'Common Pet Bird': {
            'Base Price': 2,
            'Class': 'Commodities'
        },
        'Common Pet Collar': {
            'Base Price': 5,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Pillow': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Rats (Pair)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Common Serving Bowl': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Smoking Pipe': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Tablecloth': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Toy Doll': {
            'Base Price': 3,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Vase': {
            'Base Price': 5,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Vegetables': {
            'Base Price': 1,
            'Class': 'Food & Drink & Lodging'
        },
        'Common Wine (pitcher)': {
            'Base Price': 20,
            'Class': 'Food & Drink & Lodging'
        },
        'Common Wooden Toy': {
            'Base Price': 5,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common fresh Fruit': {
            'Base Price': 2,
            'Class': 'Food & Drink & Lodging'
        },
        "Cook's Knives (set)": {
            'Base Price': 800,
            'Class': 'Tools & Skill Kits'
        },
        'Cookie Cutter': {
            'Base Price': 5,
            'Class': 'Tools & Skill Kits'
        },
        'Cookies (dozen)': {
            'Base Price': 5,
            'Class': 'Food & Drink & Lodging'
        },
        'Cooking Stone': {
            'Base Price': 200,
            'Class': 'Tools & Skill Kits'
        },
        'Cooking Utensils (set)': {
            'Base Price': 50,
            'Class': 'Tools & Skill Kits'
        },
        'Copper/Stone Ash Bowl Common': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Cough Sweets': {
            'Base Price': 10,
            'Class': 'Food & Drink & Lodging'
        },
        'Covered Cart': {
            'Base Price': 2000,
            'Class': 'Transport'
        },
        'Crab Trap': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Craftsman's Paint (5 gal)": {
            'Base Price': 500,
            'Class': 'Tools & Skill Kits'
        },
        'Dandelion Wine (pitcher)': {
            'Base Price': 10,
            'Class': 'Food & Drink & Lodging'
        },
        'Domesticated Turkey': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Donkey or Mule': {
            'Base Price': 800,
            'Class': 'Mounts & Related Gear'
        },
        'Dozen Eggs': {
            'Base Price': 1,
            'Class': 'Food & Drink & Lodging'
        },
        'Drying Towel': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Duck': {
            'Base Price': 3,
            'Class': 'Commodities'
        },
        "Farmer's Tools": {
            'Base Price': 100,
            'Class': 'Tools & Skill Kits'
        },
        'Feather Mat': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Feed (per day)': {
            'Base Price': 5,
            'Class': 'Mounts & Related Gear'
        },
        'Filling Putty (4 use vial)': {
            'Base Price': 2500,
            'Class': 'Special Substances & Items'
        },
        'Firewood (per day)': {
            'Base Price': 1,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fishhook': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fishing Net (25 sq ft)': {
            'Base Price': 400,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Flask (empty)': {
            'Base Price': 3,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Flint Chips (12)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Flint and Steel': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Flower Bouquet': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fruit Pie (freshly baked)': {
            'Base Price': 10,
            'Class': 'Food & Drink & Lodging'
        },
        "Full Barber's Services": {
            'Base Price': 100,
            'Class': 'Services'
        },
        'Gallon Cider': {
            'Base Price': 20,
            'Class': 'Food & Drink & Lodging'
        },
        'Gallon Mead': {
            'Base Price': 20,
            'Class': 'Food & Drink & Lodging'
        },
        'Gerbil (Pair)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Glass Beads (24)': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Glass Goblet': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Grape Vine (Small)': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Grave Digger': {
            'Base Price': 10,
            'Class': 'Services'
        },
        'Guinea Pig': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Hair Brush': {
            'Base Price': 8,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Hair Comb': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Hair and Body Soap (flask)': {
            'Base Price': 50,
            'Class': 'Special Substances & Items'
        },
        'Hammer': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Healer's Kit": {
            'Base Price': 5000,
            'Class': 'Tools & Skill Kits'
        },
        'Hearth Tools': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Heavy Horse': {
            'Base Price': 20000,
            'Class': 'Mounts & Related Gear'
        },
        'Hemp Rope (50 ft)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Hide Apron': {
            'Base Price': 200,
            'Class': 'Clothing'
        },
        'Holy Symbol (Wooden)': {
            'Base Price': 100,
            'Class': 'Tools & Skill Kits'
        },
        'Holy Water (flask)': {
            'Base Price': 2500,
            'Class': 'Special Substances & Items'
        },
        'Honey': {
            'Base Price': 80,
            'Class': 'Food & Drink & Lodging'
        },
        'Hot Toffee Apple': {
            'Base Price': 3,
            'Class': 'Food & Drink & Lodging'
        },
        'House Slippers': {
            'Base Price': 50,
            'Class': 'Clothing'
        },
        'Hunk of Cheese': {
            'Base Price': 10,
            'Class': 'Food & Drink & Lodging'
        },
        'Inferior Meat (chunk)': {
            'Base Price': 5,
            'Class': 'Food & Drink & Lodging'
        },
        'Ink Vial (empty)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Jam': {
            'Base Price': 30,
            'Class': 'Food & Drink & Lodging'
        },
        "Juggler's Balls": {
            'Base Price': 80,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Kettle': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Kudzu Vine (Small)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Ladder (10 ft)': {
            'Base Price': 5,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Lamp (Common)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Lard': {
            'Base Price': 1,
            'Class': 'Food & Drink & Lodging'
        },
        'Leather Barding (Large)': {
            'Base Price': 4000,
            'Class': 'Mounts & Related Gear'
        },
        'Leather Barding (Medium)': {
            'Base Price': 2000,
            'Class': 'Mounts & Related Gear'
        },
        'Leather Belt (Common)': {
            'Base Price': 10,
            'Class': 'Clothing'
        },
        'Leather Cord (10 ft)': {
            'Base Price': 8,
            'Class': 'Commodities'
        },
        'Lice and Flea Soap (flask)': {
            'Base Price': 100,
            'Class': 'Special Substances & Items'
        },
        'Light Horse': {
            'Base Price': 7500,
            'Class': 'Mounts & Related Gear'
        },
        'Light Leather Gloves': {
            'Base Price': 20,
            'Class': 'Clothing'
        },
        'Lip Wax': {
            'Base Price': 5,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Lock (Very Simple)': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Loincloth': {
            'Base Price': 2,
            'Class': 'Clothing'
        },
        'Lumber Axe': {
            'Base Price': 600,
            'Class': 'Tools & Skill Kits'
        },
        'Lumber Saw': {
            'Base Price': 600,
            'Class': 'Tools & Skill Kits'
        },
        'Meat Grinder': {
            'Base Price': 200,
            'Class': 'Tools & Skill Kits'
        },
        "Merchant's Scale": {
            'Base Price': 200,
            'Class': 'Tools & Skill Kits'
        },
        'Messenger (per mile)': {
            'Base Price': 2,
            'Class': 'Services'
        },
        'Midwife': {
            'Base Price': 20,
            'Class': 'Services'
        },
        'Mop': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Mourner': {
            'Base Price': 10,
            'Class': 'Services'
        },
        'Mouse Trap': {
            'Base Price': 5,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Mug/Tankard (clay)': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Mushrooms': {
            'Base Price': 5,
            'Class': 'Food & Drink & Lodging'
        },
        'Musical Instrument (Common)': {
            'Base Price': 500,
            'Class': 'Tools & Skill Kits'
        },
        'Nails (100)': {
            'Base Price': 50,
            'Class': 'Tools & Skill Kits'
        },
        'Newts (6)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Non-poisonous Snake (Diminutive)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Non-poisonous Snake (Small)': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Non-poisonous Snake (Tiny)': {
            'Base Price': 3,
            'Class': 'Commodities'
        },
        'Oar': {
            'Base Price': 200,
            'Class': 'Transport'
        },
        'Ordinary Nutcracker': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Ox': {
            'Base Price': 2000,
            'Class': 'Commodities'
        },
        "Peasant's Outfit": {
            'Base Price': 10,
            'Class': 'Clothing'
        },
        'Pet Leash': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Pewter Goblet': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Pewter Mug/Tankard': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Pickled Vegetables': {
            'Base Price': 10,
            'Class': 'Food & Drink & Lodging'
        },
        'Pitcher (clay)': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Pitcher Milk': {
            'Base Price': 3,
            'Class': 'Food & Drink & Lodging'
        },
        'Plates (Common) set of 4': {
            'Base Price': 40,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Plow': {
            'Base Price': 3000,
            'Class': 'Tools & Skill Kits'
        },
        'Pole (10 ft)': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Pony': {
            'Base Price': 3000,
            'Class': 'Mounts & Related Gear'
        },
        'Pot (iron)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Potato Bin': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Potion Vial (empty)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Pumice': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Quality Corn Feed': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Rabbit': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        "Rabbit's Foot": {
            'Base Price': 5,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Rash Ointment (jar)': {
            'Base Price': 1000,
            'Class': 'Special Substances & Items'
        },
        'Rat Trap': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Rope Bed': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Rowboat': {
            'Base Price': 5000,
            'Class': 'Transport'
        },
        'Sack (empty)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Saddle (Pack)': {
            'Base Price': 500,
            'Class': 'Mounts & Related Gear'
        },
        'Saddle (Riding)': {
            'Base Price': 1000,
            'Class': 'Mounts & Related Gear'
        },
        'Saddlebags': {
            'Base Price': 400,
            'Class': 'Mounts & Related Gear'
        },
        'Sassafras Root': {
            'Base Price': 3,
            'Class': 'Food & Drink & Lodging'
        },
        'Scale Barding (Large)': {
            'Base Price': 20000,
            'Class': 'Mounts & Related Gear'
        },
        'Scale Barding (Medium)': {
            'Base Price': 10000,
            'Class': 'Mounts & Related Gear'
        },
        'Sealing Wax': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Seeds (50)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Sewing Needle': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Signal Whistle': {
            'Base Price': 80,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Simple Barber's Services": {
            'Base Price': 10,
            'Class': 'Services'
        },
        'Simple Cake': {
            'Base Price': 8,
            'Class': 'Food & Drink & Lodging'
        },
        'Skillet': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Sled': {
            'Base Price': 2000,
            'Class': 'Transport'
        },
        'Sledge': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Smelling Salts (flask)': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Soap (per Lb)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Soft Cheese': {
            'Base Price': 10,
            'Class': 'Services'
        },
        'Soup Pot': {
            'Base Price': 1000,
            'Class': 'Tools & Skill Kits'
        },
        'Soup/Dog Bones': {
            'Base Price': 2,
            'Class': 'Food & Drink & Lodging'
        },
        'Spade or Shovel': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Spindle': {
            'Base Price': 4,
            'Class': 'Tools & Skill Kits'
        },
        'Spinning Wheel': {
            'Base Price': 1000,
            'Class': 'Tools & Skill Kits'
        },
        'Straw Mat': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Studded Leather Barding (Large)': {
            'Base Price': 10000,
            'Class': 'Mounts & Related Gear'
        },
        'Studded Leather Barding (Medium)': {
            'Base Price': 5000,
            'Class': 'Mounts & Related Gear'
        },
        'Suede Boots (ankle high)': {
            'Base Price': 10,
            'Class': 'Clothing'
        },
        'Suede Boots (knee high)': {
            'Base Price': 30,
            'Class': 'Clothing'
        },
        'Sugar (1 Lb)': {
            'Base Price': 30,
            'Class': 'Food & Drink & Lodging'
        },
        'Tacks (100)': {
            'Base Price': 20,
            'Class': 'Tools & Skill Kits'
        },
        'Tent': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Tent Wagon': {
            'Base Price': 8500,
            'Class': 'Transport'
        },
        'Thread': {
            'Base Price': 5,
            'Class': 'Tools & Skill Kits'
        },
        'Torch': {
            'Base Price': 1,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Trail Rations (per day)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Traveler's Outfit": {
            'Base Price': 100,
            'Class': 'Clothing'
        },
        'Turtle': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Undertaker': {
            'Base Price': 50,
            'Class': 'Services'
        },
        'Untrained Hireling (per day)': {
            'Base Price': 10,
            'Class': 'Services'
        },
        'Vinegar (gallon) in jar': {
            'Base Price': 5,
            'Class': 'Food & Drink & Lodging'
        },
        'Wagon': {
            'Base Price': 3500,
            'Class': 'Transport'
        },
        'Waste Bin (10 gallon)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Waste Bin (5 gallon)': {
            'Base Price': 4,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Waterskin': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wheelbarrow': {
            'Base Price': 300,
            'Class': 'Tools & Skill Kits'
        },
        'Whetstone': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wiping Rug': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Ash Bowl (Common)': {
            'Base Price': 8,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Beads (24)': {
            'Base Price': 1,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Dice (Pair)': {
            'Base Price': 1,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Garment Hook': {
            'Base Price': 3,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Mask': {
            'Base Price': 500,
            'Class': 'Clothing'
        },
        'Wooden Picture frame (Small)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Picture frame (Tiny)': {
            'Base Price': 3,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Serving Tray': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Stool (Medium)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Stool (Small)': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Wash Basin': {
            'Base Price': 400,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wool Mittens': {
            'Base Price': 8,
            'Class': 'Clothing'
        },
        'Wool Scarf': {
            'Base Price': 10,
            'Class': 'Clothing'
        },
        'Wool Stockings/Socks': {
            'Base Price': 8,
            'Class': 'Clothing'
        },
        'Yarn Ball (500 ft)': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Yeast (baker) (for 10 Lb)': {
            'Base Price': 2,
            'Class': 'Food & Drink & Lodging'
        },
        'Yeast (brewer) (for 10 gal)': {
            'Base Price': 2,
            'Class': 'Food & Drink & Lodging'
        },
        'Yoke (and accessories)': {
            'Base Price': 200,
            'Class': 'Transport'
        }
    },
    'U': {
        'Acid (flask)': {
            'Base Price': 1000,
            'Class': 'Special Substances & Items'
        },
        "Alchemist's Fire (flask)": {
            'Base Price': 2000,
            'Class': 'Special Substances & Items'
        },
        'Animal (Medium) Cage': {
            'Base Price': 5000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Animal (Small) Cage': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Animal (Tiny) Cage': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Banded Barding (Large)': {
            'Base Price': 100000,
            'Class': 'Mounts & Related Gear'
        },
        'Banded Barding (Medium)': {
            'Base Price': 50000,
            'Class': 'Mounts & Related Gear'
        },
        "Barber's Kit": {
            'Base Price': 1000,
            'Class': 'Tools & Skill Kits'
        },
        'Bell': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Blank Book': {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Blemish Cream (jar)': {
            'Base Price': 3000,
            'Class': 'Special Substances & Items'
        },
        "Blood Letter's Leeches (flask of 12 live)": {
            'Base Price': 20,
            'Class': 'Tools & Skill Kits'
        },
        'Brass Garment Hook': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Caltrops': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Carnivorous Plant': {
            'Base Price': 3,
            'Class': 'Commodities'
        },
        'Carriage': {
            'Base Price': 10000,
            'Class': 'Transport'
        },
        'Case (map or scroll)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Cedar Chips': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Ceramic Mask': {
            'Base Price': 2000,
            'Class': 'Clothing'
        },
        'Chain (10 ft)': {
            'Base Price': 3000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Clotting Paste (jar)': {
            'Base Price': 3000,
            'Class': 'Special Substances & Items'
        },
        'Coach Cab (per mile)': {
            'Base Price': 3,
            'Class': 'Services'
        },
        'Coffee Beans': {
            'Base Price': 200,
            'Class': 'Commodities'
        },
        'Common Bedside Table': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Birdbath': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Bookmark': {
            'Base Price': 1,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Cage Wagon': {
            'Base Price': 45000,
            'Class': 'Transport'
        },
        'Common Caravan Wagon': {
            'Base Price': 75000,
            'Class': 'Transport'
        },
        'Common Chest of Drawers': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Dining Chair': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Dining Table': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Dresser (standing)': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Festival Costume': {
            'Base Price': 500,
            'Class': 'Clothing'
        },
        'Common Kaleidoscope': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Leather Mask': {
            'Base Price': 200,
            'Class': 'Clothing'
        },
        "Common Master's Chair": {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Pelt (large)': {
            'Base Price': 2500,
            'Class': 'Commodities'
        },
        "Common Performer's Cart": {
            'Base Price': 50000,
            'Class': 'Transport'
        },
        'Common Perfume (vial)': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Plate Cabinet (standing)': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Puppet': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Stained Glass Work (per sq ft)': {
            'Base Price': 500,
            'Class': 'Services'
        },
        'Common Vanity Table (w/ Mirror)': {
            'Base Price': 50000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Common Wig': {
            'Base Price': 1000,
            'Class': 'Clothing'
        },
        'Copper/Stone Ash Bowl Fancy': {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Cork Wood': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Covered Sled': {
            'Base Price': 5000,
            'Class': 'Transport'
        },
        'Crowbar': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Dart Board': {
            'Base Price': 80,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Diary (Blank w/ lock)': {
            'Base Price': 2500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Diary (Blank w/o lock)': {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Disguise Kit': {
            'Base Price': 5000,
            'Class': 'Tools & Skill Kits'
        },
        'Dominos (set)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Entertainer's Outfit": {
            'Base Price': 300,
            'Class': 'Clothing'
        },
        'Essential Oil': {
            'Base Price': 200,
            'Class': 'Commodities'
        },
        "Explorer's Outfit": {
            'Base Price': 1000,
            'Class': 'Clothing'
        },
        'Fancy Back Scratcher': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Bookmark': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Bowl': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Buttons (12)': {
            'Base Price': 30,
            'Class': 'Clothing'
        },
        'Fancy Cake': {
            'Base Price': 100,
            'Class': 'Food & Drink & Lodging'
        },
        'Fancy Curtains': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Eye Patch': {
            'Base Price': 10,
            'Class': 'Tools & Skill Kits'
        },
        'Fancy Glass Eye': {
            'Base Price': 50,
            'Class': 'Tools & Skill Kits'
        },
        'Fancy Pet Collar': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fife (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        "Foldable Merchant's Table": {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Gallon Fortified Malt Brew': {
            'Base Price': 10,
            'Class': 'Food & Drink & Lodging'
        },
        'Gallon Stout (Brew)': {
            'Base Price': 30,
            'Class': 'Food & Drink & Lodging'
        },
        'Gallon Yam Beer': {
            'Base Price': 20,
            'Class': 'Food & Drink & Lodging'
        },
        'Gaming Table': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Glass Bottle (Wine)': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Glass Orb': {
            'Base Price': 100,
            'Class': 'Tools & Skill Kits'
        },
        'Goose': {
            'Base Price': 2,
            'Class': 'Commodities'
        },
        'Grand Songbook (blank)': {
            'Base Price': 1200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Guard Dog': {
            'Base Price': 2500,
            'Class': 'Mounts & Related Gear'
        },
        'Hair Dye (1 use)': {
            'Base Price': 100,
            'Class': 'Special Substances & Items'
        },
        'Half Gallon Distilled Spirits': {
            'Base Price': 100,
            'Class': 'Food & Drink & Lodging'
        },
        'Hamster (mated Pair)': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Itching Powder (1 vial)': {
            'Base Price': 1000,
            'Class': 'Special Substances & Items'
        },
        'Ivory Dice (Pair)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Ivy Vine (Small)': {
            'Base Price': 5,
            'Class': 'Commodities'
        },
        'Keelboat': {
            'Base Price': 300000,
            'Class': 'Transport'
        },
        'Lantern (Bullseye)': {
            'Base Price': 1200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Lantern (Hooded)': {
            'Base Price': 700,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Large Bookshelf': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Large Songbook (blank)': {
            'Base Price': 800,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Leather Belt (Fancy)': {
            'Base Price': 40,
            'Class': 'Clothing'
        },
        'Lock (Average)': {
            'Base Price': 4000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Lute (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        'Manacles': {
            'Base Price': 1500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Mandolin (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        "Masterwork Artisan's Tools": {
            'Base Price': 5500,
            'Class': 'Tools & Skill Kits'
        },
        'Medium Bookshelf': {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Medium Cook's Table": {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Medium Wooden Sign': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Miner's Pick": {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Mirror (Small steel)': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Molasses': {
            'Base Price': 20,
            'Class': 'Food & Drink & Lodging'
        },
        "Monk's Outfit": {
            'Base Price': 500,
            'Class': 'Clothing'
        },
        'Mugwort Pillow': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Nanny (per day)': {
            'Base Price': 1,
            'Class': 'Services'
        },
        'Natural Sponge (3”)': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Natural Sponge (5”)': {
            'Base Price': 4,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Natural Sponge (8”)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Oil (1 pint flask)': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Organ Box (Common)': {
            'Base Price': 300,
            'Class': 'Musical Instrument'
        },
        'Parchment (sheet)': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Pepper Mill': {
            'Base Price': 500,
            'Class': 'Tools & Skill Kits'
        },
        'Pet Fish': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Pickled Meat': {
            'Base Price': 80,
            'Class': 'Food & Drink & Lodging'
        },
        'Pitcher Fortified Wine': {
            'Base Price': 20,
            'Class': 'Food & Drink & Lodging'
        },
        'Piton': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Portable Coop': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Puppet Box': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Recipe Book (blank)': {
            'Base Price': 400,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Recorder (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        'Ring Toss Set': {
            'Base Price': 20,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Saddle (Military)': {
            'Base Price': 2000,
            'Class': 'Mounts & Related Gear'
        },
        'Salt/Sugar Cured Meat': {
            'Base Price': 60,
            'Class': 'Food & Drink & Lodging'
        },
        'Sailing Ship': {
            'Base Price': 1000000,
            'Class': 'Transport'
        },
        'Sausage': {
            'Base Price': 50,
            'Class': 'Food & Drink & Lodging'
        },
        "Scholar's Outfit": {
            'Base Price': 500,
            'Class': 'Clothing'
        },
        'Shawm (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        'Silk Rope (50 ft)': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Silk Scarf': {
            'Base Price': 50,
            'Class': 'Clothing'
        },
        'Silk Stockings/Socks': {
            'Base Price': 200,
            'Class': 'Clothing'
        },
        'Small Blank Book': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Small Bookshelf': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Small Cook's Table": {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Small Songbook (blank)': {
            'Base Price': 400,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Small Wooden Sign': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Smokestick': {
            'Base Price': 2000,
            'Class': 'Special Substances & Items'
        },
        'Sparkle Candle': {
            'Base Price': 1000,
            'Class': 'Special Substances & Items'
        },
        'Spell Component Pouch': {
            'Base Price': 500,
            'Class': 'Tools & Skill Kits'
        },
        'Splint Barding (Large)': {
            'Base Price': 80000,
            'Class': 'Mounts & Related Gear'
        },
        'Splint Barding (Medium)': {
            'Base Price': 40000,
            'Class': 'Mounts & Related Gear'
        },
        'Straw Stuffed Leather Ball': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Sundial': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Sunrod': {
            'Base Price': 200,
            'Class': 'Special Substances & Items'
        },
        'Tavern Table': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Tea Biscuits': {
            'Base Price': 4,
            'Class': 'Food & Drink & Lodging'
        },
        'Thunderstone': {
            'Base Price': 3000,
            'Class': 'Special Substances & Items'
        },
        'Tindertwig': {
            'Base Price': 1000,
            'Class': 'Special Substances & Items'
        },
        'Toffee': {
            'Base Price': 30,
            'Class': 'Food & Drink & Lodging'
        },
        'Tombstone': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Tooth Ointment (25 use flask)': {
            'Base Price': 1000,
            'Class': 'Special Substances & Items'
        },
        'Trained Hireling (per day)': {
            'Base Price': 30,
            'Class': 'Services'
        },
        'Tree (Small & young)': {
            'Base Price': 20,
            'Class': 'Commodities'
        },
        'Truffles': {
            'Base Price': 100,
            'Class': 'Commodities'
        },
        'Tutor (per day)': {
            'Base Price': 1,
            'Class': 'Services'
        },
        'UnCommon Dried Herbs': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'UnCommon Nuts (in shell)': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Uncommon Vegetables': {
            'Base Price': 3,
            'Class': 'Food & Drink & Lodging'
        },
        'Waste Bin (50 gallon)': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Wizard'sSpellbook (Blank)": {
            'Base Price': 1500,
            'Class': 'Tools & Skill Kits'
        },
        'Wood Stain (5 sq ft)': {
            'Base Price': 300,
            'Class': 'Tools & Skill Kits'
        },
        'Wooden Ash Bowl (Fancy)': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Baby Cradle': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Cricket Box': {
            'Base Price': 4,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Foot Massager': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Peg Leg': {
            'Base Price': 70,
            'Class': 'Tools & Skill Kits'
        },
        'Wooden Picture frame (Medium)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Writing Board': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Writing Quills (6)': {
            'Base Price': 2,
            'Class': 'Adventuring Gear/Luxury Items'
        },
    },
    'R': {
        'Albino Rats (Pair)': {
            'Base Price': 2,
            'Class': 'Commodities'
        },
        'Animal (Diminutive) Cage': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Antitoxin': {
            'Base Price': 5000,
            'Class': 'Special Substances & Items'
        },
        "Apothecary's Table": {
            'Base Price': 3000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Beekeeper's Hive": {
            'Base Price': 200,
            'Class': 'Tools & Skill Kits'
        },
        "Beekeeper's Suit": {
            'Base Price': 1000,
            'Class': 'Tools & Skill Kits'
        },
        'Book of Fairy Tales': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Book of General Learning': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Book of Legends': {
            'Base Price': 2500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Book of Recipes': {
            'Base Price': 1500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Chinchilla': {
            'Base Price': 100,
            'Class': 'Commodities'
        },
        "Climber's Kit": {
            'Base Price': 8000,
            'Class': 'Tools & Skill Kits'
        },
        'Cocoa Beans': {
            'Base Price': 300,
            'Class': 'Commodities'
        },
        'Common Gem Eye': {
            'Base Price': 1500,
            'Class': 'Tools & Skill Kits'
        },
        'Common Padded Chair': {
            'Base Price': 800,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Copper Serving Tray': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Copper Wash Basin': {
            'Base Price': 15000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Cosmetics/Theater Makeup Kit': {
            'Base Price': 1000,
            'Class': 'Tools & Skill Kits'
        },
        "Courtier's Outfit": {
            'Base Price': 3000,
            'Class': 'Clothing'
        },
        'Didjeridoo (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        'Fancy Bed Clothing': {
            'Base Price': 100,
            'Class': 'Clothing'
        },
        'Fancy Bedside Table': {
            'Base Price': 1500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Birdbath': {
            'Base Price': 3000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Buckle': {
            'Base Price': 500,
            'Class': 'Clothing'
        },
        'Fancy Casket': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Chest of Drawers': {
            'Base Price': 5000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Cloth Dye (10yd)': {
            'Base Price': 500,
            'Class': 'Tools & Skill Kits'
        },
        'Fancy Decorative Plant': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Fancy Dining Chair': {
            'Base Price': 800,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Dining Table': {
            'Base Price': 5000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Dresser (standing)': {
            'Base Price': 2500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Eating Utensils': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Festival Costume': {
            'Base Price': 2500,
            'Class': 'Clothing'
        },
        'Fancy Foot Stool': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Gloves': {
            'Base Price': 100,
            'Class': 'Clothing'
        },
        'Fancy Hat/Headpiece': {
            'Base Price': 100,
            'Class': 'Clothing'
        },
        'Fancy Hide Blanket': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Kaleidoscope': {
            'Base Price': 8000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Fancy Master's Chair": {
            'Base Price': 10000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Mice': {
            'Base Price': 1,
            'Class': 'Commodities'
        },
        'Fancy Nutcracker': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Pelt (Small)': {
            'Base Price': 300,
            'Class': 'Commodities'
        },
        'Fancy Pelt (Tiny)': {
            'Base Price': 30,
            'Class': 'Commodities'
        },
        'Fancy Pelt/Exotic Hide (Medium)': {
            'Base Price': 3000,
            'Class': 'Commodities'
        },
        'Fancy Perfume (vial)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Pet Bird': {
            'Base Price': 20,
            'Class': 'Commodities'
        },
        'Fancy Pillow': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Plate Cabinet (standing)': {
            'Base Price': 5000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Serving Bowl': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Smoking Pipe': {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Stained Glass Work (per sq ft)': {
            'Base Price': 2000,
            'Class': 'Services'
        },
        'Fancy Tablecloth': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Toy Doll': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Vanity Table (w/ Mirror)': {
            'Base Price': 80000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Wig': {
            'Base Price': 3000,
            'Class': 'Clothing'
        },
        'Fancy Wooden Toy': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Ferret': {
            'Base Price': 30,
            'Class': 'Commodities'
        },
        'Fife (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Fine Wine (bottle)': {
            'Base Price': 1000,
            'Class': 'Food & Drink & Lodging'
        },
        'Fishbowl': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fizzle Stones (12)': {
            'Base Price': 500,
            'Class': 'Special Substances & Items'
        },
        'Flask Olive oil': {
            'Base Price': 100,
            'Class': 'Food & Drink & Lodging'
        },
        'Four Leaf Clover': {
            'Base Price': 2,
            'Class': 'Commodities'
        },
        'Full Plate Barding (Large)': {
            'Base Price': 600000,
            'Class': 'Mounts & Related Gear'
        },
        'Full Plate Barding (Medium)': {
            'Base Price': 300000,
            'Class': 'Mounts & Related Gear'
        },
        'Galley': {
            'Base Price': 3000000,
            'Class': 'Transport'
        },
        'Grand Book of Songs (100)': {
            'Base Price': 5000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Grand Cage Wagon': {
            'Base Price': 80000,
            'Class': 'Transport'
        },
        'Grand Curtains': {
            'Base Price': 300,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Grappling Hook': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Hair Removal Ointment': {
            'Base Price': 300,
            'Class': 'Special Substances & Items'
        },
        'Heavy Warhorse': {
            'Base Price': 40000,
            'Class': 'Mounts & Related Gear'
        },
        'Holy Symbol (Silver)': {
            'Base Price': 2500,
            'Class': 'Tools & Skill Kits'
        },
        'Hookah': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Hourglass': {
            'Base Price': 2500,
            'Class': 'Tools & Skill Kits'
        },
        'Hourglass (1 day)': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Hourglass (1 hour)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Hurdy Gurdy (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        'Ink (1 oz vial)': {
            'Base Price': 800,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Ink Pen': {
            'Base Price': 10,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Iron Bed': {
            'Base Price': 20000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Jade Dice (Pair)': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Large Book of Songs (50)': {
            'Base Price': 3000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Light Warhorse': {
            'Base Price': 15000,
            'Class': 'Mounts & Related Gear'
        },
        'Llama': {
            'Base Price': 1000,
            'Class': 'Transport'
        },
        'Lock (Good)': {
            'Base Price': 8000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        # 'Longship': {'Base Price': 1000000, 'Class': 'Transport'},
        'Lute (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Magnifying Glass': {
            'Base Price': 10000,
            'Class': 'Tools & Skill Kits'
        },
        'Manacles (masterwork)': {
            'Base Price': 5000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Mandolin (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Masterwork Tool': {
            'Base Price': 5000,
            'Class': 'Tools & Skill Kits'
        },
        'Maze Board (w/ marble)': {
            'Base Price': 50,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Metal Face Mask': {
            'Base Price': 5000,
            'Class': 'Clothing'
        },
        'Mink': {
            'Base Price': 50,
            'Class': 'Commodities'
        },
        'Mongoose': {
            'Base Price': 100,
            'Class': 'Commodities'
        },
        'Mood Stone Headpiece': {
            'Base Price': 3500,
            'Class': 'Special Substances & Items'
        },
        'Mood Stone Orb': {
            'Base Price': 1500,
            'Class': 'Special Substances & Items'
        },
        'Mood Stone Pendant': {
            'Base Price': 1500,
            'Class': 'Special Substances & Items'
        },
        'Mood Stone Ring': {
            'Base Price': 1000,
            'Class': 'Special Substances & Items'
        },
        'Mouth Soap (12)': {
            'Base Price': 500,
            'Class': 'Special Substances & Items'
        },
        'Music Box (Common)': {
            'Base Price': 1500,
            'Class': 'Musical Instrument'
        },
        'Musical Instrument (masterwork)': {
            'Base Price': 10000,
            'Class': 'Tools & Skill Kits'
        },
        'Noble Nanny (per day)': {
            'Base Price': 10,
            'Class': 'Services'
        },
        'Noble Tutor (per day)': {
            'Base Price': 30,
            'Class': 'Services'
        },
        "Noble's Outfit": {
            'Base Price': 7500,
            'Class': 'Clothing'
        },
        'Organ Box (Fancy)': {
            'Base Price': 800,
            'Class': 'Musical Instrument'
        },
        'Paper (sheet)': {
            'Base Price': 40,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Plates (Fancy) set of 4': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Poet's Blank Book": {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Rain Stick (Common)': {
            'Base Price': 500,
            'Class': 'Musical Instrument'
        },
        'Rare/Import Dried Herbs': {
            'Base Price': 100,
            'Class': 'Commodities'
        },
        'Recorder (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Riding Dog': {
            'Base Price': 15000,
            'Class': 'Mounts & Related Gear'
        },
        'Roundabout': {
            'Base Price': 3000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Sarod': {
            'Base Price': 2000,
            'Class': 'Musical Instrument'
        },
        'Sarod (Common)': {
            'Base Price': 1500,
            'Class': 'Musical Instrument'
        },
        "Scholar's Bed": {
            'Base Price': 4000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Set of Mahjong Tiles': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Shadow Lantern': {
            'Base Price': 2500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Shawm (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Sideshow Cart': {
            'Base Price': 65000,
            'Class': 'Transport'
        },
        'Signet Ring': {
            'Base Price': 500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Silver Serving Tray': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Singing Bowl w/ accessories (Common)': {
            'Base Price': 1500,
            'Class': 'Musical Instrument'
        },
        'Sitar (Common)': {
            'Base Price': 1500,
            'Class': 'Musical Instrument'
        },
        'Small Book of Songs (20)': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Spectacles': {
            'Base Price': 80000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Standing Mirror': {
            'Base Price': 30000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Stone Cricket Box': {
            'Base Price': 30,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Tanglefoot Bag': {
            'Base Price': 5000,
            'Class': 'Special Substances & Items'
        },
        'Tarantula': {
            'Base Price': 3,
            'Class': 'Commodities'
        },
        'Tea Service Set': {
            'Base Price': 1500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Teeth (demihuman) per tooth': {
            'Base Price': 80,
            'Class': 'Tools & Skill Kits'
        },
        'Teeth (humanoid) per tooth': {
            'Base Price': 10,
            'Class': 'Tools & Skill Kits'
        },
        'Therapeutic Massage': {
            'Base Price': 20,
            'Class': 'Services'
        },
        "Thieves' Tools": {
            'Base Price': 3000,
            'Class': 'Tools & Skill Kits'
        },
        'Tinted Spectacles': {
            'Base Price': 85000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Uncommon fresh Fruit': {
            'Base Price': 5,
            'Class': 'Food & Drink & Lodging'
        },
        'Vanity Mirror': {
            'Base Price': 5000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Warpony': {
            'Base Price': 10000,
            'Class': 'Mounts & Related Gear'
        },
        'Wooden Fortune Wheel': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Moon Calendar': {
            'Base Price': 100,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Wooden Picture frame (Large)': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Xylophone (Common)': {
            'Base Price': 1500,
            'Class': 'Musical Instrument'
        },
    },
    'E': {
        "Alchemist's Lab": {
            'Base Price': 50000,
            'Class': 'Tools & Skill Kits'
        },
        'Baboon': {
            'Base Price': 2000,
            'Class': 'Commodities'
        },
        'Boa Constrictor': {
            'Base Price': 1000,
            'Class': 'Commodities'
        },
        'Bonzai Tree (Tiny to Small)': {
            'Base Price': 10,
            'Class': 'Commodities'
        },
        'Canopy Bed': {
            'Base Price': 35000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Carnival Kaleidoscope': {
            'Base Price': 20000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Carnival Mirror (standing)': {
            'Base Price': 35000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Clockwork Toy': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Didjeridoo (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Everburning Torch': {
            'Base Price': 11000,
            'Class': 'Special Substances & Items'
        },
        'Exotic Perfume (vial)': {
            'Base Price': 2000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Exotic Saddle (Military)': {
            'Base Price': 6000,
            'Class': 'Mounts & Related Gear'
        },
        'Exotic Saddle (Pack)': {
            'Base Price': 1500,
            'Class': 'Mounts & Related Gear'
        },
        'Exotic Saddle (Riding)': {
            'Base Price': 3000,
            'Class': 'Mounts & Related Gear'
        },
        'Exotic/Rare Meat (chunk)': {
            'Base Price': 500,
            'Class': 'Food & Drink & Lodging'
        },
        'Fancy Caravan Wagon': {
            'Base Price': 125000,
            'Class': 'Transport'
        },
        'Fancy Gem Eye': {
            'Base Price': 5000,
            'Class': 'Tools & Skill Kits'
        },
        'Fancy Gnomish Cukoo Clock': {
            'Base Price': 200000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Padded Chair': {
            'Base Price': 2500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fancy Pelt/Exotic Hide (large)': {
            'Base Price': 10000,
            'Class': 'Commodities'
        },
        "Fancy Performer's Cart": {
            'Base Price': 80000,
            'Class': 'Transport'
        },
        'Fancy Pet Lizard': {
            'Base Price': 30,
            'Class': 'Commodities'
        },
        'Fancy Puppet': {
            'Base Price': 200,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Fine Leather Mask': {
            'Base Price': 500,
            'Class': 'Clothing'
        },
        'Ginseng Root': {
            'Base Price': 300,
            'Class': 'Commodities'
        },
        'Gnomish Crank Whistle': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Gnomish Cutting Shears': {
            'Base Price': 8000,
            'Class': 'Tools & Skill Kits'
        },
        'Gnomish Fire Crank': {
            'Base Price': 1500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Gnomish Gear Clock': {
            'Base Price': 120000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Gnomish Heat Lantern': {
            'Base Price': 2500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Gnomish Meat Grinder': {
            'Base Price': 1500,
            'Class': 'Tools & Skill Kits'
        },
        'Hurdy Gurdy (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Lock (Amazing)': {
            'Base Price': 15000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        "Masterwork Thieves' Tools": {
            'Base Price': 10000,
            'Class': 'Tools & Skill Kits'
        },
        'Monkey': {
            'Base Price': 500,
            'Class': 'Commodities'
        },
        'Music Box (masterwork)': {
            'Base Price': 30000,
            'Class': 'Musical Instrument'
        },
        'Noble Chest of Drawers': {
            'Base Price': 25000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Organ Box (masterwork)': {
            'Base Price': 20000,
            'Class': 'Musical Instrument'
        },
        'Peacock': {
            'Base Price': 5,
            'Class': 'Commodities'
        },
        'Portable Ram': {
            'Base Price': 1000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Rain Stick (masterwork)': {
            'Base Price': 10000,
            'Class': 'Musical Instrument'
        },
        'Rare Pet Bird': {
            'Base Price': 500,
            'Class': 'Commodities'
        },
        'Rare/Exotic Decorative Plant': {
            'Base Price': 200,
            'Class': 'Commodities'
        },
        'Royal Gnomish Cukoo Clock': {
            'Base Price': 300000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Royal Outfit': {
            'Base Price': 20000,
            'Class': 'Clothing'
        },
        'Royal Vanity Table (w/ Mirror)': {
            'Base Price': 150000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Sarod (masterwork)': {
            'Base Price': 30000,
            'Class': 'Musical Instrument'
        },
        'Singing Bowl w/ accessories (masterwork)': {
            'Base Price': 30000,
            'Class': 'Musical Instrument'
        },
        'Sitar (masterwork)': {
            'Base Price': 30000,
            'Class': 'Musical Instrument'
        },
        'Spyglass': {
            'Base Price': 100000,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Stone Moon Calendar': {
            'Base Price': 1500,
            'Class': 'Adventuring Gear/Luxury Items'
        },
        'Sugar Glider': {
            'Base Price': 100,
            'Class': 'Commodities'
        },
        'Vanilla Beans': {
            'Base Price': 100,
            'Class': 'Commodities'
        },
        # 'Warship': {'Base Price': 2500000, 'Class': 'Transport'},
        'Water Clock': {
            'Base Price': 100000,
            'Class': 'Tools & Skill Kits'
        },
        'Xylophone (masterwork)': {
            'Base Price': 30000,
            'Class': 'Musical Instrument'
        },
    },
}
