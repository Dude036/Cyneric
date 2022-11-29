/************************************
 * Element creation for all formats *
 ************************************/

// Color Indexes
let DELETE_COLOR = '#C00000';
let PF2E_COLOR = '#009900';
let PF1E_COLOR = '#000099';
let DND5_COLOR = '#009999';
let GREY_BACKGROUND = '#EFEFEF';

let latest_store_rows = 0;
let latest_table_rows = 0;
let latest_list_rows = 0;


/**Generic Delete Button
 * @param icon Name of the Icon
 * @param title Title to display on Hover
 * @param additive Additive to the image tag
 * @return Blank Delete Button
 */
function generic_action_span(icon, title, additive, margin) {
  var new_button = document.createElement('span');
  new_button.style.margin = margin;
  new_button.innerHTML = '<img src="/static/svg/' + icon + '.svg" title="' + title + '" ' + additive + ' width="30px" height="30px" >';
  return new_button;
}


/**Generic Input given id
 * @param id The base Id to set
 * @return Text input DOM object
 */
function generic_text_input(id) {
  var new_input = document.createElement('input');
  new_input.type = 'text';
  new_input.name = id;
  new_input.id = id;

  return new_input;
}


/**Generic Input given id
 * @param id The base Id to set
 * @return Text input DOM object
 */
function generic_textarea(id) {
  var new_input = document.createElement("textarea");;
  new_input.appendChild(document.createTextNode("Type Text Here"));
  new_input.name = id;
  new_input.id = id;
  new_input.style.resize = 'vertical';

  return new_input;
}


/**Create a button for adding randomly generated content from the DMTK
 * @param text Text to be added to the InnerHTML
 * @param background Background Color
 * @param color Text color 
 * @return Flex box ready for an event listener
 */
function add_api_flex_box(text, background, color) {
  var add_flex_box = document.createElement('div');
  add_flex_box.style.justifyContent = 'flex-start';
  add_flex_box.style.margin = '3px 5px';
  add_flex_box.style.width = 'auto';
  add_flex_box.style.padding = '3px';
  add_flex_box.style.backgroundColor = background;
  add_flex_box.style.color = color;
  add_flex_box.innerHTML = text;
  return add_flex_box;
}


/**Adds header function: move
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: move
 */
function add_header_move(parent, content) {
  return generic_action_span('move', 'Move Block', 'class="move-handle"', '0 20px 0 0');
}


/**Adds header function: hide
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: hide
 */
function add_header_hide(parent, content) {
  var hide_button = generic_action_span('hide', 'Hide Block', '', '0 20px 0 0');
  hide_button.name = content.id;
  hide_button.addEventListener('click', function() {
    var a = document.getElementById(this.name);
    if (this.innerHTML.includes('unhide')) {
      this.innerHTML = '<img src="/static/svg/hide.svg" title="Hide Block" width="30px" height="30px">';
      a.style.display = 'block';
    } else {
      this.innerHTML = '<img src="/static/svg/unhide.svg" title="Unhide Block" width="30px" height="30px">';
      a.style.display = 'none';
    }
  });

  return hide_button;
}


/**Adds header function: delete
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: delete
 */
function add_header_delete(parent, content) {
  var delete_button = generic_action_span('delete', 'Delete Item', '', '0 20px 0 0');
  delete_button.onclick = function() {
    if (confirm("Delete Item?")) {
      if (DEBUG) { console.log("Deleting Item"); }
      parent.parentNode.removeChild(parent);
      if (DEBUG) { console.log("Item successfully deleted"); }
      delete_container_session_storage(parent.id)
    }
  }

  return delete_button;
}


/**Adds store header function: owner
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: owner
 */
function add_store_action_owner(parent, content) {
  var add_owner = generic_action_span('owner', 'Generate Owner Information', '', '0 0 0 20px');
  add_owner.style.float = 'right';
  add_owner.onclick = function() {
    var base_id = content.id + "_OWNER";
    if (confirm("Overwrite Owner Content?")) {
      owner_api_wrapper(base_id, 'npc/json');
      save_container_as_json(parent);
    }
  }

  return add_owner;
}


/**Adds store header function: item_row
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: item_row
 */
function add_store_action_item_row(parent, content) {
  var add_row = generic_action_span('asterisk', 'Add Item Row', '', '0 0 0 20px');
  add_row.style.float = 'right';
  add_row.id = parent.id + '_SPECIAL';

  add_row.onclick = function() {
    var element = document.querySelector('table#' + content.id);

    // Row Setup
    var item_row = element.insertRow(element.rows.length);
    if (element.id.startsWith("S")) {
      item_row.id = element.id + "R" + latest_store_rows;
      latest_store_rows++;
    } else {
      item_row.id = element.id + "R" + latest_table_rows;
      latest_table_rows++;
    }

    // Move Handle
    var add_move_handle = document.createElement('img');
    add_move_handle.src = "/static/svg/move_vertical.svg";
    add_move_handle.title = "Move Row";
    add_move_handle.className = "move-handle";
    add_move_handle.width = 30;
    add_move_handle.height = 30;
    add_move_handle.style.float = "left";
    add_move_handle.style.margin = "10px";
    item_row.appendChild(add_move_handle);

    // Add custom buttons for generated content
    var add_button_td = item_row.insertCell(0);
    var add_button_div = document.createElement('div');
    add_button_div.style.padding = '5px 2px';
    add_button_div.style.width = '100%';
    add_button_div.style.margin = '5px 8px';
    add_button_div.style.display = 'flex';
    add_button_div.style.flexWrap = 'wrap';
    add_button_div.style.alignItems = 'flex-start';

    var add_generate_label = add_api_flex_box("Generate:", '#FFFFFF', '#000000');
    add_generate_label.style.border = '1px solid black';
    add_generate_label.style.backgroundColor = '#FFFFFF';
    add_generate_label.onclick = function() {
      if (add_generate_label.style.backgroundColor == 'rgb(255, 255, 255)') {
        // Setup Show Hide feature
        add_generate_label.style.backgroundColor = '#0F0F0F';
        add_generate_label.style.color = '#EFEFEF';

        // Setup another column for buttons
        var add_generator_div = document.createElement('div');
        add_generator_div.id = item_row.id + '_Generate_Buttons'
        add_generator_div.style.padding = '5px 2px';
        add_generator_div.style.width = '100%';
        add_generator_div.style.margin = '5px 8px';
        add_generator_div.style.display = 'flex';
        add_generator_div.style.flexWrap = 'wrap';
        add_generator_div.style.alignItems = 'flex-start';
        add_button_td.appendChild(add_generator_div);
        
        /* Populate with Generate functions */

        // Create Random Weapon
        var add_weapon = add_api_flex_box("Weapon", '#0CBFBF', '#000000');
        add_weapon.onclick = function() { item_api_wrapper(item_row.id, 'item/weapon/json/'); }
        add_generator_div.appendChild(add_weapon);

        // Create Random Armor
        var add_armor = add_api_flex_box("Armor", '#BF0CBF', '#EFEFEF');
        add_armor.onclick = function() { item_api_wrapper(item_row.id, 'item/armor/json/'); }
        add_generator_div.appendChild(add_armor);

        // Create Random Firearm
        var add_firearm = add_api_flex_box("Firearm", '#BFBF0C', '#000000');
        add_firearm.onclick = function() { item_api_wrapper(item_row.id, 'item/firearm/json/'); }
        add_generator_div.appendChild(add_firearm);

        // Create Random Scroll
        var add_scroll = add_api_flex_box("Scroll", '#0FAC0F', '#EFEFEF');
        add_scroll.onclick = function() { item_api_wrapper(item_row.id, 'item/scroll/json/'); }
        add_generator_div.appendChild(add_scroll);
        
        // Create Random Potion
        var add_potion = add_api_flex_box("Potion", '#0F0FAC', '#EFEFEF');
        add_potion.onclick = function() { item_api_wrapper(item_row.id, 'item/potion/json/'); }
        add_generator_div.appendChild(add_potion);
        
        // Create Random Book
        var add_book = add_api_flex_box("Book", '#AC5F0F', '#EFEFEF');
        add_book.onclick = function() { item_api_wrapper(item_row.id, 'item/book/json/'); }
        add_generator_div.appendChild(add_book);
        
        // Create Random Food
        var add_food = add_api_flex_box("Food", '#5FAC5F', '#EFEFEF');
        add_food.onclick = function() { item_api_wrapper(item_row.id, 'item/food/json/'); }
        add_generator_div.appendChild(add_food);
        
        // Create Random Trinket
        var add_trinket = add_api_flex_box("Trinket", '#AC5F5F', '#EFEFEF');
        add_trinket.onclick = function() { item_api_wrapper(item_row.id, 'item/trinket/json/'); }
        add_generator_div.appendChild(add_trinket);

        // Populate with Create functions
      } else {
        // Setup Show Hide feature
        add_generate_label.style.backgroundColor = '#FFFFFF';
        add_generate_label.style.color = '#000000';
        // Delete generator stuff
        document.getElementById(item_row.id + '_Generate_Buttons').remove();
      }
    }
    add_button_div.appendChild(add_generate_label);

    // Delete
    var add_delete = add_api_flex_box("Delete Row", '#C00000', '#EFEFEF');
    add_button_div.appendChild(add_delete);

    // Add Delete row Method
    add_delete.onclick = function() {
      if (confirm("Are you sure you want to delete this row?")) {
        if (DEBUG) { console.log("Deleting Row"); }
        item_row.parentNode.removeChild(item_row);
        if (DEBUG) { console.log("Row Successfully Deleted"); }
      }
    }

    add_button_td.appendChild(add_button_div);

    // Add Descriptor
    var item_descriptor_cell = item_row.insertCell(0);
    item_descriptor_cell.id = item_row.id + "_DESCRIPTOR";

    var item_descriptor = generic_text_input(item_descriptor_cell.id + "_I");
    item_descriptor.placeholder = 'DESCRIPTOR';
    item_descriptor_cell.appendChild(item_descriptor);

    // Add Category
    var item_category_cell = item_row.insertCell(0);
    item_category_cell.id = item_row.id + "_CATEGORY";

    var item_category = generic_text_input(item_category_cell.id + "_I");
    item_category.placeholder = 'CATEGORY';
    item_category_cell.appendChild(item_category);

    // Add Main Data
    var item_data_cell = item_row.insertCell(0);
    item_data_cell.id = item_row.id + "_DATA";

    var item_name = document.createElement('input');
    item_name.type = 'text';
    item_name.name = item_row.id + "_NAME";
    item_name.id = item_row.id + "_NAME";
    item_name.placeholder = 'Name';
    item_data_cell.appendChild(item_name);

    item_data_cell.appendChild(document.createElement('br'));

    var item_describe = document.createElement('input');
    item_describe.type = 'text';
    item_describe.name = item_row.id + "_DESCRIBE";
    item_describe.id = item_row.id + "_DESCRIBE";
    item_describe.placeholder = 'Description';
    item_data_cell.appendChild(item_describe);

    item_data_cell.appendChild(document.createElement('br'));

    var item_text = document.createElement('textarea');
    item_text.name = item_row.id + "_TEXT";
    item_text.id = item_row.id + "_TEXT";
    item_text.placeholder = 'Long Description';
    item_text.style.lineHeight = "20px";
    item_text.style.width = "400px";
    item_text.style.resize = 'vertical';
    item_data_cell.appendChild(item_text);
    save_container_as_json(parent);
  }

  return add_row;
}


/**Adds store header function: blank_row
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: blank_row
 */
function add_store_action_blank_row(parent, content) {
  var add_row = generic_action_span('add', 'Add Blank Row', '', '0 0 0 20px');
  add_row.style.float = 'right';
  add_row.id = parent.id + '_BLANK';

  add_row.onclick = function() {
    var element = document.querySelector('table#' + content.id);

    // Row Setup
    var new_row = element.insertRow(element.rows.length);
    if (element.id.startsWith("S")) {
      new_row.id = element.id + "R" + latest_store_rows;
      latest_store_rows++;
    } else {
      new_row.id = element.id + "R" + latest_table_rows;
      latest_table_rows++;
    }
    
    // Move Handle
    var add_move_handle = document.createElement('img');
    add_move_handle.src = "/static/svg/move_vertical.svg";
    add_move_handle.title = "Move Row";
    add_move_handle.className = "move-handle";
    add_move_handle.width = 30;
    add_move_handle.height = 30;
    add_move_handle.style.float = "left";
    add_move_handle.style.margin = "10px";
    new_row.appendChild(add_move_handle);

    // Contents
    var add_contents_td = new_row.insertCell(0);
    var add_contents_div = document.createElement('div');
    add_contents_div.style.padding = '5px 2px';
    add_contents_div.style.width = '100%';
    add_contents_div.style.margin = '5px 8px';
    add_contents_div.style.display = 'flex';
    add_contents_div.style.flexWrap = 'wrap';
    add_contents_div.style.alignItems = 'flex-start';

    // Detail Style
    var add_detail = add_api_flex_box("Add 'td'", '#500050', '#EFEFEF');
    add_detail.id = new_row.id + '_TD';

    // Setup function for adding td Cell
    add_detail.onclick = function() {
      var new_cell = new_row.insertCell(new_row.cells.length - 1);
      new_cell.id = new_row.id + 'C' + (new_row.cells.length - 1);
      new_cell.style.backgroundColor = "#FFFFFF";

      var new_input = document.createElement('textarea');
      new_input.style.resize = 'vertical';
      new_input.name = new_cell.id + "I";
      new_input.id = new_cell.id + "I";

      new_cell.appendChild(new_input);
    }
    add_contents_div.appendChild(add_detail)

    // Header Style
    var add_header = add_api_flex_box("Add 'th'", '#005050', '#EFEFEF');
    add_header.id = new_row.id + '_TH';

    // Setup function for adding th Cell
    add_header.onclick = function() {
      var new_cell = new_row.insertCell(new_row.cells.length - 1);
      new_cell.id = new_row.id + 'H' + (new_row.cells.length - 1);
      new_cell.style.backgroundColor = "#CFCFCF";

      var new_input = document.createElement('textarea');
      new_input.style.resize = 'vertical';
      new_input.name = new_cell.id + "I";
      new_input.id = new_cell.id + "I";

      new_cell.appendChild(new_input);
    }
    add_contents_div.appendChild(add_header);

    // Delete Row
    var add_delete = add_api_flex_box("Delete Row", '#C00000', '#EFEFEF');
    // Add Delete row Method
    add_delete.onclick = function() {
      if (confirm("Are you sure you want to delete this row?")) {
        if (DEBUG) { console.log("Deleting Row"); }
        new_row.parentNode.removeChild(new_row);
        if (DEBUG) { console.log("Row Successfully Deleted"); }
      }
    }
    add_contents_div.appendChild(add_delete)
    add_contents_td.appendChild(add_contents_div);
  }

  return add_row;
}


/**Add list settings when creating a list element
 * @param parent_obj LI container
 * @param add_id Matching ID for a list's modifier
 */
function create_list_settings(parent_obj, add_id) {
  // Bold
  var add_bold = generic_action_span('bold_white', 'Bold Line', '', '0 20px 0 20px');
  add_bold.id = add_id + '_BOLD'
  add_bold.addEventListener('click', function() {
    var a = document.getElementById(this.id);
    if (this.innerHTML.includes('white')) {
      this.innerHTML = '<img src="/static/svg/bold_black.svg" title="Remove Bold" width="30px" height="30px">';
    } else {
      this.innerHTML = '<img src="/static/svg/bold_white.svg" title="Bold Line" width="30px" height="30px">';
    }
  });

  parent_obj.appendChild(add_bold);

  // Underline
  var add_underline = generic_action_span('underline_white', 'Underline Line', '', '0 20px 0 0');
  add_underline.id = add_id + "_UNDERLINE";
  add_underline.addEventListener('click', function() {
    var a = document.getElementById(this.id);
    if (this.innerHTML.includes('white')) {
      this.innerHTML = '<img src="/static/svg/underline_black.svg" title="Remove Underline" width="30px" height="30px">';
    } else {
      this.innerHTML = '<img src="/static/svg/underline_white.svg" title="Underline Line" width="30px" height="30px">';
    }
  });

  parent_obj.appendChild(add_underline);

  // Sublist - Tentative?
  /*
  var add_row = generic_action_span('new_list', 'Add Sublist', '', '0 20px 0 0');
  add_row.id = add_id + "_UNDERLINE";
  add_row.addEventListener('click', function() {
    var parent = document.getElementById(this.id).parentElement;
    var new_line = document.createElement('ul');
    new_line.id = add_id + "_";

    var new_element = document.createElement('li');
    new_element.id = new_line.id + latest_list_rows;
    latest_list_rows++;

    var new_element_input = document.createElement('textarea');
    new_element_input.id = new_element.id + 'I'
    new_element_input.placeholder = 'Text';


    new_element.appendChild(new_element_input)
    new_line.appendChild(new_element)

    create_list_settings(new_element, new_element.id + 'I');

    parent.appendChild(new_line);
  })

  parent_obj.appendChild(add_row);
  */

  // Delete
  var add_delete_div = generic_action_span('delete', 'Delete Item', '', '0 20px 0 0');
  add_delete_div.id = add_id + "_DELETE";

  // Delete Row option
  add_delete_div.onclick = function() {
    if (confirm("Delete row?")) {
      if (DEBUG) { console.log("Deleting row"); }
      parent_obj.parentNode.removeChild(parent_obj);
      if (DEBUG) { console.log("Row successfully deleted"); }
    }
  }

  parent_obj.appendChild(add_delete_div);
}


/**Adds list header function: new_row
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: new_row
 */
function add_list_action_new_row(parent, content) {
  var new_row = generic_action_span('add', 'Add List Row', '', '0 0 0 20px');
  new_row.style.float = 'right';
  new_row.id = parent.id + '_ADD';

  new_row.onclick = function() {
    var new_row = document.createElement('li');
    new_row.id = content.id + "R" + latest_list_rows;
    latest_list_rows++;
    
    var new_row_input = document.createElement('textarea');
    new_row_input.id = new_row.id + 'I'
    new_row_input.placeholder = 'Text';

    new_row.appendChild(new_row_input);

    create_list_settings(new_row, new_row_input.id);

    content.appendChild(new_row);
    save_container_as_json(parent);
  }

  return new_row
}


/**Adds monster header function: import
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @param icon Icon to use for action
 * @param label Label to use for action
 * @return Action for parent of type: import
 */
function add_monster_action_import(parent, content, icon, label) {
  var new_row = generic_action_span(icon, label, '', '0 0 0 20px');
  new_row.style.float = 'right';
  new_row.id = content.id + '_IMPORT';

  new_row.onclick = function() {
    get_monster_contents(label, icon[icon.length - 1], parent.id)
  }

  return new_row;
}


/**Adds hazard header function: import
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @param icon Icon to use for action
 * @param label Label to use for action
 * @return Action for parent of type: import
 */
function add_hazard_action_import(parent, content, icon, label) {
  var new_row = generic_action_span(icon, label, '', '0 0 0 20px');
  new_row.style.float = 'right';
  new_row.id = content.id + '_IMPORT';

  new_row.onclick = function() {
    get_hazard_contents(label, icon[icon.length - 1], content.id)
  }

  return new_row;
}


/**Adds monster header function: edition
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @param icon Icon to use for action
 * @param label Label to use for action
 * @return Action for parent of type: edition
 */
function add_list_action_edition(parent, content, icon, label) {
  var new_row = generic_action_span(icon, label, '', '0 0 0 20px');
  new_row.style.float = 'right';
  new_row.id = content.id + '_EDITION';
  new_row.name = content.id + '_EDITION_' + label[label.length - 2];
  new_row.style.display = 'none';

  return new_row;
}
