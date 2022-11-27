/*********************************
 * Page updates for all elements *
 *********************************/


/**Set a DOM value for import
 * @param dom DOM Id string
 * @param value Value to be set
 */
function set_dom_value(dom, value) {
  var dom_elem = document.getElementById(dom);
  dom_elem.value = value;
}


/**Remove all lower rows in a table
 * @param table_id The id for the Table to delete from
 * @param skip Number of rows to skip when deleting
 */
function remove_table_rows(table_id, skip) {
  var tables = document.getElementById(table_id);
  while (tables.rows.length > skip) {
    // Delete from the end of the table rows
    tables.deleteRow(-1);
  }
}


/**Updates a Small section of the webpage
 * @param new_json Imported JSON object to update the whole page with
 */
function update_page(new_json) {
  // Update page information to reflect the data imported.
  set_dom_value('header', new_json['Name']);
  set_dom_value('description', deconvert_text(new_json['Description']))
  new_json['Data'].forEach(function(data_obj) {
    // Null check
    if (data_obj === null) {return;}

    // Check type for button check, and create object
    if (data_obj['Type'] === 'Store') {
      create_element('Store');
    } else if (data_obj['Type'] === 'Table') {
      create_element('Table');
    } else if (data_obj['Type'] === 'List') {
      create_element('List');
    } else if (data_obj['Type'].startsWith('Monster')) {
      create_element('Monster' + data_obj['Edition']);
    } else if (data_obj['Type'].startsWith('Hazard')) {
      create_element('Hazard2');
    } else if (data_obj['Type'] === 'Divider') {
      create_element('Divider');
    } else if (data_obj['Type'] === 'Paragraph') {
      create_element('Paragraph');
    }

    // Get the last item in the editor and update container from there
    var editor_container = document.getElementById('editor').lastElementChild;
    update_container(data_obj, editor_container.id)
  });
}


/**Updates a Small section of the webpage
 * @param new_json JSON object to update
 * @param container_id ID of the container as retrieved from storage
 */
function update_container(new_json, container_id) {
  if (container_id.startsWith('S')) {
    var content = document.getElementById(container_id).childNodes[1]
    update_owner_container(new_json, content.id);

    var add_special = document.getElementById(container_id + '_SPECIAL')
    var add_blank = document.getElementById(container_id + '_BLANK')
    update_table_container(new_json, content.id, add_blank, add_special);
  } else if (container_id.startsWith('M')) {
    var content = document.getElementById(container_id).childNodes[1]
    update_monster_container(new_json, content.id);
  } else if (container_id.startsWith('T')) {
    var table = document.getElementById(container_id).childNodes[1].childNodes[0]
    set_dom_value(table.id + "_NAME_I", new_json['Name']);

    var content = document.getElementById(container_id).childNodes[1]
    var add_special = document.getElementById(container_id + '_SPECIAL')
    var add_blank = document.getElementById(container_id + '_BLANK')
    update_table_container(new_json, content.id, add_blank, add_special);
  } else if (container_id.startsWith('H')) {
    var content = document.getElementById(container_id).childNodes[1]
    update_hazard_container(new_json, content.id);
  } else if (container_id.startsWith('L')) {
    update_list_container(new_json, container_id);
  } else if (container_id.startsWith('D')) {
    var name = document.getElementById(container_id).childNodes[1]
    set_dom_value(name.id + "_NAME_I", new_json['Name']);
  } else if (container_id.startsWith('P')) {
    var name = document.getElementById(container_id).childNodes[1]
    set_dom_value(name.id + "_TEXT_I", new_json['Text']);
  }
}


/**Updates a owner section of the webpage
 * @param new_json JSON object to update
 * @param container_id ID of the container as retrieved from storage
 */
function update_owner_container(new_json, container_id) {
  if (DEBUG) { console.log("Updating Owner: " + container_id); }
  // Set Owner Elements
  set_dom_value(container_id + '_OWNER_STORE', new_json['Owner']['Store Name']);
  set_dom_value(container_id + '_OWNER_NAME', new_json['Owner']['Name']);
  set_dom_value(container_id + '_OWNER_DESCRIBE', deconvert_text(new_json['Owner']['Description']));
  set_dom_value(container_id + '_OWNER_RACE', new_json['Owner']['Race']);
  set_dom_value(container_id + '_OWNER_GENDER', new_json['Owner']['Gender']);
  set_dom_value(container_id + '_OWNER_AGE', new_json['Owner']['Age']);
  set_dom_value(container_id + '_OWNER_TRAIT_1', new_json['Owner']['Trait 1']);
  set_dom_value(container_id + '_OWNER_TRAIT_2', new_json['Owner']['Trait 2']);
}


/**Updates a monster section of the webpage
 * @param new_json JSON object to update
 * @param container_id ID of the container as retrieved from storage
 */
function update_monster_container(new_json, container_id) {
  if (DEBUG) { console.log("Updating Monster: " + container_id); }

  set_dom_value(container_id + 'R1_NAME', new_json['Name']);
  set_dom_value(container_id + 'R1_CR', new_json['Cr']);
  set_dom_value(container_id + 'R1_XP', new_json['Xp']);
  set_dom_value(container_id + 'R1_ALIGN', new_json['Alignment']);
  set_dom_value(container_id + 'R1_DESCRIBE', deconvert_text(new_json['Description']));

  // Traits
  if (new_json['Edition'] === '2') {
    var trait_list = document.getElementById(container_id + 'R1_TRAITS');
    for (var i = 0; i < new_json['Traits'].length; i++) {
      document.getElementById(container_id + 'R1_TRAIT_ADD').click();
      set_dom_value(trait_list.lastElementChild.childNodes[0].id, new_json['Traits'][i])
    }
  }

  /************************************************************************************************/

  var stat_list;
  if (new_json['Edition'] == '2') {
    stat_list = PATHFINDER_2_STATS;
  } else if (new_json['Edition'] == '1') {
    stat_list = PATHFINDER_1_STATS;
  } else if (new_json['Edition'] == '5') {
    stat_list = DND_5_STATS;
  }

  for (var i = 0; i < stat_list.length; i++) {
    // 5e Saves are checkboxes
    if (/[A-Z]{3} Save/.test(stat_list[i])) {
      if (new_json[stat_list[i]]) {
        document.getElementById(container_id + 'R2_' + stat_list[i].toUpperCase()).checked = true;
      }
    } else {
      set_dom_value(container_id + 'R2_' + stat_list[i].toUpperCase(), new_json[stat_list[i]]);
    }
  }

  /************************************************************************************************/

  var attrib = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'];
  for (var i = 0; i < attrib.length; i++) {
    set_dom_value(container_id + 'R3_' + attrib[i], new_json[attrib[i]]);
  }

  /************************************************************************************************/
  
  var add_action_button = document.getElementById(container_id + 'R4_ACTION_ADD');
  var action_list = document.getElementById(container_id + 'R4_ACTIONS');

  new_json['Actions'].forEach(function(action_obj) {
    add_action_button.click()
    var action_table_id = action_list.lastElementChild.id;

    // Different Edition Additions
    if (new_json['Edition'] == '5') {
      if (action_obj['Legendary']) {
        document.getElementById(action_table_id + '_LEGEND').checked = true
      }
    } else if (new_json['Edition'] == '2') {
      set_dom_value(action_table_id + '_COST', action_obj['Cost'])
    }

    set_dom_value(action_table_id + '_NAME', action_obj['Name'])
    set_dom_value(action_table_id + '_TEXT', action_obj['Text'])
  })

  /************************************************************************************************/

  if (new_json['Spells'].length !== 0) {
    // Add a spell list container
    document.getElementById(container_id + 'R5_SPELL_ADD').click();
    var all_spell_row_buttons = document.querySelectorAll('div[id$=_ROW_ADD]');
    var add_spell_row_button = all_spell_row_buttons[all_spell_row_buttons.length - 1];
    var spell_table = document.querySelector('table[id^=' + container_id + 'R5_LOC]');

    // Add spell list
    new_json['Spells'].forEach(function(spell_obj) {
      add_spell_row_button.click()
      var add_spell_button = document.getElementById(spell_table.lastElementChild.id + '_LIST_ADD');
      var spell_list_container = document.querySelector('div#' + spell_table.lastElementChild.id + '_LIST')

      // Add spell 
      spell_obj['List'].forEach(function(spell_instance) {
        add_spell_button.click();
        var inputs = spell_list_container.lastElementChild.querySelectorAll('input');

        for (var i = 0; i < inputs.length; i++) {
          if (inputs[i].id.includes('NAME')) {
            inputs[i].value = spell_instance['Name'];
          }
          if (inputs[i].id.includes('LINK')) {
            inputs[i].value = spell_instance['Link'];
          }
        }
      });

      set_dom_value(spell_table.lastElementChild.id + '_USES_INPUT', spell_obj['Uses']);
      set_dom_value(spell_table.lastElementChild.id + '_USES_DC_INPUT', spell_obj['Dc']);
    });
  }

  /************************************************************************************************/

  // Get Treasure buttons
  var treasure_row = document.getElementById(container_id + 'R7');
  var treasure_table = treasure_row.querySelector('table');

  var treasure_blank_button = document.getElementById(treasure_table.id + 'C_BLANK');
  var treasure_special_button = document.getElementById(treasure_table.id + 'C_SPECIAL');

  update_table_container(new_json['Treasure'], treasure_table.id, treasure_blank_button, treasure_special_button);
}


/**Updates a table section of the webpage
 * @param new_json JSON object to update
 * @param container_id ID of the container as retrieved from storage
 * @param blank_button Button to click when adding a blank row
 * @param special_button Button to click when adding a special row
 */
function update_table_container(new_json, container_id, blank_button, special_button) {
  if (DEBUG) { console.log("Updating Table: " + container_id); }
  new_json['Data'].forEach(function (row) {
    if (row['Type'] === 'Blank') {
      blank_button.click();
      var table = document.querySelector('table#' + container_id);
      var last_row = table.rows[ table.rows.length - 1 ];

      var add_th = document.getElementById(last_row.id + '_TH');
      var add_td = document.getElementById(last_row.id + '_TD');

      for (var key in row) {
        if (key.endsWith('C')) {
          add_td.click();
          set_dom_value(last_row.id + key.split("").reverse().join("") + 'I', row[key]);
        } else if (key.endsWith('H')) {
          add_th.click();
          set_dom_value(last_row.id + key.split("").reverse().join("") + 'I', row[key]);
        }
      }
    } else if (row['Type'] === 'Item') {
      var new_row_id = special_button.click();
      table = document.querySelector('table#' + container_id);
      var last_row = table.rows[ table.rows.length - 1 ];
      set_dom_value(last_row.id + '_NAME', row['Name']);
      set_dom_value(last_row.id + '_DESCRIBE', row['Describe']);
      set_dom_value(last_row.id + '_TEXT', row['Text']);
      set_dom_value(last_row.id + '_CATEGORY_I', row['Category']);
      set_dom_value(last_row.id + '_DESCRIPTOR_I', row['Descriptor']);
    }
  })
}


/**Updates a hazard section of the webpage
 * @param new_json JSON object to update
 * @param container_id ID of the container as retrieved from storage
 */
function update_hazard_container(new_json, container_id) {
  if (DEBUG) { console.log("Updating Hazard: " + container_id); }
  var hazard_table = document.querySelector('table#' + container_id);

  // Standard List
  set_dom_value(container_id + 'R1_NAME', new_json['Name']);
  set_dom_value(container_id + 'R1_CR', new_json['Cr']);
  set_dom_value(container_id + 'R4_COMPLEXITY', new_json['Complexity']);
  set_dom_value(container_id + 'R4_STEALTH', new_json['Stealth']);
  set_dom_value(container_id + 'R4_DESCRIPTION', new_json['Description']);
  set_dom_value(container_id + 'R4_DISABLE', new_json['Disable']);

  // Trait List
  var trait_list = document.getElementById(container_id + 'R2_TRAITS');
  for (var x = 0; x < new_json['Traits'].length; x++) {
    document.getElementById(container_id + 'R3_TRAIT_ADD').click()
    set_dom_value(trait_list.lastElementChild.firstElementChild.id, new_json['Traits'][x]);
  }

  // Custom
  var custom_list = document.getElementById(container_id + 'R5_CUSTOM_LIST');
  new_json['Custom'].forEach(function(custom_obj) {
    var key = Object.keys(custom_obj)[0];

    document.getElementById(container_id + 'R5_CUSTOM_ADD').click();
    var custom_inputs = custom_list.lastElementChild.querySelectorAll('input');
    set_dom_value(custom_inputs[0].id, key);
    set_dom_value(custom_inputs[1].id, custom_obj[key]);
  });
}


/**Updates a list section of the webpage
 * @param new_json JSON object to update
 * @param container_id ID of the container as retrieved from storage
 */
function update_list_container(new_json, container_id) {
  if (DEBUG) { console.log("Updating List: " + container_id); }
  
  var add_row_button = document.getElementById(container_id + '_ADD');
  var content = document.getElementById(container_id).lastElementChild.firstElementChild;
  new_json['Data'].forEach(function(line_obj) {
    add_row_button.click();
    set_dom_value(content.lastElementChild.id + 'I', line_obj['Data']);
    if (line_obj['Bold']) {
        document.getElementById(content.lastElementChild.id + 'I_BOLD').checked = true;
    }
    if (line_obj['Underline']) {
        document.getElementById(content.lastElementChild.id + 'I_UNDERLINE').checked = true;
    }
  })
}
