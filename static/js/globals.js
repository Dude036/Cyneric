let DEBUG = true;
let latest_store = 0;
let latest_table = 0;
let latest_list = 0;
let latest_monster = 0;
let latest_monster_rows = 0;
let latest_monster_trait = 0;
let latest_monster_spell = 0;
let latest_monster_spell_row = 0;
let latest_monster_spell_col = 0;
let latest_monster_action = 0;
let latest_hazard = 0;
let latest_hazard_trait = 0;
let latest_hazard_custom = 0;
let latest_divider = 0;
let latest_paragraph = 0;

// Export Variables
let export_counter = 0;

let PATHFINDER_2_STATS = ['HP', 'Speed', 'Size', 'AC', 'Fortitude Save', 'Will Save', 'Reflex Save', 'Skills', 'Recall Knowledge', 'Damage Immunities', 'Damage Resistances', 'Damage Weakness', 'Senses', 'Languages']
let PATHFINDER_1_STATS = ['HP', 'Speed', 'Size', 'AC', 'Touch AC', 'Flat AC', 'CMD', 'CMB', 'Fortitude Save', 'Will Save', 'Reflex Save', 'Skills', 'Damage Immunities', 'Damage Resistances', 'Damage Weakness', 'Senses', 'Languages']
let DND_5_STATS = ['HP', 'Speed', 'Size', 'AC', 'STR Save', 'DEX Save', 'CON Save', 'WIS Save', 'INT Save', 'CHA Save', 'Skills', 'Damage Immunities', 'Damage Resistances', 'Damage Weakness', 'Senses', 'Languages']


/*******************************************************************************************************/
/* HELPER FUNCTIONS ************************************************************************************/
/*******************************************************************************************************/


/**Convert Text to paragraphed HTML
 * @param text The text to HTMLify
 * @return HTMLified text
 */
function convert_text(text) {
  return '<p>' + text.split('\n').join('</p><p>') + '</p>'
}


/**Reavers the convert text function into paragraphs
 * @param text The text to normalize
 * @return Normal text
 */
function deconvert_text(text) {
  if (text.length == 0) { return text; }
  return text.substring(3, text.length - 4).split('</p><p>').join('\n');
}


/**Validate id string passed in is Numeric
 * @param value Number
 * @return True if a number
 */
function is_numeric(value) {
  return /^-?\d+$/.test(value);
}


/**Convert Stat to modifier
 * @param stat Stat
 * @return Modifier
 */
function get_mod(stat) {
  var val = Math.floor(parseInt(stat) / 2) - 5;
  return (val > 0) ? '+' + val : val;
}


/** Get uuid
 * @returns random uuid
 */
function get_uuid() {
  return crypto.randomUUID();
}


/**Incriment the counter for editor items 
 * @param name of the thing to incriment
 * @return number to add to ID
 */
function incriment_item_counter(name) {
  if (name === 'Store') {
    return ++latest_store;
  } else if (name === 'Table') {
    return ++latest_table;
  } else if (name === 'List') {
    return ++latest_list;
  } else if (/Monster\d/.test(name)) {
    return ++latest_monster;
  } else if (name === 'Hazard2') {
    return ++latest_hazard;
  } else if (name === 'Divider') {
    return ++latest_divider;
  } else if (name === 'Paragraph') {
    return ++latest_paragraph;
  } else {
    return NaN;
  }
}
