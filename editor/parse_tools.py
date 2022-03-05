import bs4
import re
from urllib import parse


spells_5etools_by_source = {
    "abi-dalzim's horrid wilting": "abi-dalzim%27s%20horrid%20wilting_xge",
    "absorb elements": "absorb%20elements_xge",
    "acid splash": "acid%20splash_phb",
    "acid stream": "acid%20stream_ua2020spellsandmagictattoos",
    "aganazzar's scorcher": "aganazzar%27s%20scorcher_xge",
    "aid": "aid_phb",
    "alarm": "alarm_phb",
    "alter self": "alter%20self_phb",
    "animal friendship": "animal%20friendship_phb",
    "animal messenger": "animal%20messenger_phb",
    "animal shapes": "animal%20shapes_phb",
    "animate dead": "animate%20dead_phb",
    "animate objects": "animate%20objects_phb",
    "antilife shell": "antilife%20shell_phb",
    "antimagic field": "antimagic%20field_phb",
    "antipathy/sympathy": "antipathy/sympathy_phb",
    "arcane eye": "arcane%20eye_phb",
    "arcane gate": "arcane%20gate_phb",
    "arcane hacking (ua)": "arcane%20hacking%20%28ua%29_uamodernmagic",
    "arcane lock": "arcane%20lock_phb",
    "arcane weapon": "arcane%20weapon_uaartificerrevisited",
    "armor of agathys": "armor%20of%20agathys_phb",
    "arms of hadar": "arms%20of%20hadar_phb",
    "ashardalon's stride": "ashardalon%27s%20stride_ftd",
    "astral projection": "astral%20projection_phb",
    "augury": "augury_phb",
    "aura of life": "aura%20of%20life_phb",
    "aura of purity": "aura%20of%20purity_phb",
    "aura of vitality": "aura%20of%20vitality_phb",
    "awaken": "awaken_phb",
    "bane": "bane_phb",
    "banishing smite": "banishing%20smite_phb",
    "banishment": "banishment_phb",
    "barkskin": "barkskin_phb",
    "beacon of hope": "beacon%20of%20hope_phb",
    "beast bond": "beast%20bond_xge",
    "beast sense": "beast%20sense_phb",
    "bestow curse": "bestow%20curse_phb",
    "bigby's hand": "bigby%27s%20hand_phb",
    "blade barrier": "blade%20barrier_phb",
    "blade of disaster": "blade%20of%20disaster_tce",
    "blade ward": "blade%20ward_phb",
    "bless": "bless_phb",
    "blight": "blight_phb",
    "blinding smite": "blinding%20smite_phb",
    "blindness/deafness": "blindness/deafness_phb",
    "blink": "blink_phb",
    "blur": "blur_phb",
    "bones of the earth": "bones%20of%20the%20earth_xge",
    "booming blade": "booming%20blade_tce",
    "branding smite": "branding%20smite_phb",
    "burning hands": "burning%20hands_phb",
    "call lightning": "call%20lightning_phb",
    "calm emotions": "calm%20emotions_phb",
    "catapult": "catapult_xge",
    "catnap": "catnap_xge",
    "cause fear": "cause%20fear_xge",
    "cause fear (ua)": "cause%20fear%20%28ua%29_uastarterspells",
    "ceremony": "ceremony_xge",
    "ceremony (ua)": "ceremony%20%28ua%29_uastarterspells",
    "chain lightning": "chain%20lightning_phb",
    "chaos bolt": "chaos%20bolt_xge",
    "chaos bolt (ua)": "chaos%20bolt%20%28ua%29_uastarterspells",
    "charm monster": "charm%20monster_xge",
    "charm person": "charm%20person_phb",
    "chill touch": "chill%20touch_phb",
    "chromatic orb": "chromatic%20orb_phb",
    "circle of death": "circle%20of%20death_phb",
    "circle of power": "circle%20of%20power_phb",
    "clairvoyance": "clairvoyance_phb",
    "clone": "clone_phb",
    "cloud of daggers": "cloud%20of%20daggers_phb",
    "cloudkill": "cloudkill_phb",
    "color spray": "color%20spray_phb",
    "command": "command_phb",
    "commune": "commune_phb",
    "commune with city (ua)": "commune%20with%20city%20%28ua%29_uamodernmagic",
    "commune with nature": "commune%20with%20nature_phb",
    "compelled duel": "compelled%20duel_phb",
    "comprehend languages": "comprehend%20languages_phb",
    "compulsion": "compulsion_phb",
    "cone of cold": "cone%20of%20cold_phb",
    "confusion": "confusion_phb",
    "conjure animals": "conjure%20animals_phb",
    "conjure barlgura (ua)": "conjure%20barlgura%20%28ua%29_uathatoldblackmagic",
    "conjure barrage": "conjure%20barrage_phb",
    "conjure celestial": "conjure%20celestial_phb",
    "conjure elemental": "conjure%20elemental_phb",
    "conjure fey": "conjure%20fey_phb",
    "conjure hezrou (ua)": "conjure%20hezrou%20%28ua%29_uathatoldblackmagic",
    "conjure knowbot (ua)": "conjure%20knowbot%20%28ua%29_uamodernmagic",
    "conjure lesser demon (ua)": "conjure%20lesser%20demon%20%28ua%29_uathatoldblackmagic",
    "conjure minor elementals": "conjure%20minor%20elementals_phb",
    "conjure shadow demon (ua)": "conjure%20shadow%20demon%20%28ua%29_uathatoldblackmagic",
    "conjure volley": "conjure%20volley_phb",
    "conjure vrock (ua)": "conjure%20vrock%20%28ua%29_uathatoldblackmagic",
    "conjure woodland beings": "conjure%20woodland%20beings_phb",
    "contact other plane": "contact%20other%20plane_phb",
    "contagion": "contagion_phb",
    "contingency": "contingency_phb",
    "continual flame": "continual%20flame_phb",
    "control flames": "control%20flames_xge",
    "control water": "control%20water_phb",
    "control weather": "control%20weather_phb",
    "control winds": "control%20winds_xge",
    "cordon of arrows": "cordon%20of%20arrows_phb",
    "counterspell": "counterspell_phb",
    "create bonfire": "create%20bonfire_xge",
    "create food and water": "create%20food%20and%20water_phb",
    "create homunculus": "create%20homunculus_xge",
    "create magen": "create%20magen_idrotf",
    "create or destroy water": "create%20or%20destroy%20water_phb",
    "create undead": "create%20undead_phb",
    "creation": "creation_phb",
    "crown of madness": "crown%20of%20madness_phb",
    "crown of stars": "crown%20of%20stars_xge",
    "crusader's mantle": "crusader%27s%20mantle_phb",
    "cure wounds": "cure%20wounds_phb",
    "dancing lights": "dancing%20lights_phb",
    "danse macabre": "danse%20macabre_xge",
    "dark star": "dark%20star_egw",
    "darkness": "darkness_phb",
    "darkvision": "darkvision_phb",
    "dawn": "dawn_xge",
    "daylight": "daylight_phb",
    "death ward": "death%20ward_phb",
    "delayed blast fireball": "delayed%20blast%20fireball_phb",
    "demiplane": "demiplane_phb",
    "destructive wave": "destructive%20wave_phb",
    "detect evil and good": "detect%20evil%20and%20good_phb",
    "detect magic": "detect%20magic_phb",
    "detect poison and disease": "detect%20poison%20and%20disease_phb",
    "detect thoughts": "detect%20thoughts_phb",
    "digital phantom (ua)": "digital%20phantom%20%28ua%29_uamodernmagic",
    "dimension door": "dimension%20door_phb",
    "disguise self": "disguise%20self_phb",
    "disintegrate": "disintegrate_phb",
    "dispel evil and good": "dispel%20evil%20and%20good_phb",
    "dispel magic": "dispel%20magic_phb",
    "dissonant whispers": "dissonant%20whispers_phb",
    "distort value": "distort%20value_ai",
    "divination": "divination_phb",
    "divine favor": "divine%20favor_phb",
    "divine word": "divine%20word_phb",
    "dominate beast": "dominate%20beast_phb",
    "dominate monster": "dominate%20monster_phb",
    "dominate person": "dominate%20person_phb",
    "draconic transformation": "draconic%20transformation_ua2021draconicoptions",
    "dragon's breath": "dragon%27s%20breath_xge",
    "drawmij's instant summons": "drawmij%27s%20instant%20summons_phb",
    "dream": "dream_phb",
    "dream of the blue veil": "dream%20of%20the%20blue%20veil_tce",
    "druid grove": "druid%20grove_xge",
    "druidcraft": "druidcraft_phb",
    "dust devil": "dust%20devil_xge",
    "earth tremor": "earth%20tremor_xge",
    "earthbind": "earthbind_xge",
    "earthquake": "earthquake_phb",
    "ego whip": "ego%20whip_uafighterroguewizard",
    "eldritch blast": "eldritch%20blast_phb",
    "elemental bane": "elemental%20bane_xge",
    "elemental weapon": "elemental%20weapon_phb",
    "encode thoughts": "encode%20thoughts_ggr",
    "enemies abound": "enemies%20abound_xge",
    "enervation": "enervation_xge",
    "enhance ability": "enhance%20ability_phb",
    "enlarge/reduce": "enlarge/reduce_phb",
    "ensnaring strike": "ensnaring%20strike_phb",
    "entangle": "entangle_phb",
    "enthrall": "enthrall_phb",
    "erupting earth": "erupting%20earth_xge",
    "etherealness": "etherealness_phb",
    "evard's black tentacles": "evard%27s%20black%20tentacles_phb",
    "expeditious retreat": "expeditious%20retreat_phb",
    "eyebite": "eyebite_phb",
    "fabricate": "fabricate_phb",
    "faerie fire": "faerie%20fire_phb",
    "false life": "false%20life_phb",
    "far step": "far%20step_xge",
    "fast friends": "fast%20friends_ai",
    "fear": "fear_phb",
    "feather fall": "feather%20fall_phb",
    "feeblemind": "feeblemind_phb",
    "feign death": "feign%20death_phb",
    "find familiar": "find%20familiar_phb",
    "find greater steed": "find%20greater%20steed_xge",
    "find steed": "find%20steed_phb",
    "find the path": "find%20the%20path_phb",
    "find traps": "find%20traps_phb",
    "find vehicle (ua)": "find%20vehicle%20%28ua%29_uamodernmagic",
    "finger of death": "finger%20of%20death_phb",
    "fire bolt": "fire%20bolt_phb",
    "fire shield": "fire%20shield_phb",
    "fire storm": "fire%20storm_phb",
    "fireball": "fireball_phb",
    "fizban's platinum shield": "fizban%27s%20platinum%20shield_ua2021draconicoptions",
    "flame arrows": "flame%20arrows_xge",
    "flame blade": "flame%20blade_phb",
    "flame stride": "flame%20stride_ua2021draconicoptions",
    "flame strike": "flame%20strike_phb",
    "flaming sphere": "flaming%20sphere_phb",
    "flesh to stone": "flesh%20to%20stone_phb",
    "flock of familiars": "flock%20of%20familiars_llk",
    "fly": "fly_phb",
    "fog cloud": "fog%20cloud_phb",
    "forbiddance": "forbiddance_phb",
    "forcecage": "forcecage_phb",
    "foresight": "foresight_phb",
    "fortune's favor": "fortune%27s%20favor_egw",
    "freedom of movement": "freedom%20of%20movement_phb",
    "friends": "friends_phb",
    "frost fingers": "frost%20fingers_idrotf",
    "frostbite": "frostbite_xge",
    "galder's speedy courier": "galder%27s%20speedy%20courier_llk",
    "galder's tower": "galder%27s%20tower_llk",
    "gaseous form": "gaseous%20form_phb",
    "gate": "gate_phb",
    "geas": "geas_phb",
    "gentle repose": "gentle%20repose_phb",
    "giant insect": "giant%20insect_phb",
    "gift of alacrity": "gift%20of%20alacrity_egw",
    "gift of gab": "gift%20of%20gab_ai",
    "glibness": "glibness_phb",
    "globe of invulnerability": "globe%20of%20invulnerability_phb",
    "glyph of warding": "glyph%20of%20warding_phb",
    "goodberry": "goodberry_phb",
    "grasping vine": "grasping%20vine_phb",
    "gravity fissure": "gravity%20fissure_egw",
    "gravity sinkhole": "gravity%20sinkhole_egw",
    "grease": "grease_phb",
    "greater invisibility": "greater%20invisibility_phb",
    "greater restoration": "greater%20restoration_phb",
    "green-flame blade": "green-flame%20blade_tce",
    "guardian of faith": "guardian%20of%20faith_phb",
    "guardian of nature": "guardian%20of%20nature_xge",
    "guards and wards": "guards%20and%20wards_phb",
    "guidance": "guidance_phb",
    "guiding bolt": "guiding%20bolt_phb",
    "guiding hand (ua)": "guiding%20hand%20%28ua%29_uastarterspells",
    "gust": "gust_xge",
    "gust of wind": "gust%20of%20wind_phb",
    "hail of thorns": "hail%20of%20thorns_phb",
    "hallow": "hallow_phb",
    "hallucinatory terrain": "hallucinatory%20terrain_phb",
    "hand of radiance (ua)": "hand%20of%20radiance%20%28ua%29_uastarterspells",
    "harm": "harm_phb",
    "haste": "haste_phb",
    "haywire (ua)": "haywire%20%28ua%29_uamodernmagic",
    "heal": "heal_phb",
    "healing elixir (ua)": "healing%20elixir%20%28ua%29_uastarterspells",
    "healing spirit": "healing%20spirit_xge",
    "healing word": "healing%20word_phb",
    "heat metal": "heat%20metal_phb",
    "hellish rebuke": "hellish%20rebuke_phb",
    "heroes' feast": "heroes%27%20feast_phb",
    "heroism": "heroism_phb",
    "hex": "hex_phb",
    "hold monster": "hold%20monster_phb",
    "hold person": "hold%20person_phb",
    "holy aura": "holy%20aura_phb",
    "holy weapon": "holy%20weapon_xge",
    "hunger of hadar": "hunger%20of%20hadar_phb",
    "hunter's mark": "hunter%27s%20mark_phb",
    "hypnotic pattern": "hypnotic%20pattern_phb",
    "ice knife": "ice%20knife_xge",
    "ice storm": "ice%20storm_phb",
    "icingdeath's frost": "icingdeath%27s%20frost_ua2021draconicoptions",
    "id insinuation": "id%20insinuation_uafighterroguewizard",
    "identify": "identify_phb",
    "illusory dragon": "illusory%20dragon_xge",
    "illusory script": "illusory%20script_phb",
    "immolation": "immolation_xge",
    "immovable object": "immovable%20object_egw",
    "imprisonment": "imprisonment_phb",
    "incendiary cloud": "incendiary%20cloud_phb",
    "incite greed": "incite%20greed_ai",
    "infallible relay (ua)": "infallible%20relay%20%28ua%29_uamodernmagic",
    "infernal calling": "infernal%20calling_xge",
    "infestation": "infestation_xge",
    "infestation (ua)": "infestation%20%28ua%29_uastarterspells",
    "inflict wounds": "inflict%20wounds_phb",
    "insect plague": "insect%20plague_phb",
    "intellect fortress": "intellect%20fortress_uafighterroguewizard",
    "investiture of flame": "investiture%20of%20flame_xge",
    "investiture of ice": "investiture%20of%20ice_xge",
    "investiture of stone": "investiture%20of%20stone_xge",
    "investiture of wind": "investiture%20of%20wind_xge",
    "invisibility": "invisibility_phb",
    "invisibility to cameras (ua)": "invisibility%20to%20cameras%20%28ua%29_uamodernmagic",
    "invulnerability": "invulnerability_xge",
    "jim's glowing coin": "jim%27s%20glowing%20coin_ai",
    "jim's magic missile": "jim%27s%20magic%20missile_ai",
    "jump": "jump_phb",
    "knock": "knock_phb",
    "legend lore": "legend%20lore_phb",
    "leomund's secret chest": "leomund%27s%20secret%20chest_phb",
    "leomund's tiny hut": "leomund%27s%20tiny%20hut_phb",
    "lesser restoration": "lesser%20restoration_phb",
    "levitate": "levitate_phb",
    "life transference": "life%20transference_xge",
    "light": "light_phb",
    "lightning arrow": "lightning%20arrow_phb",
    "lightning bolt": "lightning%20bolt_phb",
    "lightning lure": "lightning%20lure_tce",
    "linked glyphs": "linked%20glyphs_aitfr-avi",
    "locate animals or plants": "locate%20animals%20or%20plants_phb",
    "locate creature": "locate%20creature_phb",
    "locate object": "locate%20object_phb",
    "longstrider": "longstrider_phb",
    "maddening darkness": "maddening%20darkness_xge",
    "maelstrom": "maelstrom_xge",
    "mage armor": "mage%20armor_phb",
    "mage hand": "mage%20hand_phb",
    "magic circle": "magic%20circle_phb",
    "magic jar": "magic%20jar_phb",
    "magic missile": "magic%20missile_phb",
    "magic mouth": "magic%20mouth_phb",
    "magic stone": "magic%20stone_xge",
    "magic weapon": "magic%20weapon_phb",
    "magnify gravity": "magnify%20gravity_egw",
    "major image": "major%20image_phb",
    "mass cure wounds": "mass%20cure%20wounds_phb",
    "mass heal": "mass%20heal_phb",
    "mass healing word": "mass%20healing%20word_phb",
    "mass polymorph": "mass%20polymorph_xge",
    "mass suggestion": "mass%20suggestion_phb",
    "maximilian's earthen grasp": "maximilian%27s%20earthen%20grasp_xge",
    "maze": "maze_phb",
    "meld into stone": "meld%20into%20stone_phb",
    "melf's acid arrow": "melf%27s%20acid%20arrow_phb",
    "melf's minute meteors": "melf%27s%20minute%20meteors_xge",
    "mending": "mending_phb",
    "mental barrier": "mental%20barrier_uafighterroguewizard",
    "mental prison": "mental%20prison_xge",
    "message": "message_phb",
    "meteor swarm": "meteor%20swarm_phb",
    "mighty fortress": "mighty%20fortress_xge",
    "mind blank": "mind%20blank_phb",
    "mind sliver": "mind%20sliver_uasorcererandwarlock",
    "mind spike": "mind%20spike_xge",
    "mind thrust": "mind%20thrust_uafighterroguewizard",
    "minor illusion": "minor%20illusion_phb",
    "mirage arcane": "mirage%20arcane_phb",
    "mirror image": "mirror%20image_phb",
    "mislead": "mislead_phb",
    "misty step": "misty%20step_phb",
    "modify memory": "modify%20memory_phb",
    "mold earth": "mold%20earth_xge",
    "moonbeam": "moonbeam_phb",
    "mordenkainen's faithful hound": "mordenkainen%27s%20faithful%20hound_phb",
    "mordenkainen's magnificent mansion": "mordenkainen%27s%20magnificent%20mansion_phb",
    "mordenkainen's private sanctum": "mordenkainen%27s%20private%20sanctum_phb",
    "mordenkainen's sword": "mordenkainen%27s%20sword_phb",
    "motivational speech": "motivational%20speech_ai",
    "move earth": "move%20earth_phb",
    "nathair's mischief": "nathair%27s%20mischief_ua2021draconicoptions",
    "negative energy flood": "negative%20energy%20flood_xge",
    "nondetection": "nondetection_phb",
    "nystul's magic aura": "nystul%27s%20magic%20aura_phb",
    "on/off (ua)": "on/off%20%28ua%29_uamodernmagic",
    "otherworldly form": "otherworldly%20form_ua2020spellsandmagictattoos",
    "otiluke's freezing sphere": "otiluke%27s%20freezing%20sphere_phb",
    "otiluke's resilient sphere": "otiluke%27s%20resilient%20sphere_phb",
    "otto's irresistible dance": "otto%27s%20irresistible%20dance_phb",
    "pass without trace": "pass%20without%20trace_phb",
    "passwall": "passwall_phb",
    "phantasmal force": "phantasmal%20force_phb",
    "phantasmal killer": "phantasmal%20killer_phb",
    "phantom steed": "phantom%20steed_phb",
    "planar ally": "planar%20ally_phb",
    "planar binding": "planar%20binding_phb",
    "plane shift": "plane%20shift_phb",
    "plant growth": "plant%20growth_phb",
    "poison spray": "poison%20spray_phb",
    "polymorph": "polymorph_phb",
    "power word heal": "power%20word%20heal_phb",
    "power word kill": "power%20word%20kill_phb",
    "power word pain": "power%20word%20pain_xge",
    "power word stun": "power%20word%20stun_phb",
    "prayer of healing": "prayer%20of%20healing_phb",
    "prestidigitation": "prestidigitation_phb",
    "primal savagery": "primal%20savagery_xge",
    "primal savagery (ua)": "primal%20savagery%20%28ua%29_uastarterspells",
    "primordial ward": "primordial%20ward_xge",
    "prismatic spray": "prismatic%20spray_phb",
    "prismatic wall": "prismatic%20wall_phb",
    "produce flame": "produce%20flame_phb",
    "programmed illusion": "programmed%20illusion_phb",
    "project image": "project%20image_phb",
    "protection from ballistics (ua)": "protection%20from%20ballistics%20%28ua%29_uamodernmagic",
    "protection from energy": "protection%20from%20energy_phb",
    "protection from evil and good": "protection%20from%20evil%20and%20good_phb",
    "protection from poison": "protection%20from%20poison_phb",
    "psionic blast": "psionic%20blast_uafighterroguewizard",
    "psychic crush": "psychic%20crush_uafighterroguewizard",
    "psychic scream": "psychic%20scream_xge",
    "pulse wave": "pulse%20wave_egw",
    "puppet (ua)": "puppet%20%28ua%29_uastarterspells",
    "purify food and drink": "purify%20food%20and%20drink_phb",
    "pyrotechnics": "pyrotechnics_xge",
    "raise dead": "raise%20dead_phb",
    "rary's telepathic bond": "rary%27s%20telepathic%20bond_phb",
    "raulothim's psychic lance": "raulothim%27s%20psychic%20lance_ua2021draconicoptions",
    "ravenous void": "ravenous%20void_egw",
    "ray of enfeeblement": "ray%20of%20enfeeblement_phb",
    "ray of frost": "ray%20of%20frost_phb",
    "ray of sickness": "ray%20of%20sickness_phb",
    "reality break": "reality%20break_egw",
    "regenerate": "regenerate_phb",
    "reincarnate": "reincarnate_phb",
    "remote access (ua)": "remote%20access%20%28ua%29_uamodernmagic",
    "remove curse": "remove%20curse_phb",
    "resistance": "resistance_phb",
    "resurrection": "resurrection_phb",
    "reverse gravity": "reverse%20gravity_phb",
    "revivify": "revivify_phb",
    "rime's binding ice": "rime%27s%20binding%20ice_ftd",
    "rope trick": "rope%20trick_phb",
    "sacred flame": "sacred%20flame_phb",
    "sanctuary": "sanctuary_phb",
    "sapping sting": "sapping%20sting_egw",
    "scatter": "scatter_xge",
    "scorching ray": "scorching%20ray_phb",
    "scrying": "scrying_phb",
    "searing smite": "searing%20smite_phb",
    "see invisibility": "see%20invisibility_phb",
    "seeming": "seeming_phb",
    "sending": "sending_phb",
    "sense emotion (ua)": "sense%20emotion%20%28ua%29_uastarterspells",
    "sequester": "sequester_phb",
    "shadow blade": "shadow%20blade_xge",
    "shadow of moil": "shadow%20of%20moil_xge",
    "shape water": "shape%20water_xge",
    "shapechange": "shapechange_phb",
    "shatter": "shatter_phb",
    "shield": "shield_phb",
    "shield of faith": "shield%20of%20faith_phb",
    "shillelagh": "shillelagh_phb",
    "shocking grasp": "shocking%20grasp_phb",
    "shutdown (ua)": "shutdown%20%28ua%29_uamodernmagic",
    "sickening radiance": "sickening%20radiance_xge",
    "silence": "silence_phb",
    "silent image": "silent%20image_phb",
    "simulacrum": "simulacrum_phb",
    "skill empowerment": "skill%20empowerment_xge",
    "skywrite": "skywrite_xge",
    "sleep": "sleep_phb",
    "sleet storm": "sleet%20storm_phb",
    "slow": "slow_phb",
    "snare": "snare_xge",
    "snare (ua)": "snare%20%28ua%29_uastarterspells",
    "snilloc's snowball swarm": "snilloc%27s%20snowball%20swarm_xge",
    "soul cage": "soul%20cage_xge",
    "spare the dying": "spare%20the%20dying_phb",
    "speak with animals": "speak%20with%20animals_phb",
    "speak with dead": "speak%20with%20dead_phb",
    "speak with plants": "speak%20with%20plants_phb",
    "spider climb": "spider%20climb_phb",
    "spike growth": "spike%20growth_phb",
    "spirit guardians": "spirit%20guardians_phb",
    "spirit shroud": "spirit%20shroud_ua2020spellsandmagictattoos",
    "spiritual weapon": "spiritual%20weapon_phb",
    "staggering smite": "staggering%20smite_phb",
    "steel wind strike": "steel%20wind%20strike_xge",
    "stinking cloud": "stinking%20cloud_phb",
    "stone shape": "stone%20shape_phb",
    "stoneskin": "stoneskin_phb",
    "storm of vengeance": "storm%20of%20vengeance_phb",
    "storm sphere": "storm%20sphere_xge",
    "sudden awakening (ua)": "sudden%20awakening%20%28ua%29_uastarterspells",
    "suggestion": "suggestion_phb",
    "summon aberrant spirit": "summon%20aberrant%20spirit_ua2020spellsandmagictattoos",
    "summon aberration": "summon%20aberration_tce",
    "summon beast": "summon%20beast_tce",
    "summon bestial spirit": "summon%20bestial%20spirit_ua2020spellsandmagictattoos",
    "summon celestial": "summon%20celestial_tce",
    "summon celestial spirit": "summon%20celestial%20spirit_ua2020spellsandmagictattoos",
    "summon construct": "summon%20construct_tce",
    "summon draconic spirit": "summon%20draconic%20spirit_ua2021draconicoptions",
    "summon elemental": "summon%20elemental_tce",
    "summon elemental spirit": "summon%20elemental%20spirit_ua2020spellsandmagictattoos",
    "summon fey": "summon%20fey_tce",
    "summon fey spirit": "summon%20fey%20spirit_ua2020spellsandmagictattoos",
    "summon fiend": "summon%20fiend_tce",
    "summon fiendish spirit": "summon%20fiendish%20spirit_ua2020spellsandmagictattoos",
    "summon greater demon": "summon%20greater%20demon_xge",
    "summon lesser demons": "summon%20lesser%20demons_xge",
    "summon shadow spirit": "summon%20shadow%20spirit_ua2020spellsandmagictattoos",
    "summon shadowspawn": "summon%20shadowspawn_tce",
    "summon undead": "summon%20undead_tce",
    "summon undead spirit": "summon%20undead%20spirit_ua2020spellsandmagictattoos",
    "sunbeam": "sunbeam_phb",
    "sunburst": "sunburst_phb",
    "swift quiver": "swift%20quiver_phb",
    "sword burst": "sword%20burst_tce",
    "symbol": "symbol_phb",
    "synaptic static": "synaptic%20static_xge",
    "synchronicity (ua)": "synchronicity%20%28ua%29_uamodernmagic",
    "system backdoor (ua)": "system%20backdoor%20%28ua%29_uamodernmagic",
    "tasha's caustic brew": "tasha%27s%20caustic%20brew_tce",
    "tasha's hideous laughter": "tasha%27s%20hideous%20laughter_phb",
    "tasha's mind whip": "tasha%27s%20mind%20whip_tce",
    "tasha's otherworldly guise": "tasha%27s%20otherworldly%20guise_tce",
    "telekinesis": "telekinesis_phb",
    "telepathy": "telepathy_phb",
    "teleport": "teleport_phb",
    "teleportation circle": "teleportation%20circle_phb",
    "temple of the gods": "temple%20of%20the%20gods_xge",
    "temporal shunt": "temporal%20shunt_egw",
    "tenser's floating disk": "tenser%27s%20floating%20disk_phb",
    "tenser's transformation": "tenser%27s%20transformation_xge",
    "tether essence": "tether%20essence_egw",
    "thaumaturgy": "thaumaturgy_phb",
    "thorn whip": "thorn%20whip_phb",
    "thought shield": "thought%20shield_uafighterroguewizard",
    "thunder step": "thunder%20step_xge",
    "thunderclap": "thunderclap_xge",
    "thunderous smite": "thunderous%20smite_phb",
    "thunderwave": "thunderwave_phb",
    "tidal wave": "tidal%20wave_xge",
    "time ravage": "time%20ravage_egw",
    "time stop": "time%20stop_phb",
    "tiny servant": "tiny%20servant_xge",
    "toll the dead": "toll%20the%20dead_xge",
    "toll the dead (ua)": "toll%20the%20dead%20%28ua%29_uastarterspells",
    "tongues": "tongues_phb",
    "transmute rock": "transmute%20rock_xge",
    "transport via plants": "transport%20via%20plants_phb",
    "tree stride": "tree%20stride_phb",
    "true polymorph": "true%20polymorph_phb",
    "true resurrection": "true%20resurrection_phb",
    "true seeing": "true%20seeing_phb",
    "true strike": "true%20strike_phb",
    "tsunami": "tsunami_phb",
    "unearthly chorus (ua)": "unearthly%20chorus%20%28ua%29_uastarterspells",
    "unseen servant": "unseen%20servant_phb",
    "vampiric touch": "vampiric%20touch_phb",
    "vicious mockery": "vicious%20mockery_phb",
    "virtue (ua)": "virtue%20%28ua%29_uastarterspells",
    "vitriolic sphere": "vitriolic%20sphere_xge",
    "wall of fire": "wall%20of%20fire_phb",
    "wall of force": "wall%20of%20force_phb",
    "wall of ice": "wall%20of%20ice_phb",
    "wall of light": "wall%20of%20light_xge",
    "wall of sand": "wall%20of%20sand_xge",
    "wall of stone": "wall%20of%20stone_phb",
    "wall of thorns": "wall%20of%20thorns_phb",
    "wall of water": "wall%20of%20water_xge",
    "warding bond": "warding%20bond_phb",
    "warding wind": "warding%20wind_xge",
    "water breathing": "water%20breathing_phb",
    "water walk": "water%20walk_phb",
    "watery sphere": "watery%20sphere_xge",
    "web": "web_phb",
    "weird": "weird_phb",
    "whirlwind": "whirlwind_xge",
    "wild cunning (ua)": "wild%20cunning%20%28ua%29_uastarterspells",
    "wind walk": "wind%20walk_phb",
    "wind wall": "wind%20wall_phb",
    "wish": "wish_phb",
    "witch bolt": "witch%20bolt_phb",
    "word of radiance": "word%20of%20radiance_xge",
    "word of recall": "word%20of%20recall_phb",
    "wrath of nature": "wrath%20of%20nature_xge",
    "wrathful smite": "wrathful%20smite_phb",
    "wristpocket": "wristpocket_egw",
    "zephyr strike": "zephyr%20strike_xge",
    "zephyr strike (ua)": "zephyr%20strike%20%28ua%29_uastarterspells",
    "zone of truth": "zone%20of%20truth_phb"
}


def de_dict(d):
    s = ''
    for k, v in d.items():
        s += k + ' ' + str(v) + ', '
    return s[:-2]


def de_list(l):
    s = ''
    for x in l:
        s += x + ', '
    return s[:-2]


class Creature:
    def __init__(self, name, link):
        self.Name = name
        self.Link = link

        # Add new variables as Empty
        self.Perception = ''
        self.Recall = ''
        self.Source = ''
        self.Speed = ''
        self.Size = ''
        self.Description = ''
        self.Alignment = ''
        self.Traits = []
        self.Languages = []
        self.Skills = {}
        self.Actions = []
        self.Abilities = []
        self.Spells = []
        self.Str = -2
        self.Dex = -2
        self.Con = -2
        self.Wis = -2
        self.Int = -2
        self.Cha = -2
        self.Ac = ''
        self.Hp = -2
        self.Cr = -2
        self.Fort = ''
        self.Ref = ''
        self.Will = ''
        self.Resist = ''
        self.Immune = ''
        self.Weak = ''

    def validate(self):
        state = True
        for key, value in vars(self).items():
            if isinstance(value, str):
                if value == '':
                    print("!! Missing", key)
                    state = False
            elif isinstance(value, int):
                if value == -2:
                    print("!! Missing", key)
                    state = False
            elif isinstance(value, list):
                if len(value) == 0:
                    print("!! Missing", key)
                    state = False
            elif isinstance(value, dict):
                if len(value.keys()) == 0:
                    print("!! Missing", key)
                    state = False
        return state

    def set_from_raw_text(self, text):
        print("\t\tSetting Description")
        match = re.search(r'([a-z\)][A-Z])', text)
        if 'Recall Knowledge' in text:
            if match is None:
                self.Description = text[0 : text.index('Recall Knowledge')]
                self.Description = self.Description.encode(encoding='utf-8', errors='replace')
            else:
                self.Description = text[text.find(match.group(1)) + 1 : text.index('Recall Knowledge')]
            print("\t\tSetting Recall")
            dc = text.find('DC ', text.index('Recall Knowledge'))
            s = text.find('(', text.index('Recall Knowledge'))
            e = text.find(')', text.index('Recall Knowledge'))
            self.Recall = text[s+1 : e] + ': ' + text[dc: dc+5]
        else:
            self.Description = text[0 : text.index('|')]
            r = 10 + self.Cr
            if 'Uncommon' in self.Traits:
                r += 2
            if 'Rare' in self.Traits:
                r += 5
            if 'Unique' in self.Traits:
                r += 10
            self.Recall = '?: DC' + str(r)

    def set_traits(self, uncommon, rare, unique, align, size, traits):
        print("\t\tSetting Traits")
        if uncommon is not None:
            self.Traits.append('Uncommon')
        if rare is not None:
            self.Traits.append('Rare')
        if unique is not None:
            self.Traits.append('Unique')
        if align is not None:
            self.Traits.append(align.text)
            self.Alignment = align.text
        if size is not None:
            self.Traits.append(size.text)
            self.Size = size.text

        for t in traits:
            self.Traits.append(str(t.string))

    def set_source(self, line):
        print("\t\tSetting Source")
        self.Source = line.i.string

    def set_cr(self, line):
        print("\t\tSetting CR")
        self.Cr = int(line)

    def set_perception(self, line):
        print("\t\tSetting Perception")
        self.Perception = line.text.replace('Perception ', '')

    def set_languages(self, line):
        print("\t\tSetting Language")
        self.Languages = [x.strip() for x in re.split(r'[\,\;]', line.text.replace('Languages ', ''))]

    def set_skills(self, line):
        print("\t\tSetting Skills")
        for x in re.split(r'[\,\;]', line.text.replace('Skills ', '')):
            match = re.match(r'\s*(\w+)\s(.*)', x)
            self.Skills[match.group(1)] = match.group(2)

    def set_stats(self, line):
        print("\t\tSetting Stats")
        for x in re.split(r'[\,\;]', line.text):
            match = re.match(r'\s?([\w]{3}) ([\+\-]\d*)', x)
            if match.group(1) == 'Str':
                self.Str = match.group(2)
            elif match.group(1) == 'Dex':
                self.Dex = match.group(2)
            elif match.group(1) == 'Con':
                self.Con = match.group(2)
            elif match.group(1) == 'Int':
                self.Int = match.group(2)
            elif match.group(1) == 'Wis':
                self.Wis = match.group(2)
            elif match.group(1) == 'Cha':
                self.Cha = match.group(2)

    def remaining_parser(self, lines):
        print("\t\tParsing Remaining")
        for line in lines:
            if line.startswith('<span class="hanging-indent">'):
                print('\t\t\tBegin Bulk action parsing')
                self.handle_actions(line)

            elif 'alt="Reaction"' in line:
                print('\t\t\tReaction found. Adding to Abilities')
                self.put_ability(line, -1)
            elif 'alt="Free Action"' in line:
                print('\t\t\tFree Action found. Adding to Abilities')
                self.put_ability(line, 0)
            elif 'alt="Single Action"' in line:
                print('\t\t\tSingle Action found. Adding to Abilities')
                self.put_ability(line, 1)
            elif 'alt="Two Actions"' in line:
                print('\t\t\tTwo Actions found. Adding to Abilities')
                self.put_ability(line, 2)
            elif 'alt="Three Actions"' in line:
                print('\t\t\tThree Actions found. Adding to Abilities')
                self.put_ability(line, 3)

            elif '<b>Items</b>' in line:
                print('\t\t\tItems found. Adding to Items')
            elif '<b>Speed</b>' in line:
                print('\t\t\tSpeed found')
                self.Speed = line[13:]

            elif '<b>AC</b>' in line:
                print('\t\t\tAC and Saves found')
                new_line = bs4.BeautifulSoup(line, 'html.parser')
                match = re.search(r'b>([^<]*)<b', str(new_line))
                if match is None:
                    self.Ac = new_line.text.split('; ')[0][3:]
                    new_line = new_line.text.split('; ')[1]
                else:
                    self.Ac = match[0].strip()
                    new_line = ''.join(str(new_line).split('<b>')[2:]).replace('</b>', '')

                for x in re.split(r'\,', new_line):
                    match = re.match(r'\s*(Fort|Ref|Will) (.*)', x)
                    if match.group(1) == 'Fort':
                        self.Fort = match.group(2)
                    elif match.group(1) == 'Ref':
                        self.Ref = match.group(2)
                    elif match.group(1) == 'Will':
                        self.Will = match.group(2)

            elif '<b>HP</b>' in line:
                new_line = bs4.BeautifulSoup(line, 'html.parser')
                data = re.split(r'\;', new_line.text)
                latest = None
                for d in data:
                    match = re.match(r'\s?(HP|Immunities|Resistances|Weaknesses)\s(.*)', d)
                    if match is None and latest is not None:
                        exec(latest)
                    elif match.group(1) == 'HP':
                        self.Hp = match.group(2)
                        latest = "self.Hp += d"
                    elif match.group(1) == 'Immunities':
                        self.Immune = match.group(2)
                        latest = "self.Immune += d"
                    elif match.group(1) == 'Resistances':
                        self.Resist = match.group(2)
                        latest = "self.Resist += d"
                    elif match.group(1) == 'Weaknesses':
                        self.Weak = match.group(2)
                        latest = "self.Weak += d"

            elif line.startswith('<b>Arcane') or line.startswith('<b>Divine') or line.startswith('<b>Occult') or line.startswith('<b>Primal') or line.startswith('<b>Monk') or line.startswith('<b>Champion'):
                print('\t\t\tSpell Work Begins')
                dc = int(line[line.index('DC ')+3 : line.index('DC ')+5])

                data = bs4.BeautifulSoup(line, 'html.parser')
                # print(type(data.find_all('b')[1].next_sibling.next_sibling.next_sibling))
                # print(data.find_all('b')[1].next_sibling.next_sibling.next_sibling)
                data_split = line.split('<b>')
                for line in data_split[2:]:
                    level, spells = line.split('</b>')
                    temp_spell_line = {
                        'Dc': dc,
                        'Uses': level,
                        'List': [],
                    }
                    print('\t\t\t\tProcessing ' + level + ' level spells')
                    spells = bs4.BeautifulSoup(spells, 'html.parser')
                    for link in spells.find_all('a'):
                        print('\t\t\t\t\t' + link.text.title())
                        temp_spell = {
                            'Name': link.text.title(),
                            'Link': "https://2e.aonprd.com/" + link['href'],
                        }
                        temp_spell_line['List'].append(temp_spell)
                    self.Spells.append(temp_spell_line)

            else:
                print('\t\t\tAdding Ability')
                try:
                    temp_ab = {
                        'Name': line[line.index('<b>')+3 : line.index('</b>')]
                    }
                    print('\t\t\t\t' + temp_ab['Name'])
                    if temp_ab['Name'] in ['Critical Success', 'Critical Failure', 'Success', 'Failure']:
                        self.Abilities[-1]['Description'] += line[line.index('</b>'):].strip()
                    else:
                        temp_ab['Description'] = line[line.index('</b>')+4:].strip()
                        self.Abilities.append(temp_ab)
                except Exception as e:
                    print('!! Unparsable Ability:')
                    print(line)

    def put_ability(self, action, cost):
        data = bs4.BeautifulSoup(action, 'html.parser')
        temp_a = {
            'Name': data.b.text.strip(),
            'Text': '<p>' + data.text[len(data.b.text):].strip() + '</p>',
            'Cost': cost

        }
        self.Actions.append(temp_a)

    def handle_actions(self, action):
        data = bs4.BeautifulSoup(action, 'html.parser')
        actions = data.find_all('span', recursive=False)
        for a in actions:
            cost = -2
            action = a.find('span')
            if action is None:
                cost = "1 Action"
            elif action['title'] == "Reaction":
                cost = "Reaction"
            elif action['title'] == "Free Action":
                cost = "Free"
            elif action['title'] == "Single Action":
                cost = "1 Action"
            elif action['title'] == "Two Actions":
                cost = "2 Action"
            elif action['title'] == "Three Actions":
                cost = "3 Action"
            print('\t\t\t\tAction: ' + a.b.text)
            temp_a = {
                'Name': str(a.b.text),
                'Text': '<p>' + a.text[len(a.b.text):].strip() + '</p>',
                'Cost': cost
            }
            self.Actions.append(temp_a)

    def get_dict(self):
        return self.__dict__


sources_5etools = {
    'ai': 'https://5e.tools/data/bestiary/bestiary-ai.json',
    'aitfr-dn': 'https://5e.tools/data/bestiary/bestiary-aitfr-dn.json',
    'aitfr-fcd': 'https://5e.tools/data/bestiary/bestiary-aitfr-fcd.json',
    'aitfr-isf': 'https://5e.tools/data/bestiary/bestiary-aitfr-isf.json',
    'aitfr-thp': 'https://5e.tools/data/bestiary/bestiary-aitfr-thp.json',
    'bgdia': 'https://5e.tools/data/bestiary/bestiary-bgdia.json',
    'cm': 'https://5e.tools/data/bestiary/bestiary-cm.json',
    'cos': 'https://5e.tools/data/bestiary/bestiary-cos.json',
    'dc': 'https://5e.tools/data/bestiary/bestiary-dc.json',
    'dip': 'https://5e.tools/data/bestiary/bestiary-dip.json',
    'dmg': 'https://5e.tools/data/bestiary/bestiary-dmg.json',
    'dod': 'https://5e.tools/data/bestiary/bestiary-dod.json',
    'egw': 'https://5e.tools/data/bestiary/bestiary-egw.json',
    'erlw': 'https://5e.tools/data/bestiary/bestiary-erlw.json',
    'esk': 'https://5e.tools/data/bestiary/bestiary-esk.json',
    'ftd': 'https://5e.tools/data/bestiary/bestiary-ftd.json',
    'ggr': 'https://5e.tools/data/bestiary/bestiary-ggr.json',
    'gos': 'https://5e.tools/data/bestiary/bestiary-gos.json',
    'hftt': 'https://5e.tools/data/bestiary/bestiary-hftt.json',
    'hol': 'https://5e.tools/data/bestiary/bestiary-hol.json',
    'hotdq': 'https://5e.tools/data/bestiary/bestiary-hotdq.json',
    'idrotf': 'https://5e.tools/data/bestiary/bestiary-idrotf.json',
    'imr': 'https://5e.tools/data/bestiary/bestiary-imr.json',
    'kkw': 'https://5e.tools/data/bestiary/bestiary-kkw.json',
    'llk': 'https://5e.tools/data/bestiary/bestiary-llk.json',
    'lmop': 'https://5e.tools/data/bestiary/bestiary-lmop.json',
    'lr': 'https://5e.tools/data/bestiary/bestiary-lr.json',
    'mabjov': 'https://5e.tools/data/bestiary/bestiary-mabjov.json',
    'mff': 'https://5e.tools/data/bestiary/bestiary-mff.json',
    'mm': 'https://5e.tools/data/bestiary/bestiary-mm.json',
    'mot': 'https://5e.tools/data/bestiary/bestiary-mot.json',
    'mtf': 'https://5e.tools/data/bestiary/bestiary-mtf.json',
    'oota': 'https://5e.tools/data/bestiary/bestiary-oota.json',
    'oow': 'https://5e.tools/data/bestiary/bestiary-oow.json',
    'phb': 'https://5e.tools/data/bestiary/bestiary-phb.json',
    'pota': 'https://5e.tools/data/bestiary/bestiary-pota.json',
    'psa': 'https://5e.tools/data/bestiary/bestiary-ps-a.json',
    'psd': 'https://5e.tools/data/bestiary/bestiary-ps-d.json',
    'psi': 'https://5e.tools/data/bestiary/bestiary-ps-i.json',
    'psk': 'https://5e.tools/data/bestiary/bestiary-ps-k.json',
    'psx': 'https://5e.tools/data/bestiary/bestiary-ps-x.json',
    'psz': 'https://5e.tools/data/bestiary/bestiary-ps-z.json',
    'rmbre': 'https://5e.tools/data/bestiary/bestiary-rmbre.json',
    'rot': 'https://5e.tools/data/bestiary/bestiary-rot.json',
    'rtg': 'https://5e.tools/data/bestiary/bestiary-rtg.json',
    'sads': 'https://5e.tools/data/bestiary/bestiary-sads.json',
    'sdw': 'https://5e.tools/data/bestiary/bestiary-sdw.json',
    'skt': 'https://5e.tools/data/bestiary/bestiary-skt.json',
    'slw': 'https://5e.tools/data/bestiary/bestiary-slw.json',
    'tce': 'https://5e.tools/data/bestiary/bestiary-tce.json',
    'tftyp': 'https://5e.tools/data/bestiary/bestiary-tftyp.json',
    'toa': 'https://5e.tools/data/bestiary/bestiary-toa.json',
    'ttp': 'https://5e.tools/data/bestiary/bestiary-ttp.json',
    'ua2020spellsandmagictattoos': 'https://5e.tools/data/bestiary/bestiary-ua-2020smt.json',
    'ua2020subclassespt2': 'https://5e.tools/data/bestiary/bestiary-ua-20s2.json',
    'ua2020subclassespt5': 'https://5e.tools/data/bestiary/bestiary-ua-20s5.json',
    'ua2021draconicoptions': 'https://5e.tools/data/bestiary/bestiary-ua-2021do.json',
    'ua2021magesofstrixhaven': 'https://5e.tools/data/bestiary/bestiary-ua-2021mos.json',
    'uaartificerrevisited': 'https://5e.tools/data/bestiary/bestiary-ua-ar.json',
    'uaclassfeaturevariants': 'https://5e.tools/data/bestiary/bestiary-ua-cfv.json',
    'uaclericdruidwizard': 'https://5e.tools/data/bestiary/bestiary-ua-cdw.json',
    'vgm': 'https://5e.tools/data/bestiary/bestiary-vgm.json',
    'vrgr': 'https://5e.tools/data/bestiary/bestiary-vrgr.json',
    'wbtw': 'https://5e.tools/data/bestiary/bestiary-wbtw.json',
    'wdh': 'https://5e.tools/data/bestiary/bestiary-wdh.json',
    'wdmm': 'https://5e.tools/data/bestiary/bestiary-wdmm.json',
    'xge': 'https://5e.tools/data/bestiary/bestiary-xge.json'
}


def fix_dict_diff(old, new):
    for key in old.keys():
        if key == '_copy':
            continue
        if key in new.keys():
            new[key] = old[key]
    return new


def modify_title(s):
    if ' Of ' in s:
        s = s.replace(' Of ', ' of ')
    if ' And ' in s:
        s = s.replace(' And ', ' and ')
    if ' The ' in s:
        s = s.replace(' The ', ' the ')
    if '-O\'-' in s:
        s = s.replace('-O\'-', '-o\'-')
    if 'Yuan-Ti' in s:
        s = s.replace('Yuan-Ti', 'Yuan-ti')
    if 'Parasite-Infested' in s:
        s = s.replace('Parasite-Infested', 'Parasite-infested')
    if 'Kuo-Toa' in s:
        s = s.replace('Kuo-Toa', 'Kuo-toa')
    if 'Thri-Kreen' in s:
        s = s.replace('Thri-Kreen', 'Thri-kreen')
    if 'Mend-Nets' in s:
        s = s.replace('Mend-Nets', 'Mend-nets')
    if 'Leuk-O' in s:
        s = s.replace('Leuk-O', 'Leuk-o')
    if 'Su-Monster' in s:
        s = s.replace('Su-Monster', 'Su-monster')
    if 'Ki-Rin' in s:
        s = s.replace('Ki-Rin', 'Ki-rin')
    if 'Tri-Flower' in s:
        s = s.replace('Tri-Flower', 'Tri-flower')
    if 'Play-By-Play' in s:
        s = s.replace('Play-By-Play', 'Play-by-Play')
    if "'S " in s:
        s = s.replace("'S ", "'s ")
    if "Blit'Zen" in s:
        s = s.replace("Blit'Zen", "Blit'zen")
    if "K'Thriss Drow'B" in s:
        s = s.replace("K'Thriss Drow'B", "K'thriss Drow'b")
    if "Bol'Bara" in s:
        s = s.replace("Bol'Bara", "Bol'bara")
    if "F'Yorl" in s:
        s = s.replace("F'Yorl", "F'yorl")
    if "Kith'Rak" in s:
        s = s.replace("Kith'Rak", "Kith'rak")
    if "Graz'Zt" in s:
        s = s.replace("Graz'Zt", "Graz'zt")
    if "Skr'A S'Orsk" in s:
        s = s.replace("Skr'A S'Orsk", "Skr'a S'orsk")
    if 'Aribeth De Tylmarande' in s:
        s = s.replace('Aribeth De Tylmarande', 'Aribeth de Tylmarande')
    if "Crokek'Toeck" in s:
        s = s.replace("Crokek'Toeck", "Crokek'toeck")
    if "D'Avenir" in s:
        s = s.replace("D'Avenir", "d'Avenir")
    if "Druu'Giir" in s:
        s = s.replace("Druu'Giir", "Druu'giir")
    if "Urb'Luu" in s:
        s = s.replace("Urb'Luu", "Urb'luu")
    if "Ur'Gray" in s:
        s = s.replace("Ur'Gray", "Ur'gray")
    if "Uk'Otoa" in s:
        s = s.replace("Uk'Otoa", "Uk'otoa")
    if "Talro'A" in s:
        s = s.replace("Talro'A", "Talro'a")
    if "Pu'Pu" in s:
        s = s.replace("Pu'Pu", "Pu'pu")
    if "O'Tamu" in s:
        s = s.replace("O'Tamu", "O'tamu")
    if "Fel'Rekt" in s:
        s = s.replace("Fel'Rekt", "Fel'rekt")
    if "Grum'Shar" in s:
        s = s.replace("Grum'Shar", "Grum'shar")
    if "Masq'Il'Yr" in s:
        s = s.replace("Masq'Il'Yr", "Masq'il'yr")
    if "Nar'L" in s:
        s = s.replace("Nar'L", "Nar'l")
    if "Al'Chaia" in s:
        s = s.replace("Al'Chaia", "Al'chaia")
    if "N'Ghathrod" in s:
        s = s.replace("N'Ghathrod", "N'ghathrod")
    if "Kol'Daan" in s:
        s = s.replace("Kol'Daan", "Kol'daan")
    if ' Von ' in s:
        s = s.replace(' Von ', ' von ')
    if 'Duloc' in s:
        s = s.replace('Duloc', 'DuLoc')
    if ' Van Der ' in s:
        s = s.replace(' Van Der ', ' van der ')
    if "Brain In Iron" in s:
        s = s.replace("Brain In Iron", "Brain in Iron")
    if "Brain In A Jar" in s:
        s = s.replace("Brain In A Jar", "Brain in a Jar")
    if " Devir" in s:
        s = s.replace(" Devir", " DeVir")
    if 'Ii' in s:
        s = s.replace('Ii', 'II')

    if 'Archon of Redemption' in s:
        s = s.replace('Archon of Redemption', 'Archon Of Redemption')
    if 'Nurvureem, the Dark Lady' in s:
        s = s.replace('Nurvureem, the Dark Lady', 'Nurvureem, The Dark Lady')

    return s


def process_actions_5etools(content, legendary):
    actions = []
    for action in content:
        if 'name' not in action.keys():
            continue
        if len(action['entries']) == 1 and isinstance(action['entries'][0], dict):
            text = de_dict(action['entries'][0])
        elif len(action['entries']) == 1:
            text = de_list(action['entries'])
        else:
            text = str(action['entries'])
        text = text.replace('{@atk mw}', '').replace('{@atk rw}', '').replace('{@atk mw,rw}', '').replace('{@atk rw,mw}', '')
        actions.append({'Name': action['name'], 'Text': text.strip(), 'Legendary': legendary})
    return actions


def get_spell_link(spell_name):
    try:
        return 'https://5e.tools/spells.html#' + spells_5etools_by_source[spell_name.lower()]
    except Exception as e:
        return 'Unable to find in 5e.tools'


def process_spells_5etools(content):
    all_spells = []
    spell_dc = '?'
    if 'headerEntries' in content.keys():
        match = re.search(r"@dc ([0-9]{2})", str(content))
        if match is not None:
            spell_dc = match.group(1)
    if 'daily' in content.keys():
        for uses in content['daily'].keys():
            temp_level = {
                'Uses': uses,
                'Dc': spell_dc,
                'List': []
            }
            for spell in content['daily'][uses]:
                if isinstance(spell, dict):
                    continue
                spell_name = spell.replace('{@spell', '').replace('}', '').strip()
                spell_link = get_spell_link(spell_name)
                temp_level['List'].append({'Name': spell_name.title(), 'Link': spell_link})
            all_spells.append(temp_level)
    if 'will' in content.keys():
        temp_level = {
            'Uses': 'At Will',
            'Dc': spell_dc,
            'List': []
        }
        for cantrip in content['will']:
            if isinstance(cantrip, dict):
                continue
            spell_name = cantrip.replace('{@spell', '').replace('}', '').strip()
            spell_link = get_spell_link(spell_name)
            temp_level['List'].append({'Name': spell_name.title(), 'Link': spell_link})
        all_spells.append(temp_level)
    return all_spells

