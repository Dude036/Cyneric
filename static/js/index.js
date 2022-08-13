/*******************************************************************************************************/
/* DYNAMIC ELEMENT CREATION ****************************************************************************/
/*******************************************************************************************************/

// Dragula Initial Setup
let drake = dragula([document.getElementById('editor')], {
  revertOnSpill: true,
  direction: 'vertical',
  moves: function (el, container, handle) {
    // Elements that contain the move-handle class can be moved.
    return handle.classList.contains('move-handle');
  },
  accepts: function (el, target, source, sibling) {
    // If we're working with a store, don't swap the OWNER element
    if (target != null) {
      if (target.firstChild != null) {
        if (target.firstChild.id != null) {
          if (!target.firstChild.id.endsWith('_OWNER')) {
            return false;
          }
        }
      }
    }
    // Accept dragged container only if the drop target is the same
    // as the source container the element came from
    return target == source;
  }
});


/**Manual saving or Deleting the page
 * @param state "Save" or "Delete"
 */
function update_page_state(state) {
  if (DEBUG) { console.log("Updating page state"); }
  if (state === "Save") {
    refresh_page_json()
    save_json_from_page();
    (async () => {
      // Toast Message
      var toast = document.createElement('div');
      toast.style.backgroundColor = "#8DE09F";
      toast.style.position = "fixed";
      toast.style.top = "40px";
      toast.style.left = "40px";
      toast.id = "toast";
      toast.style.padding = "10px 20px";

      toast.appendChild(document.createTextNode("Document has been Saved"));

      var header_img = document.getElementById("header_img");
      header_img.appendChild(toast);

      setTimeout(function(){
        toast.parentNode.removeChild(toast);
      }, 5000);
    })()
  } else if (state === "Delete") {
    // Recursive Deletion of the page
    if (confirm("Are you sure you want Delete everthing on this page?")) {
      header.value = "";
      description.value = "";

      // Delete contents of editor and session
      document.getElementById('editor').innerHTML = "";
      sessionStorage.clear();
    }
  } else if (state === "Load") {
    if (confirm("Loading will Current Page contents. Are you sure you want to Load from Storage?")) {
      header.value = "";
      description.value = "";

      // Delete contents of editor and session
      document.getElementById('editor').innerHTML = "";
      var json_from_storage = export_session_json();
      update_page(json_from_storage);
      sessionStorage.clear();
    }
  }
  if (DEBUG) { console.log("Page state updated"); }
}


/**Create the Parent Container for Tables
 * @param element Primary child element, the table
 * @return Fully formed container for Table elements
 */
function editor_container_table(element) {
  if (DEBUG) { console.log("Begin Table Container Creation"); }

  // Dragula Add
  drake.containers.push(element.firstChild);

  var container = document.createElement("div");
  container.id = element.id + "C";
  container.width = '100%';

  // Add Sub Element Methods
  // Add New Row divs
  var add_row_div = document.createElement('div');
  add_row_div.id = container.id + "_BLANK";
  add_row_div.style.backgroundColor = '#500050';
  add_row_div.style.color = '#EFEFEF';
  add_row_div.style.float = 'right';
  add_row_div.style.padding = '5px';
  add_row_div.innerHTML = "Add Blank Row";

  // Setup function to add items to the row
  add_row_div.onclick = function() {
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

      var new_input = document.createElement('input');
      new_input.type = 'text';
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

      var new_input = document.createElement('input');
      new_input.type = 'text';
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
  };

  // Add Table Name
  if (element.id.startsWith("T")) {
    var add_title_div = document.createElement('div');
    add_title_div.id = container.id + "_NAME";
    add_title_div.style.backgroundColor = '#666666';
    add_title_div.style.color = '#EFEFEF';
    add_title_div.style.float = 'left';
    add_title_div.style.padding = '4px';
    var add_title_input = document.createElement('input');
    add_title_input.id = add_title_div.id + "_I";
    add_title_input.placeholder = 'Table Name';
    add_title_div.appendChild(add_title_input);
  }

  // Only Delete if it is its own table.
  if (element.id.startsWith("S") || element.id.startsWith("T")) {
    // Delete Method
    var add_delete_div = document.createElement('div');
    add_delete_div.style.float = 'right';
    add_delete_div.style.padding = '5px';
    add_delete_div.style.backgroundColor = '#C00000';
    add_delete_div.style.color = '#EFEFEF';
    add_delete_div.innerHTML = "Delete Table";
    add_delete_div.id = container.id + "_DELETE";

    // Delete Table option
    add_delete_div.onclick = function() {
      if (confirm("Delete Table?")) {
        if (DEBUG) { console.log("Deleting Table"); }
        container.parentNode.removeChild(container);
        if (DEBUG) { console.log("Table successfully deleted"); }
      }
    }

    container.appendChild(add_delete_div);
  } else if (element.id.startsWith("M")) {
    // Clear Elementes Method
    var add_delete_div = document.createElement('div');
    add_delete_div.style.float = 'right';
    add_delete_div.style.padding = '5px';
    add_delete_div.style.backgroundColor = '#C00000';
    add_delete_div.style.color = '#EFEFEF';
    add_delete_div.innerHTML = "Clear Table";
    add_delete_div.id = container.id + "_CLEAR";

    // Delete Table option
    add_delete_div.onclick = function() {
      if (confirm("Clear Table?")) {
        if (DEBUG) { console.log("Clearing Table"); }
        element.innerHTML = '';
        if (DEBUG) { console.log("Table successfully Cleared"); }
      }
    }

    container.appendChild(add_delete_div);
  }

  // Add Special Row
  var add_item_div = document.createElement('div');
  add_item_div.id = container.id + "_SPECIAL";
  add_item_div.style.float = 'right';
  add_item_div.style.padding = '5px';
  add_item_div.style.backgroundColor = '#005050';
  add_item_div.style.color = '#EFEFEF';
  add_item_div.innerHTML = "Add Item Row";

  // Add Special Row options
  add_item_div.onclick = function() {
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

    // Delete Row
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
  }

  if (element.id.startsWith("S")) {
    // Adding Automated store Button
    var generate_owner_div = document.createElement('div');

    generate_owner_div.style.float = 'right';
    generate_owner_div.style.padding = '5px';
    generate_owner_div.style.backgroundColor = '#50A0A0';
    generate_owner_div.style.color = '#EFEFEF';
    generate_owner_div.innerHTML = "Generate Owner";
    generate_owner_div.id = container.id + "_GENERATE";

    generate_owner_div.onclick = function() {
      if (DEBUG) { console.log("container.id = " + container.id); }
      var base_id = element.id + "_OWNER";
      if (confirm("Overwrite Owner Content?")) {
        owner_api_wrapper(base_id, 'npc/json');
      }
    }

    container.appendChild(generate_owner_div);
  }

  container.appendChild(add_row_div);
  container.appendChild(add_item_div);

  if (element.id.startsWith("T")) {
    container.appendChild(add_title_div);
  }
  
  // Add Movement within local div?
  container.appendChild(element);
  return container;
}


/** Adds list item, and its input, to a parent list.
 * @param parent Parent list
 * @param prefix Label prefix for either a monster or an owner
 * @param descriptor The descriptor for the placeholder text and id
 * @param type Type of input
 * @param add_id The id that will be referenced during export
 * @return Sub-Element for owner information
 */
function sub_list_element(parent, prefix, descriptor, type, add_id) {
  var new_input = document.createElement('li');
  var new_input_input = document.createElement('input');
  new_input_input.id = add_id + "_" + descriptor.toUpperCase();
  new_input_input.type = type;
  new_input_input.placeholder = prefix + ' ' + descriptor;
  new_input_input.style.marginLeft = '10px';
  var new_input_input_label = document.createElement('label');
  new_input_input_label.id = new_input_input.id + '_LABEL'
  new_input_input_label.innerHTML = prefix + ' ' + descriptor;
  new_input.appendChild(new_input_input_label);

  new_input.appendChild(new_input_input);
  parent.appendChild(new_input);
}


/**Create the Parent container for Hazard
 * @param element Primary Child element, the table
 * @param edition Child element's edition
 * @return Fully formed chontainer for Hazard table elements
 */
function editor_container_hazard(element, edition) {
  var container = document.createElement("div");
  container.id = element.id + "C";
  container.width = '100%';

  // Add hazard information
  var add_edition_div = document.createElement('div');
  add_edition_div.style.float = 'right';
  add_edition_div.style.padding = '5px';
  add_edition_div.style.color = '#EFEFEF';
  if (edition == '5') {
    add_edition_div.style.backgroundColor = '#009999';
    add_edition_div.innerHTML = "Edition: D&D 5e";
  } else if (edition == '2') {
    add_edition_div.style.backgroundColor = '#009900';
    add_edition_div.innerHTML = "Edition: Pathfinder 2e";
  } else if (edition == '1') {
    add_edition_div.style.backgroundColor = '#000099';
    add_edition_div.innerHTML = "Edition: Pathfinder 1e";
  }
  add_edition_div.id = container.id + "_EDITION";

  // Add import Div
  var add_import_div = document.createElement('div');
  add_import_div.style.float = 'right';
  add_import_div.style.padding = '5px';
  add_import_div.style.color = '#EFEFEF';
  if (edition == '5') {
    add_import_div.style.backgroundColor = '#002222';
    add_import_div.innerHTML = "Import from 5e.tools";
  } else if (edition == '2') {
    add_import_div.style.backgroundColor = '#002200';
    add_import_div.innerHTML = "Import from 2e.aonprd.com";
  } else if (edition == '1') {
    add_import_div.style.backgroundColor = '#000022';
    add_import_div.innerHTML = "Import from d20pfsrd.com";
  }
  add_import_div.id = container.id + "_IMPORT";
  add_import_div.onclick = function() {
    get_hazard_contents(add_import_div.innerHTML, edition, container.id)
  }

  // Delete Styling
  var add_delete_div = document.createElement('div');
  add_delete_div.style.float = 'right';
  add_delete_div.style.padding = '5px';
  add_delete_div.style.backgroundColor = '#C00000';
  add_delete_div.style.color = '#EFEFEF';
  add_delete_div.innerHTML = "Delete Hazard";
  add_delete_div.id = container.id + "_DELETE";

  // Delete List Function
  add_delete_div.onclick = function() {
    if (confirm("Delete Hazard?")) {
      if (DEBUG) { console.log("Deleting Hazard"); }
      container.parentNode.removeChild(container);
      if (DEBUG) { console.log("Hazard successfully deleted"); }
    }
  }

  container.appendChild(add_delete_div);
  container.appendChild(add_edition_div);
  container.appendChild(add_import_div);

  container.appendChild(element);
  return container;
}


/**Create Store element
 * @param store Primary element to modify
 * @return Full formed store DOM object
 */
function create_element_store(store) {
  store.id = "S" + latest_store
  latest_store += 1;
  
  // Dragula Add
  drake.containers.push(store.firstChild);

  // Style
  store.style.width = "100%";
  store.style.borderBottom = "1px solid black";
  store.style.marginBottom = "20px";
  // store.style.padding = '5px'

  // Add sub elements for Store
  var owner_row = store.insertRow(store.rows.length);
  owner_row.id = store.id + "_OWNER";
  var owner_container = owner_row.insertCell();
  owner_container.setAttribute("colspan", '100%');
  owner_container.id = store.id + "_OWNER";

  // Store Name
  var owner_store_name = document.createElement('input');
  owner_store_name.id = owner_container.id + "_STORE";
  owner_store_name.type = 'text';
  owner_store_name.placeholder = 'Store Name (Type)';
  owner_store_name.value = '';
  owner_store_name.style.fontSize = '24px';

  owner_store_name.style.marginLeft = '10px';
  var owner_store_name_label = document.createElement('label');
  owner_store_name_label.id = owner_store_name.id + '_LABEL'
  owner_store_name_label.innerHTML = "Store Name";
  owner_container.appendChild(owner_store_name_label);

  owner_container.appendChild(owner_store_name);
  owner_container.appendChild(document.createElement('br'));

  // Owner Name
  var owner_name = document.createElement('input');
  owner_name.id = owner_container.id + "_NAME";
  owner_name.type = 'text';
  owner_name.placeholder = 'Owner Name';
  owner_name.value = '';

  owner_name.style.marginLeft = '10px';
  var owner_name_label = document.createElement('label');
  owner_name_label.id = owner_name.id + '_LABEL'
  owner_name_label.innerHTML = "Owner Name";
  owner_container.appendChild(owner_name_label);
  
  owner_container.appendChild(owner_name);

  // Descriptions
  var owner_description = document.createElement('ul');

  // Race
  sub_list_element(owner_description, 'Owner', 'Race', 'text', owner_container.id);
  sub_list_element(owner_description, 'Owner', 'Gender', 'text', owner_container.id);
  sub_list_element(owner_description, 'Owner', 'Age', 'text', owner_container.id);
  sub_list_element(owner_description, 'Owner', 'Trait_1', 'text', owner_container.id);
  sub_list_element(owner_description, 'Owner', 'Trait_2', 'text', owner_container.id);

  owner_container.appendChild(owner_description);

  // Description
  owner_description_text = document.createElement('textarea');
  owner_description_text.placeholder = 'Owner Description'
  owner_description_text.style.width = '90%';
  owner_description_text.style.lineHeight = "20px";
  owner_description_text.style.resize = 'vertical';
  owner_description_text.id = owner_container.id + "_DESCRIBE";

  owner_container.appendChild(owner_description_text)

  return store;
}


/**Create Monster element
 * @param monster Primary element to modify
 * @param edition Edition
 * @return Full formed monster DOM object
 */
function create_element_monster(monster, edition) {
  monster.id = "M" + latest_monster
  latest_monster += 1;

  // Style
  monster.style.width = "100%";
  monster.style.borderBottom = "1px solid black";
  monster.style.marginBottom = "20px";
  monster.style.padding = '2px';

  // Add Monster Header
  var monster_header = document.createElement('tr');
  monster_header.id = monster.id + 'R1';

  var monster_header_content = document.createElement('div');
  monster_header_content.style.width = '100%';

  // Monster Name & CR
  var monster_name = document.createElement('div');
  var monster_name_input = document.createElement('input');
  monster_name_input.style.fontSize = '24px';
  monster_name_input.placeholder = 'Monster Name';
  monster_name_input.id = monster_header.id + '_NAME'
  monster_name.appendChild(monster_name_input);
  monster_name.appendChild(document.createTextNode(' - CR: '));

  var monster_cr_input = document.createElement('input');
  monster_cr_input.style.fontSize = '24px';
  monster_cr_input.placeholder = 'CR';
  monster_cr_input.size = '3';
  monster_cr_input.id = monster_header.id + '_CR'
  monster_name.appendChild(monster_cr_input);

  monster_header_content.appendChild(monster_name);

  var monster_align = document.createElement('div');
  var monster_align_input = document.createElement('input');
  monster_align_input.id = monster_header.id + '_ALIGN'
  monster_align_input.placeholder = 'Alignment';

  monster_align.appendChild(monster_align_input);
  monster_header_content.appendChild(monster_align);

  // Traits for Pathfinder 2e
  if (edition == "2") {
    var monster_trait_list_add = document.createElement('div');
    monster_trait_list_add.style.backgroundColor = '#030303';
    monster_trait_list_add.style.color = '#EFEFEF';
    monster_trait_list_add.style.float = 'right'
    monster_trait_list_add.style.padding = '5px'
    monster_trait_list_add.innerHTML = 'Add Trait';
    monster_trait_list_add.id = monster_header.id + "_TRAIT_ADD";

    var monster_trait_list_loc = document.createElement('div');
    monster_trait_list_loc.id = monster_header.id + '_TRAITS';
    monster_trait_list_loc.style.padding = '5px 2px';
    monster_trait_list_loc.style.width = '95%';
    monster_trait_list_loc.style.margin = '15px 10px';
    monster_trait_list_loc.style.display = 'flex';
    monster_trait_list_loc.style.flexWrap = 'wrap';
    monster_trait_list_loc.style.alignItems = 'flex-start';

    monster_trait_list_add.onclick = function() {
      var temp_trait = document.createElement('div');
      temp_trait.style.backgroundColor = '#666666';
      temp_trait.style.color = '#EFEFEF';
      temp_trait.style.justifyContent = 'flex-start';
      temp_trait.style.width = '23%';
      temp_trait.style.margin = '0px 10px';
      temp_trait.style.padding = '3px';

      var temp_trait_input = document.createElement('input');
      temp_trait_input.id = monster_trait_list_loc.id + '_' + latest_monster_trait;
      latest_monster_trait++;
      temp_trait_input.style.fontSize = '13px';

      var temp_trait_delete = document.createElement('span');
      temp_trait_delete.style.color = 'red';
      temp_trait_delete.style.fontWeight = 'bold';
      temp_trait_delete.innerHTML = ' X';

      temp_trait_delete.onclick = function() {
        if (confirm("Delete Trait?")) {
          if (DEBUG) { console.log("Deleting Trait"); }
          temp_trait.parentNode.removeChild(temp_trait);
          if (DEBUG) { console.log("Trait successfully deleted"); }
        }
      }

      temp_trait.appendChild(temp_trait_input);
      temp_trait.appendChild(temp_trait_delete);

      monster_trait_list_loc.appendChild(temp_trait);
    }

    var monster_trait_list_clear = document.createElement('div');
    monster_trait_list_clear.style.float = 'right';
    monster_trait_list_clear.style.padding = '5px';
    monster_trait_list_clear.style.backgroundColor = '#900000';
    monster_trait_list_clear.style.color = '#EFEFEF';
    monster_trait_list_clear.innerHTML = "Clear Traits";
    monster_trait_list_clear.id = monster_header.id + "_TRAIT_CLEAR";

    monster_trait_list_clear.onclick = function() {
      if (confirm("Clear All Traits?")) {
        if (DEBUG) { console.log("Deleting Traits"); }
        monster_trait_list_loc.innerHTML = '';
        if (DEBUG) { console.log("Traits successfully cleared"); }
      }
    }

    monster_header_content.appendChild(monster_trait_list_clear);
    monster_header_content.appendChild(monster_trait_list_add);
    monster_header_content.appendChild(monster_trait_list_loc);
  }

  // Monster Text Box
  var monster_description = document.createElement('div');
  var monster_description_input = document.createElement('textarea');
  monster_description_input.id = monster_header.id + '_DESCRIBE'
  monster_description_input.placeholder = 'Monster Description';
  monster_description_input.style.width = '50%';
  monster_description_input.style.lineHeight = "20px";
  monster_description_input.style.resize = 'vertical';
  monster_description.appendChild(monster_description_input);

  monster_header_content.appendChild(monster_description);
  monster_header.appendChild(monster_header_content);
  monster.appendChild(monster_header);

  /*******************************************************************************************************/

  var monster_info = document.createElement('tr');
  monster_info.id = monster.id + 'R2';
  var monster_info_content = document.createElement('div');
  
  // Monster Base Information
  var stat_list;
  if (edition == '2') {
    stat_list = PATHFINDER_2_STATS;
  } else if (edition == '1') {
    stat_list = PATHFINDER_1_STATS;
  } else if (edition == '5') {
    stat_list = DND_5_STATS;
  }

  var monster_info_list = document.createElement('ul');
  monster_info_list.style.columnCount = 2;

  for (var i = 0; i < stat_list.length; i++) {
    // 5e Saves are checkboxes
    if (/[A-Z]{3} Save/.test(stat_list[i])) {
      sub_list_element(monster_info_list, '', stat_list[i], 'checkbox', monster_info.id);
    } else {
      sub_list_element(monster_info_list, '', stat_list[i], 'text', monster_info.id);
    }
  }

  // Add all above info into the Header
  monster_info_content.appendChild(monster_info_list);
  monster_info.appendChild(monster_info_content);

  monster.appendChild(monster_info);

  /*******************************************************************************************************/

  var monster_stats = document.createElement('tr')
  monster_stats.id = monster.id + 'R3';
  var monster_stats_content = document.createElement('div')

  // Base Stats
  var stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'];
  var monster_stats_table = document.createElement('table');
  monster_stats_table.style.width = '100%';
  var monster_stats_header = document.createElement('tr');
  var monster_stats_info = document.createElement('tr');
  for (var i = 0; i < stats.length; i++) {
    var temp_th = document.createElement('th');
    temp_th.innerHTML = stats[i];
    monster_stats_header.appendChild(temp_th);

    var temp_td = document.createElement('td');
    var temp_td_input = document.createElement('input');
    temp_td_input.placeholder = stats[i];
    temp_td_input.id = monster_stats.id + '_' + stats[i];
    temp_td_input.name = monster_stats.id + '_' + stats[i];
    temp_td_input.style.width = '130px';
    temp_td.appendChild(temp_td_input);
    monster_stats_info.appendChild(temp_td);
  }
  monster_stats_table.appendChild(monster_stats_header);
  monster_stats_table.appendChild(monster_stats_info);

  monster_stats_content.appendChild(monster_stats_table);
  monster_stats.appendChild(monster_stats_content);

  monster.appendChild(monster_stats)

  /*******************************************************************************************************/
  
  var monster_action = document.createElement('tr')
  var monster_action_content = document.createElement('div')
  monster_action.id = monster.id + 'R4';

  // Actions
  var monster_action_container = document.createElement('div');
  monster_action_container.style.display = 'flex';
  monster_action_container.style.flexWrap = 'wrap';
  monster_action_container.style.alignItems = 'flex-start';
  monster_action_container.style.width = '100%';
  monster_action_container.style.paddingTop = '10px';
  monster_action_container.style.paddingBottom = '20px';
  monster_action_container.id = monster_action.id + '_ACTIONS';

  var monster_action_add = document.createElement('div');
  monster_action_add.style.backgroundColor = '#030303';
  monster_action_add.style.color = '#EFEFEF';
  monster_action_add.style.float = 'right';
  monster_action_add.style.padding = '5px';
  monster_action_add.id = monster_action.id + '_ACTION_ADD';
  monster_action_add.innerHTML = 'Add Action';

  monster_action_add.onclick = function() {
    if (DEBUG) { console.log("Adding Action to Monster " + monster_header.id); }

    var temp_action = document.createElement('table');
    temp_action.id = monster_action_container.id + latest_monster_action;
    latest_monster_action++;
    temp_action.style.width = '44%';
    temp_action.style.marginLeft = '3%';
    temp_action.style.marginRight = '3%';
    temp_action.style.marginBottom = '1%';

    // Header Info
    var temp_action_header = document.createElement('tr');
    
    temp_action_header.style.backgroundColor = '#999999'
    temp_action_header.style.color = '#EFEFEF';

    var temp_action_header_input = document.createElement('input');
    temp_action_header_input.type = 'text';
    temp_action_header_input.id = temp_action.id + '_NAME';
    temp_action_header_input.placeholder = 'Action Name';
    temp_action_header.appendChild(temp_action_header_input);

    // Delete action
    var temp_action_header_delete = document.createElement('input');
    temp_action_header_delete.type = 'button';
    temp_action_header_delete.value = 'Delete';
    temp_action_header_delete.style.backgroundColor = '#990000'
    temp_action_header_delete.style.color = '#EFEFEF'

    temp_action_header_delete.onclick = function() {
      if (confirm("Delete Action?")) {
        if (DEBUG) { console.log("Deleting Action"); }
        temp_action.parentNode.removeChild(temp_action);
        if (DEBUG) { console.log("Action successfully deleted"); }
      }
    }
    temp_action_header.appendChild(temp_action_header_delete);

    // Legendary Action Qualifier
    if (edition == '5') {
      var monster_action_legend = document.createElement('input');
      monster_action_legend.type = 'checkbox';
      monster_action_legend.id = temp_action.id  + '_LEGEND'
      monster_action_legend.name = temp_action.id  + '_LEGEND'

      var monster_action_legend_label = document.createElement('label');
      monster_action_legend_label.htmlFor = temp_action.id  + '_LEGEND_LABEL'
      monster_action_legend_label.innerHTML = "<b>Legendary</b>"
      monster_action_legend_label.style.paddingLeft = '10px'
      temp_action_header.appendChild(monster_action_legend_label);
      temp_action_header.appendChild(monster_action_legend);
    }
    // Action Cost Qualifier
    if (edition == '2') {
      var monster_action_cost = document.createElement('select');
      monster_action_cost.id = temp_action.id  + '_COST'
      
      var monster_action_cost_reaction = document.createElement("option");
      monster_action_cost_reaction.text = 'Reaction';
      monster_action_cost.add(monster_action_cost_reaction);

      var monster_action_cost_free = document.createElement("option");
      monster_action_cost_free.text = 'Free';
      monster_action_cost.add(monster_action_cost_free);

      var monster_action_cost_1 = document.createElement("option");
      monster_action_cost_1.text = '1 Action';
      monster_action_cost.add(monster_action_cost_1);

      var monster_action_cost_2 = document.createElement("option");
      monster_action_cost_2.text = '2 Action';
      monster_action_cost.add(monster_action_cost_2);

      var monster_action_cost_3 = document.createElement("option");
      monster_action_cost_3.text = '3 Action';

      monster_action_cost.add(monster_action_cost_3);
      var monster_action_cost_label = document.createElement('label');
      monster_action_cost_label.htmlFor = temp_action.id  + '_COST_LABEL'
      monster_action_cost_label.innerHTML = "<b>Cost: </b>"
      monster_action_cost_label.style.paddingLeft = '10px'

      monster_action_cost.value = '1 Action';
      if (DEBUG) { console.log('Value: ' + monster_action_cost.value); }

      temp_action_header.appendChild(monster_action_cost_label);
      temp_action_header.appendChild(monster_action_cost);
    }

    // Detail Info
    var temp_action_info = document.createElement('tr');
    var temp_action_info_input = document.createElement('textarea');
    temp_action_info_input.id = temp_action.id  + '_TEXT'
    temp_action_info_input.placeholder = 'Action Details';
    temp_action_info_input.style.width = '90%';
    temp_action_info_input.style.lineHeight = "20px";
    temp_action_info_input.style.resize = 'vertical';
    temp_action_info.appendChild(temp_action_info_input);

    temp_action.appendChild(temp_action_header);
    temp_action.appendChild(temp_action_info);
    monster_action_container.appendChild(temp_action);
  }

  var monster_action_clear = document.createElement('div');
  monster_action_clear.style.backgroundColor = '#C00000';
  monster_action_clear.style.color = '#EFEFEF';
  monster_action_clear.style.float = 'right'
  monster_action_clear.style.padding = '5px'
  monster_action_clear.id = monster_action.id + '_ACTION_CLEAR';
  monster_action_clear.innerHTML = 'Clear Actions';

  // Delete Table option
  monster_action_clear.onclick = function() {
    if (confirm("Clear Actions?")) {
      if (DEBUG) { console.log("Clearing Actions"); }
      monster_action_container.innerHTML = '';
      if (DEBUG) { console.log("Actions successfully Cleared"); }
    }
  }

  monster_action_content.appendChild(monster_action_clear);
  monster_action_content.appendChild(monster_action_add);
  monster_action_content.appendChild(monster_action_container);
  monster_action.appendChild(monster_action_content);
  monster.appendChild(monster_action);

  /*******************************************************************************************************/


  var monster_spell = document.createElement('tr');
  monster_spell.id = monster.id + 'R5';


  var monster_spell_sub = document.createElement('tr');
  monster_spell_sub.id = monster.id + 'R6';

  var monster_spell_container = document.createElement('div');
  monster_spell_container.id = monster_spell.id + '_LOC';
  monster_spell_container.style.marginTop = '5px';
  monster_spell_container.style.marginBottom = '5px';

  var monster_spell_add = document.createElement('div');
  monster_spell_add.id = monster_spell.id + '_SPELL_ADD';

  monster_spell_add.innerHTML = "Add Spell Table";
  monster_spell_add.style.backgroundColor = '#030303';
  monster_spell_add.style.color = '#EFEFEF';
  monster_spell_add.style.float = 'right';
  monster_spell_add.style.padding = '5px';

  // Delete Values
  var monster_spell_clear = document.createElement('div');
  monster_spell_clear.style.backgroundColor = '#C00000';
  monster_spell_clear.style.color = '#EFEFEF';
  monster_spell_clear.style.float = 'right'
  monster_spell_clear.style.padding = '5px'
  monster_spell_clear.id = monster_spell.id + '_SPELL_CLEAR';
  monster_spell_clear.innerHTML = 'Delete Tables';
  monster_spell_clear.style.display = 'none';


  monster_spell_add.onclick = function() {
    if (DEBUG) { console.log("Adding Spell Table to Monster " + monster.id); }

    var monster_spell_table = document.createElement('table');
    monster_spell_table.id = monster_spell_container.id + "_MS" + latest_monster_spell;
    var monster_spell_table_container = document.createElement('div');
    monster_spell_table_container.appendChild(monster_spell_table)
    latest_monster_spell++;

    var monster_spell_table_header = document.createElement('tr');
    var monster_spell_table_header_usage = document.createElement('th');
    monster_spell_table_header_usage.innerHTML = 'Usage';
    monster_spell_table_header_usage.style.width = '20%';
    var monster_spell_table_header_spells = document.createElement('th');
    monster_spell_table_header_spells.innerHTML = 'Spell List';
    monster_spell_table_header.appendChild(monster_spell_table_header_usage);
    monster_spell_table_header.appendChild(monster_spell_table_header_spells);
    monster_spell_table.appendChild(monster_spell_table_header)

    // Table Style
    monster_spell_table.style.width = "100%";
    monster_spell_table.style.borderBottom = "1px solid black";
    monster_spell_table.style.marginBottom = "20px";

    var monster_spell_row_add = document.createElement('div');
    monster_spell_row_add.id = monster_spell_table.id + '_ROW_ADD';
    monster_spell_row_add.style.backgroundColor = '#030303';
    monster_spell_row_add.style.color = '#EFEFEF';
    monster_spell_row_add.style.float = 'right';
    monster_spell_row_add.style.padding = '5px';
    monster_spell_row_add.innerHTML = "Add Spell Row";

    monster_spell_row_add.onclick = function() {
      var temp_row = document.createElement('tr');
      temp_row.id = monster_spell_table.id + 'R' + latest_monster_spell_row;

      var temp_spell_use = document.createElement('td');
      temp_spell_use.id = temp_row.id + '_USES';

      var temp_spell_list = document.createElement('td');
      temp_spell_list.id = temp_row.id + '_LIST';
      
      latest_monster_spell_row++;

      // Input Text for usage
      temp_spell_use.style.width = '20%';

      var temp_spell_use_input = document.createElement('input');
      temp_spell_use_input.size = '5';
      temp_spell_use_input.id = temp_spell_use.id + '_INPUT'
      var temp_spell_use_text = document.createElement('span');
      temp_spell_use_text.innerHTML = '/ times day';

      var temp_spell_use_container = document.createElement('div')

      temp_spell_use_container.appendChild(temp_spell_use_input);
      temp_spell_use_container.appendChild(temp_spell_use_text);
      temp_spell_use.appendChild(temp_spell_use_container);

      // Input for DC
      var temp_spell_dc_input = document.createElement('input');
      temp_spell_dc_input.size = '5';
      temp_spell_dc_input.id = temp_spell_use.id + '_DC_INPUT'
      var temp_spell_dc_text = document.createElement('span');
      temp_spell_dc_text.innerHTML = 'DC ';

      var temp_spell_dc_container = document.createElement('div')
      temp_spell_dc_container.appendChild(temp_spell_dc_text);
      temp_spell_dc_container.appendChild(temp_spell_dc_input);
      temp_spell_use.appendChild(temp_spell_dc_container);

      // Input text for Spell list
      var temp_spell_list_loc = document.createElement('div');
      temp_spell_list_loc.style.width = "95%";
      temp_spell_list_loc.style.display = 'flex';
      temp_spell_list_loc.style.padding = '5px 2px';
      temp_spell_list_loc.style.margin = '2px 5px';
      temp_spell_list_loc.style.flexWrap = 'wrap';
      temp_spell_list_loc.style.alignItems = 'flex-start';
      temp_spell_list_loc.id = temp_spell_list.id

      var temp_spell_list_add = document.createElement('input');
      temp_spell_list_add.style.width = "10%";
      temp_spell_list_add.style.float = "right";
      temp_spell_list_add.value = 'Add Spell';
      temp_spell_list_add.id = temp_spell_list.id + '_ADD';
      temp_spell_list_add.type = 'button';

      // Button input for adding spells
      temp_spell_list_add.onclick = function() {
        var spell_cont = document.createElement('div');
        spell_cont.style.justifyContent = 'flex-start';
        spell_cont.style.width = '31%';
        spell_cont.style.margin = '0px 5px';
        spell_cont.style.padding = '3px';
        spell_cont.id = temp_spell_list.id + '_CONTAINER_' + latest_monster_spell_col

        var spell_name = document.createElement('input');
        spell_name.type = 'text';
        spell_name.placeholder = 'Spell Name';
        spell_name.size = 26;
        spell_name.id = temp_spell_list.id + '_NAME_' + latest_monster_spell_col;

        var spell_link = document.createElement('input');
        spell_link.type = 'text';
        spell_link.placeholder = 'Spell Link';
        spell_link.size = 22;
        spell_link.id = temp_spell_list.id + '_LINK_' + latest_monster_spell_col;

        var spell_delete = document.createElement('input');
        spell_delete.type = 'button';
        spell_delete.value = 'X';
        spell_delete.style.marginLeft = '2px';
        spell_delete.id = temp_spell_list.id + '_DELETE_' + latest_monster_spell_col;
        spell_delete.onclick = function() {
          if (confirm("Delete Spell Table?")) {
            if (DEBUG) { console.log("Deleteing Spell Table"); }
            spell_cont.parentNode.removeChild(spell_cont);
            if (DEBUG) { console.log("Spell Tables successfully Deleted"); }
          }
        }

        latest_monster_spell_col++;
        spell_cont.appendChild(spell_name);
        spell_cont.appendChild(spell_link);
        spell_cont.appendChild(spell_delete);

        temp_spell_list_loc.appendChild(spell_cont);
      }

      var temp_spell_list_delete = document.createElement('input');
      temp_spell_list_delete.style.float = "right";
      temp_spell_list_delete.value = 'Delete Spell Row';
      temp_spell_list_delete.id = temp_spell_list.id + '_DELETE';
      temp_spell_list_delete.type = 'button';

      temp_spell_list_delete.onclick = function() {
        if (confirm("Delete Spell Row?")) {
          if (DEBUG) { console.log("Deleting Spell Row"); }
          temp_row.parentNode.removeChild(temp_row);
          if (DEBUG) { console.log("Spell Row successfully Deleted"); }
        }
      }

      temp_spell_list.appendChild(temp_spell_list_loc);
      temp_spell_list.appendChild(temp_spell_list_delete);
      temp_spell_list.appendChild(temp_spell_list_add);
      temp_row.appendChild(temp_spell_use);
      temp_row.appendChild(temp_spell_list);
      monster_spell_table.appendChild(temp_row)
    }

    var monster_spell_row_delete = document.createElement('div');
    monster_spell_row_delete.style.backgroundColor = '#C00000';
    monster_spell_row_delete.style.color = '#EFEFEF';
    monster_spell_row_delete.style.float = 'right'
    monster_spell_row_delete.style.padding = '5px'
    monster_spell_row_delete.id = monster_spell_table.id + '_SPELL_CLEAR';
    monster_spell_row_delete.innerHTML = 'Delete Spell Table';

    // Delete Table option
    monster_spell_row_delete.onclick = function() {
      if (confirm("Delete Spell Table?")) {
        if (DEBUG) { console.log("Deleteing Spell Table"); }
        monster_spell_table_container.parentNode.removeChild(monster_spell_table_container);
        if (DEBUG) { console.log("Spell Tables successfully Deleted"); }
      }
      if (monster_spell_container.childNodes.length === 0) {
        monster_spell_add.style.display = 'block';
        monster_spell_clear.style.display = 'none';
      }
    }
    // Finalize
    monster_spell_table_container.appendChild(monster_spell_row_delete);
    monster_spell_table_container.appendChild(monster_spell_row_add);
    monster_spell_table_container.appendChild(monster_spell_table);
    monster_spell_container.appendChild(monster_spell_table_container);

    monster_spell_add.style.display = 'none';
    monster_spell_clear.style.display = 'block';
  }

  // Delete Table option
  monster_spell_clear.onclick = function() {
    if (confirm("Clear Spell Tables?")) {
      if (DEBUG) { console.log("Clearing Spell Tables"); }
      monster_spell_container.innerHTML = '';
      if (DEBUG) { console.log("Spell Tables successfully Cleared"); }
    }
    monster_spell_add.style.display = 'block';
    monster_spell_clear.style.display = 'none';
  }

  monster_spell.appendChild(monster_spell_clear);
  monster_spell.appendChild(monster_spell_add);
  monster.appendChild(monster_spell);

  monster_spell_sub.appendChild(monster_spell_container);
  monster.appendChild(monster_spell_sub);

  /*******************************************************************************************************/

  var monster_loot = document.createElement('tr');
  var monster_loot_table = document.createElement('table');
  monster_loot_table.appendChild(document.createElement('tbody'))

  monster_loot_table.id = "MT" + latest_table
  latest_table += 1;

  // Style
  monster_loot_table.style.width = "100%";
  monster_loot_table.style.borderBottom = "1px solid black";
  monster_loot_table.style.marginBottom = "20px";

  var monster_loot_container = editor_container_table(monster_loot_table);
  monster_loot.id = monster.id + 'R7';

  // Finalize

  var monster_loot_text = document.createElement('h3');
  monster_loot_text.style.textAlign = 'center'
  monster_loot_text.innerHTML = 'Treasure';
  monster_loot.appendChild(monster_loot_text);
  monster_loot.appendChild(monster_loot_container);
  monster.appendChild(monster_loot);

  return monster;
}


/**Create Hazard item
 * @param item_text Item text to use for id, text, and placeholder
 * @param add_id Parent ID text
 * @param custom Flag for whether or not to have a special input for Custom Keys
 * @param input_options Options to impliment for the input
 * @return Hazard div item
 */
function create_element_hazard_list_item(item_text, add_id, custom, input_options) {
  // Key
  var hazard_list_item = document.createElement('div');
  if (custom) {
    var hazard_list_key_input = document.createElement('input');
    hazard_list_key_input.id = add_id + '_CUSTOM_' + latest_hazard_custom;
    hazard_list_key_input.placeholder = 'Custom Key ' + latest_hazard_custom;
    hazard_list_item.appendChild(hazard_list_key_input);
  } else {
    hazard_list_item.appendChild(document.createTextNode(item_text + ': '))
  }
  
  // Value
  var hazard_list_item_input = document.createElement('input');
  hazard_list_item_input.type = 'text';
  if (custom) {
    hazard_list_item_input.id = add_id + '_CUSTOM_' + latest_hazard_custom + '_INPUT';
    hazard_list_item_input.placeholder = 'Custom Input ' + latest_hazard_custom;
    latest_hazard_custom++;
  } else {
    hazard_list_item_input.placeholder = item_text;
    hazard_list_item_input.id = add_id + '_' + item_text.toUpperCase();
  }

  // Special Properties
  for (const property in input_options) {
    hazard_list_item_input[property] = input_options[property];
  }

  hazard_list_item.appendChild(hazard_list_item_input)

  // Delete Method
  if (custom) {
    var hazard_list_button = document.createElement('button');
    hazard_list_button.style.color = 'red';
    hazard_list_button.style.fontWeight = 'bold';
    hazard_list_button.innerHTML = ' X ';
    hazard_list_button.onclick = function() {
      if (confirm("Delete Custom Field?")) {
        if (DEBUG) { console.log("Deleting Custom Field"); }
        hazard_list_item.parentNode.removeChild(hazard_list_item);
        if (DEBUG) { console.log("Custom Field successfully deleted"); }
      }
    }

    hazard_list_item.appendChild(hazard_list_button);
  }

  return hazard_list_item;
}


/**Create Hazard item
 * @param hazard Primary element to modify
 * @return Full formed hazard DOM object
 */
function create_element_hazard(hazard, item) {
  hazard.id = 'H' + latest_hazard;
  latest_hazard++;

  hazard.style.width = "100%";
  hazard.style.borderBottom = "1px solid black";
  hazard.style.marginBottom = "20px";
  hazard.style.padding = '2px';

  // Add Hazard Header
  var hazard_header = document.createElement('tr');
  hazard_header.id = hazard.id + 'R1';

  var hazard_header_content = document.createElement('th');
  hazard_header_content.style.backgroundColor = '#CFCFCF';
  // hazard_header_content.style.width = '100%';

  // Name
  var hazard_name = document.createElement('div');
  hazard_name.style.float = 'left';

  var hazard_name_input = document.createElement('input');
  hazard_name_input.type = 'text'
  hazard_name_input.style.fontSize = '24px';
  hazard_name_input.placeholder = 'Hazard Name';
  hazard_name_input.id = hazard_header.id + '_NAME';
  hazard_name.appendChild(hazard_name_input);
  hazard_header_content.appendChild(hazard_name);

  // CR
  var hazard_cr = document.createElement('div');
  hazard_cr.style.float = 'right';

  var hazard_cr_input = document.createElement('input');
  hazard_cr_input.type = 'text'
  hazard_cr_input.style.fontSize = '24px';
  hazard_cr_input.size = '3';
  hazard_cr_input.placeholder = 'CR';
  hazard_cr_input.id = hazard_header.id + '_CR';
  hazard_cr.appendChild(hazard_cr_input);
  hazard_header_content.appendChild(hazard_cr);

  hazard_header.appendChild(hazard_header_content);
  hazard.appendChild(hazard_header);

  /*******************************************************************************************************/

  var hazard_traits = document.createElement('tr');
  hazard_traits.id = hazard.id + 'R2';
  var hazard_traits_content = document.createElement('td');

  var hazard_traits_sub = document.createElement('tr');

  hazard_traits_sub.id = hazard.id + 'R3';
  var hazard_traits_sub_content = document.createElement('td');

  // Trait List
  var hazard_trait_loc = document.createElement('div');
  hazard_trait_loc.id = hazard_traits.id + '_TRAITS';
  hazard_trait_loc.style.padding = '5px 2px';
  hazard_trait_loc.style.width = '95%';
  hazard_trait_loc.style.margin = '15px 10px';
  hazard_trait_loc.style.display = 'flex';
  hazard_trait_loc.style.flexWrap = 'wrap';
  hazard_trait_loc.style.alignItems = 'flex-start';
  hazard_traits_content.appendChild(hazard_trait_loc);

  // Add hazard trait button
  var hazard_trait_add = document.createElement('div');
  hazard_trait_add.style.float = 'right';
  hazard_trait_add.style.padding = '5px';
  hazard_trait_add.style.backgroundColor = '#606090';
  hazard_trait_add.style.color = '#EFEFEF';
  hazard_trait_add.innerHTML = "Add Hazard Trait";
  hazard_trait_add.id = hazard_traits_sub.id + "_TRAIT_ADD";

  hazard_trait_add.onclick = function() {
    var temp_trait = document.createElement('div');
    temp_trait.style.backgroundColor = '#666666';
    temp_trait.style.color = '#EFEFEF';
    temp_trait.style.justifyContent = 'flex-start';
    temp_trait.style.width = '23%';
    temp_trait.style.margin = '0px 10px';
    temp_trait.style.padding = '3px';

    var temp_trait_input = document.createElement('input');
    temp_trait_input.id = hazard_trait_loc.id + '_' + latest_hazard_trait;
    latest_hazard_trait++;
    temp_trait_input.style.fontSize = '13px';

    var temp_trait_delete = document.createElement('span');
    temp_trait_delete.style.color = 'red';
    temp_trait_delete.style.fontWeight = 'bold';
    temp_trait_delete.innerHTML = ' X';

    temp_trait_delete.onclick = function() {
      if (confirm("Delete Trait?")) {
        if (DEBUG) { console.log("Deleting Trait"); }
        temp_trait.parentNode.removeChild(temp_trait);
        if (DEBUG) { console.log("Trait successfully deleted"); }
      }
    }

    temp_trait.appendChild(temp_trait_input);
    temp_trait.appendChild(temp_trait_delete);

    hazard_trait_loc.appendChild(temp_trait);
  }

  var hazard_trait_clear = document.createElement('div');
  hazard_trait_clear.style.float = 'right';
  hazard_trait_clear.style.padding = '5px';
  hazard_trait_clear.style.backgroundColor = '#900000';
  hazard_trait_clear.style.color = '#EFEFEF';
  hazard_trait_clear.innerHTML = "Clear Traits";
  hazard_trait_clear.id = hazard_traits_sub.id + "_TRAIT_CLEAR";

  hazard_trait_clear.onclick = function() {
    if (confirm("Clear All Traits?")) {
      if (DEBUG) { console.log("Deleting Traits"); }
      hazard_trait_loc.innerHTML = '';
      if (DEBUG) { console.log("Traits successfully cleared"); }
    }
  }

  // Add
  hazard_traits_sub_content.appendChild(hazard_trait_clear);
  hazard_traits_sub_content.appendChild(hazard_trait_add);
  hazard_traits_sub.appendChild(hazard_traits_sub_content);

  hazard_traits.appendChild(hazard_traits_content);
  hazard.appendChild(hazard_traits);
  hazard.appendChild(hazard_traits_sub);

  /*******************************************************************************************************/

  var hazard_details = document.createElement('tr');
  hazard_details.id = hazard.id + 'R4';
  var hazard_details_content = document.createElement('td');

  hazard_details_content.appendChild(create_element_hazard_list_item('Complexity', hazard_details.id, false, {}));
  hazard_details_content.appendChild(create_element_hazard_list_item('Stealth', hazard_details.id, false, {}));
  hazard_details_content.appendChild(create_element_hazard_list_item('Description', hazard_details.id, false, {'size': '100'}));
  hazard_details_content.appendChild(create_element_hazard_list_item('Disable', hazard_details.id, false, {'size': '100'}));

  hazard_details.appendChild(hazard_details_content);
  hazard.appendChild(hazard_details);

  /*******************************************************************************************************/

  var hazard_custom = document.createElement('tr');
  hazard_custom.id = hazard.id + 'R5';
  var hazard_custom_content = document.createElement('td');

  var hazard_custom_add = document.createElement('div');
  hazard_custom_add.id = hazard_custom.id + '_CUSTOM_ADD'
  hazard_custom_add.innerHTML = 'Add Custom Field';
  hazard_custom_add.style.padding = '5px';
  hazard_custom_add.style.backgroundColor = '#606090';
  hazard_custom_add.style.color = '#EFEFEF';
  hazard_custom_add.style.float = 'right';

  hazard_custom_add.onclick = function() {
    hazard_custom_loc.appendChild(create_element_hazard_list_item('', hazard_custom.id, true, {'size': '70'}))
  }

  hazard_custom_content.appendChild(hazard_custom_add);

  var hazard_custom_loc = document.createElement('div')
  hazard_custom_loc.id = hazard_custom.id + '_CUSTOM_LIST'
  hazard_custom_content.appendChild(hazard_custom_loc);

  hazard_custom.appendChild(hazard_custom_content);
  hazard.appendChild(hazard_custom);

  /*******************************************************************************************************/

  return hazard;
}


/**Function to add stuff to the main page. Creates the elements, to then wrap in containers
 * @param item The type of item to be made
 */
function create_element(item) {
  if (DEBUG) { console.log("Begin Element Creation"); }

  // Add header here. should always contain:
  var container = document.createElement('div');
  container.id = item[0] + get_uuid();
  container.style.marginBottom = '60px';

  // Generic update function for all bits of data within a form.
  container.addEventListener('change', function() {
    save_container_as_json(container);
  });

  // Actions
  var actions = document.createElement('div');
  actions.id = container.id + '_ACTIONS';
  actions.style.marginBottom = '5px';

  // Init content
  var content = document.createElement('div');
  content.id = item[0] + incriment_item_counter(item);
  content.style.display = 'block';

  // Add all Actions here
  actions.appendChild(add_header_move(container, content));
  actions.appendChild(add_header_hide(container, content));
  actions.appendChild(add_header_delete(container, content));
  container.appendChild(actions);

  // Finalize content
  if (item === 'Store') {
    // Actions
    actions.appendChild(add_store_action_owner(container, content));
    actions.appendChild(add_store_action_blank_row(container, content));
    actions.appendChild(add_store_action_item_row(container, content));

    // Content
    var store_element = document.createElement('table')
    store_element.appendChild(document.createElement('tbody'))
    var store = create_element_store(store_element);
    content.appendChild(store);
  } else if (item === 'Table') {
    // ACtions
    actions.appendChild(add_store_action_blank_row(container, content));
    actions.appendChild(add_store_action_item_row(container, content));

    // Content
    var table = document.createElement('table');
    table.style.width = '100%';
    table.style.borderBottom = '1px solid black';
    table.style.marginBottom = '20px';
    table.id = content.id

    // Add Table Name
    var add_title_div = document.createElement('div');
    add_title_div.id = content.id + "_NAME";
    add_title_div.style.backgroundColor = '#666666';
    add_title_div.style.color = '#EFEFEF';
    add_title_div.style.float = 'right';
    add_title_div.style.margin = '4px';
    var add_title_input = generic_text_input(add_title_div.id + "_I");
    add_title_input.placeholder = 'Table Name';
    add_title_div.appendChild(add_title_input);

    actions.appendChild(add_title_div)

    content.appendChild(table);
  } else if (item === 'List') {
    // Content
    var list = document.createElement('ul');
    list.id = content.id;

    // Actions
    actions.appendChild(add_list_action_new_row(container, list));

    content.appendChild(list);
  } else if (item.startsWith('Monster')) {
    var import_action;
    var edition;

    // Edition selector
    if (item.endsWith('1')) {
      import_action = add_monster_action_import(container, content, 'pathfinder_1', 'Import from d20pfsrd.com');
      edition_action = add_list_action_edition(container, content, 'import', 'Edition: Pathfinder 1e');
    } else if (item.endsWith('2')) {
      import_action = add_monster_action_import(container, content, 'pathfinder_2', 'Import from 2e.aonprd.com');
      edition_action = add_list_action_edition(container, content, 'import', 'Edition: Pathfinder 2e');
    } else if (item.endsWith('5')) {
      import_action = add_monster_action_import(container, content, 'dnd_5', 'Import from 5e.tools');
      edition_action = add_list_action_edition(container, content, 'import', 'Edition: D&D 5e');
    }

    actions.appendChild(import_action);
    actions.appendChild(edition_action);

    var monster = create_element_monster(document.createElement('table'), item[item.length - 1]);
    content.appendChild(monster);
  } else if (item === 'Hazard2') {
      var import_action = add_hazard_action_import(container, content, 'pathfinder_2', 'Import from 2e.aonprd.com');
      var edition_action = add_list_action_edition(container, content, 'import', 'Edition: Pathfinder 2e');


    actions.appendChild(import_action);
    actions.appendChild(edition_action);
    var hazard = create_element_hazard(document.createElement('table'), item[item.length - 1]);
    content.appendChild(hazard);
  } else if (item === 'Divider') {
    // Add name for Divider
    var add_title_div = document.createElement('div');
    add_title_div.id = content.id + "_NAME";
    add_title_div.style.color = '#EFEFEF';
    add_title_div.style.margin = '4px';

    var add_title_input = generic_text_input(add_title_div.id + "_I");
    add_title_input.placeholder = 'Divider Name';
    add_title_input.style.lineHeight = "20px";
    add_title_input.style.width = "400px";
    add_title_input.style.fontSize = '24px';
    add_title_div.appendChild(add_title_input);

    content.style.textAlign = 'center';

    content.appendChild(add_title_div)
  } else if (item === 'Paragraph') {
    // Add name for Divider
    var add_paragraph_div = document.createElement('div');
    add_paragraph_div.id = content.id + "_TEXT";
    add_paragraph_div.style.color = '#EFEFEF';
    add_paragraph_div.style.margin = '4px';
    add_paragraph_div.style.padding = '10px';

    var add_paragraph_input = generic_textarea(add_paragraph_div.id + "_I");
    add_paragraph_input.placeholder = 'Type Text Here';
    add_paragraph_input.style.width = '100%';
    add_paragraph_input.style.resize = 'vertical';
    add_paragraph_div.appendChild(add_paragraph_input);

    content.style.textAlign = 'center';

    content.appendChild(add_paragraph_div)
  }
  container.appendChild(content);

  // Add everything here
  var editor = document.getElementById('editor');
  editor.appendChild(container);

  if (DEBUG) { console.log("Element Creation successful."); }
}


/*******************************************************************************************************/
/* DATA STORAGE AND RETRIEVAL **************************************************************************/
/*******************************************************************************************************/


/**Get the owner input data from the list
 * @param row The owner row
 * @return Owner information for the table
 */
function get_table_owner_data(row) {
  var owner_obj = {
    'Store Name': document.getElementById(row.id + "_STORE").value,
    'Name': document.getElementById(row.id + "_NAME").value,
    'Race': document.getElementById(row.id + "_RACE").value,
    'Gender': document.getElementById(row.id + "_GENDER").value,
    'Age': document.getElementById(row.id + "_AGE").value,
    'Trait 1': document.getElementById(row.id + "_TRAIT_1").value,
    'Trait 2': document.getElementById(row.id + "_TRAIT_2").value,
    'Description': convert_text(document.getElementById(row.id + "_DESCRIBE").value),
  }

  if (DEBUG) { console.log("Owner Complete"); }
  if (DEBUG) { console.log(owner_obj); }
  return owner_obj;
}


/**Extract all table data from the div table element
 * @param table The table produced
 * @param source Either a Store (Has Owner), Table (Has Name), or nothing
 * @return Object data for the table element
 */
function get_table_data(table, source) {
  if (DEBUG) { console.log("Exporting Table: " + table.id); }
  var table_obj = {
    'Type': source,
    'Data': []
  };

  // Get Owner
  var store = false;
  if (source === 'Store') {
    table_obj['Owner'] = get_table_owner_data(table.rows[0]);
    store = true;
  } else if (source === 'Table') {
    table_obj['Name'] = document.getElementById(table.id + "_NAME_I").value;
  }

  // Loop through items
  if (DEBUG) { console.log("Looping through item rows"); }
  for (var i = store ? 1 : 0; i < table.rows.length; i++) {
    if (DEBUG) { console.log(table.rows[i]); }
    var item = {};

    // Split handling depending on how created
    if (table.rows[i].childNodes[1].id.includes('_')) {
      // Handle Special Row
      if (DEBUG) { console.log("Special Row Encountered"); }
      var temp_id = table.rows[i].id + '_';
      item['Type'] = 'Item'
      item['Name'] = document.getElementById(temp_id + 'NAME').value;
      item['Describe'] = document.getElementById(temp_id + 'DESCRIBE').value;
      item['Text'] = document.getElementById(temp_id + 'TEXT').value;
      item['Category'] = document.getElementById(temp_id + 'CATEGORY_I').value;
      item['Descriptor'] = document.getElementById(temp_id + 'DESCRIPTOR_I').value;
    } else {
      // Handle Blank Row
      if (DEBUG) { console.log("Blank Row Encountered"); }
      item['Type'] = 'Blank';

      var children = table.rows[i].childNodes;
      for (var x = 0; x < children.length; x++) {
        if (children[x].querySelector('input')) {
          item[(x + 1).toString() + children[x].id[children[x].id.length - 2]] = document.getElementById(children[x].id + 'I').value
        }
      }
    }

    // Add to Data
    table_obj['Data'].push(item);
  }

  if (DEBUG) { console.log("Table successfully handled"); }
  if (DEBUG) { console.log(table_obj); }
  return table_obj;
}


/**Get list data in sequence
 * @param list The list DOM element
 * @return JSON of list Data
 */
function get_list_data(list) {
  if (DEBUG) { console.log("Exporting List: " + list.id); }
  var list_obj = {
    'Type': 'List',
    'Data': []
  };
  if (DEBUG) { console.log("Traversing list elements"); }

  for (var i = 0; i < list.childNodes.length; i ++) {
    var stuff = {
      'Data': document.getElementById(list.childNodes[i].id + 'I').value,
      'Bold': document.getElementById(list.childNodes[i].id + 'I_BOLD').checked,
      'Underline': document.getElementById(list.childNodes[i].id + 'I_UNDERLINE').checked
    }
    list_obj['Data'].push(stuff);
  }

  if (DEBUG) { console.log("List successfully handled"); }
  return list_obj;
}


/**Get monster data depending on edition
 * @param monster The monster table DOM element
 * @param edition Edition for the which type of export
 */
function get_monster_data(monster, edition) {
  if (DEBUG) { console.log("Exporting Monster: " + monster.id); }

  var monster_obj = {
    'Type': 'Monster',
    'Edition': edition,
    'id': monster.id + "C",
  };

  // Grab info from the first row (monster_header_content)
  var monster_header = monster.rows[0];

  monster_obj['Name'] = document.getElementById(monster_header.id + '_NAME').value;
  monster_obj['Cr'] = document.getElementById(monster_header.id + '_CR').value;
  monster_obj['Description'] = convert_text(document.getElementById(monster_header.id + '_DESCRIBE').value);
  monster_obj['Alignment'] = document.getElementById(monster_header.id + '_ALIGN').value;

  // Grab all traits for 2e monsters
  if (edition === '2') {
    var monster_trait_loc = document.getElementById(monster_header.id + '_TRAITS');
    var monster_trait_list = monster_trait_loc.querySelectorAll('input');
    if (DEBUG) { console.log(monster_trait_list); }
    monster_obj['Traits'] = [];
    monster_trait_list.forEach(function(sub) {
      monster_obj['Traits'].push(sub.value);
    });
  }

  /*******************************************************************************************************/

  var monster_info_list = monster.rows[1].childNodes[0].childNodes[0].childNodes;
  for (var i = 0; i < monster_info_list.length; i++) {
    var new_key = document.getElementById(monster_info_list[i].firstChild.id).innerText
    
    var attrib = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'];
    if (attrib.includes(new_key.substring(0, 3))) {
      monster_obj[new_key] = monster_info_list[i].lastChild.checked;
    } else {
      monster_obj[new_key] = monster_info_list[i].lastChild.value;
    }
  }

  /*******************************************************************************************************/

  var monster_stats = monster.rows[2].childNodes[0];
  var monster_stats_inputs = monster_stats.querySelectorAll('input');
  if (DEBUG) { console.log(monster_stats_inputs); }
  var attrib = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'];
  for (var i = 0; i < monster_stats_inputs.length; i++) {
    monster_obj[attrib[i]] = monster_stats_inputs[i].value;
  }

  /*******************************************************************************************************/

  var monster_action = monster.rows[3];
  var monster_action_tables = monster_action.querySelectorAll('table');
  monster_obj['Actions'] = [];
  if (DEBUG) { console.log(monster_action_tables); }

  monster_action_tables.forEach(function(action_table) {
    var action_obj = {
      'Name': document.getElementById(action_table.id + '_NAME').value,
      'Text':convert_text(document.getElementById(action_table.id + '_TEXT').value),
    };
    if (edition === '5') {
      action_obj['Legendary'] = document.getElementById(action_table.id + '_LEGEND').checked;
    }
    if (edition === '2') {
      action_obj['Cost'] = document.getElementById(action_table.id + '_COST').value;
    }

    monster_obj['Actions'].push(action_obj);
  });

  /*******************************************************************************************************/
  
  var monster_spells_tables = monster.rows[5].childNodes;
  if (DEBUG) { console.log(monster_spells_tables); }
  monster_obj['Spells'] = [];

  // Get all spell tables
  for (var i = 0; i < monster_spells_tables.length; i++) {
    var spell_tables = monster_spells_tables[i].querySelectorAll('table');

    // Loop through tables
    for (var j = 0; j < spell_tables.length; j++) {
      // Loop through Rows, skipping the Header row
      for (var k = 1; k < spell_tables[j].rows.length; k++) {
        // Set Data extration point
        var spell_row = spell_tables[j].rows[k];

        // Temp variable for extraction
        var temp_row = {};
        temp_row['List'] = [];

        temp_row['Uses'] = document.getElementById(spell_row.id + '_USES_INPUT').value;
        temp_row['Dc'] = document.getElementById(spell_row.id + '_USES_DC_INPUT').value;

        // Get all spells on this row
        var spell_list = spell_row.cells[1].querySelectorAll('div');
        for (var x = 1; x < spell_list.length; x++) {
          // Get spell Name and Link          
          var spell_list_inputs = spell_list[x].querySelectorAll('input')
          if (DEBUG) { console.log(spell_list_inputs); }
          temp_row['List'].push({
            "Name": spell_list_inputs[0].value,
            "Link": spell_list_inputs[1].value,
          })
        }

        // Add Temp variable to final output
        monster_obj['Spells'].push(temp_row);
      }
    }
  }

  /*******************************************************************************************************/

  var monster_loot = monster.rows[monster.rows.length - 1].querySelector('table');
  if (DEBUG) { console.log(monster_loot); }
  monster_obj['Treasure'] = get_table_data(monster_loot, '');
  
  if (DEBUG) { console.log("Monster successfully handled"); }
  if (DEBUG) { console.log(monster_obj); }

  return monster_obj;
}


/**Get hazard data depending on edition
 * @param hazard The hazard table DOM element
 * @param edition Edition for the which type of export
 */
function get_hazard_data(hazard, edition) {
  if (DEBUG) { console.log("Exporting Hazard: " + hazard.id); }

  var hazard_obj = {
    'Type': 'Hazard',
    'Edition': edition,
    'id': hazard.id + "C",
  };

  var hazard_header = hazard.rows[0].querySelectorAll('input');

  hazard_obj['Name'] = hazard_header[0].value;
  hazard_obj['Cr'] = hazard_header[1].value;

  /*******************************************************************************************************/

  var hazard_traits = hazard.rows[1].querySelectorAll('input');
  hazard_obj['Traits'] = [];

  for (var i = 0; i < hazard_traits.length; i++) {
    hazard_obj['Traits'].push(hazard_traits[i].value);
  }

  /*******************************************************************************************************/

  var hazard_details = hazard.rows[3].querySelectorAll('input');
  hazard_obj['Complexity'] = hazard_details[0].value;
  hazard_obj['Stealth'] = hazard_details[1].value;
  hazard_obj['Description'] = hazard_details[2].value;
  hazard_obj['Disable'] = hazard_details[3].value;

  /*******************************************************************************************************/

  var hazard_custom = hazard.rows[4].querySelectorAll('input');
  hazard_obj['Custom'] = [];

  for (var i = 0; i < hazard_custom.length; i += 2) {
    var temp = {};
    temp[hazard_custom[i].value] = hazard_custom[i + 1].value;
    hazard_obj['Custom'].push(temp);
  }

  /*******************************************************************************************************/

  if (DEBUG) { console.log("Hazard successfully handled"); }
  if (DEBUG) { console.log(hazard_obj); }

  return hazard_obj;
}


/**Saves a section of the editor element to Storage
 * @param container DOM Container to save to Storage
 */
function save_container_as_json(container) {
  // Found a store container
  if (/^S/.test(container.id)) {
    if (DEBUG) { console.log("Found a store container"); }
    var editor_element = container.childNodes[1].childNodes[0];
    var store_data_obj = get_table_data(editor_element, 'Store')
    window.sessionStorage.setItem(container.id, JSON.stringify(store_data_obj));
  }

  // Found a table container
  if (/^T/.test(container.id)) {
    if (DEBUG) { console.log("Found a table container"); }
    var editor_element = container.childNodes[1].childNodes[0];
    var table_data_obj = get_table_data(editor_element, 'Table');
    window.sessionStorage.setItem(container.id, JSON.stringify(table_data_obj));
  }

  // Found a monster container
  if (/^M/.test(container.id)) {
    if (DEBUG) { console.log("Found a monster container"); }
    var editor_element = container.childNodes[1].childNodes[0];
    var edition = document.getElementById(editor_element.id + '_EDITION');
    var monster_data_obj = get_monster_data(editor_element, edition.name[edition.name.length - 1]);
    window.sessionStorage.setItem(container.id, JSON.stringify(monster_data_obj));
  }

  // Found a hazard container
  if (/^H/.test(container.id)) {
    if (DEBUG) { console.log("Found a hazard container"); }
    var editor_element = container.childNodes[1].childNodes[0];
    var edition = document.getElementById(editor_element.id + '_EDITION');
    var hazard_data_obj = get_hazard_data(editor_element, edition.name[edition.name.length - 1])
    window.sessionStorage.setItem(container.id, JSON.stringify(hazard_data_obj));
  }

  // Found a list container
  if (/^L/.test(container.id)) {
    if (DEBUG) { console.log("Found a list container"); }
    var editor_element = container.lastElementChild.firstElementChild;
    var list_data_obj = get_list_data(editor_element);
    window.sessionStorage.setItem(container.id, JSON.stringify(list_data_obj));
  }

  // Found a divider container
  if (/^D/.test(container.id)) {
    if (DEBUG) { console.log("Found a divider container"); }
    var editor_element = container.childNodes[1];
    var divider_obj = {
      'Type': 'Divider',
      'Name': document.getElementById(editor_element.id + '_NAME_I').value,
    };
    window.sessionStorage.setItem(container.id, JSON.stringify(divider_obj));
  }

  // Found a divider container
  if (/^P/.test(container.id)) {
    if (DEBUG) { console.log("Found a paragraph container"); }
    var editor_element = container.childNodes[1];
    var divider_obj = {
      'Type': 'Paragraph',
      'Text': document.getElementById(editor_element.id + '_TEXT_I').value,
    };
    window.sessionStorage.setItem(container.id, JSON.stringify(divider_obj));
  }
}


/**Deletes all session data
 */
function refresh_page_json() {
  window.sessionStorage.clear();
}


/**Trawls editor container to save all data to session storage
 */
function save_json_from_page() {
  if (DEBUG) { console.log("Exporting containers to session storage"); }

  var session_state_obj = {
    "Name": document.getElementById('header').value,
    "Description": document.getElementById('description').value,
    "Data": [],
  }
  export_counter = 0;
  /**Export State Object
   * Name and Description is stored as strings and retrieved from header
   * Data is a list of strings, in order, for the Containers in the editor element
   *  - These strings map directly to Container IDs
   */
  // Begin exporting
  var editor_container = document.getElementById('editor').childNodes;
  if (DEBUG) { console.log("Parsing all editor objects"); }
  for(var i = 0; i < editor_container.length; i++) {
    session_state_obj['Data'].push(editor_container[i].id);
    save_container_as_json(editor_container[i]);
  }

  window.sessionStorage.setItem('state', JSON.stringify(session_state_obj));
}


/**Set storage value for page, for later retrieval
 */
function save_container_session_storage(container_id) {
  if (DEBUG) { console.log("Updating JSON for container: " + container_id); }
  var export_obj = save_container_as_json(document.getElementById(container_id));
}


/**Remove container from storage
 */
function delete_container_session_storage(container_id) {
  if (DEBUG) { console.log("Deleting JSON for container: " + container_id); }
  window.sessionStorage.removeItem(container_id);
  save_json_from_page();
}


/*******************************************************************************************************/
/* IMPORT AND EXPORT OF PAGE JSON **********************************************************************/
/*******************************************************************************************************/


/**Export data to JSON object
 * @param callback Whether or not to return or print to file
 * @return JSON data for the webpage 
 */
function export_json(callback) {
  if (DEBUG) { console.log("Exporting containers to JSON"); }
  // Clear export objects
  var export_state_obj = {
    "Name": document.getElementById('header').value,
    "Description": convert_text(document.getElementById('description').value),
    "Data": [],
  }
  export_counter = 0;

  // Save all to JSON
  refresh_page_json();
  save_json_from_page();
  var session_obj = JSON.parse(window.sessionStorage.getItem('state'));
  if (DEBUG) { console.log("Session Containers:"); }
  if (DEBUG) { console.log(session_obj['Data']); }

  // Transfer to single object
  session_obj['Data'].forEach(function(key) {
    if (DEBUG) { console.log("Container JSON for: " + key); }
    var session_container_obj = JSON.parse(window.sessionStorage.getItem(key));
    if (DEBUG) { console.log(session_container_obj); }
    export_state_obj['Data'].push(session_container_obj);
  });
  
  if (DEBUG) { console.log("Final Export Data"); }
  if (DEBUG) { console.log(export_state_obj); }
  if (!callback) {
    // Save to file
    var textFile = null
    var new_doc_blob = new Blob([JSON.stringify(export_state_obj, null, 2)], {type: 'text/plain;charset=utf-8'});
    saveAs(new_doc_blob, document.getElementById("header").value + '.custom.json');
  } else {
    return export_state_obj;
  }
}


/**Get all data from session in a single JSON object
 * @return Exportable JSON from session storage
 */
function export_session_json() {
  if (!window.sessionStorage.getItem('state')) {
    (async () => {
      // Toast Message
      var toast = document.createElement('div');
      toast.style.backgroundColor = "#E34D4D";
      toast.style.position = "fixed";
      toast.style.top = "40px";
      toast.style.left = "40px";
      toast.style.width = "250px";
      toast.id = "toast";
      toast.style.padding = "10px 20px";

      toast.appendChild(document.createTextNode("Unable to load from Storage"));

      var header_img = document.getElementById("header_img");
      header_img.appendChild(toast);

      setTimeout(function(){
        toast.parentNode.removeChild(toast);
      }, 5000);
    })()
    return null;
  }
  if (DEBUG) { console.log("Exporting JSON from storage"); }
  var session_obj = JSON.parse(window.sessionStorage.getItem('state'));

  var export_state_obj = {
    "Name": session_obj['Name'],
    "Description": convert_text(session_obj['Description']),
    "Data": [],
  }

  // Get all keys and remove data from 
  var all_keys = Object.keys(window.sessionStorage);
  all_keys.splice(all_keys.indexOf('state'), 1);

  for (var i = 0; i < all_keys.length; i++) {
    export_state_obj['Data'].push(JSON.parse(window.sessionStorage.getItem(all_keys[i])));
  }

  return export_state_obj;
}


/**Import everything from JSON object
 */
function import_page() {
  var string = prompt("Import JSON", '');
  if (string == null) {
    alert("Invalid data entered.")
    return
  }

  // Test whether the imported string is valid
  if (DEBUG) { console.log("Raw Import String"); }
  if (DEBUG) { console.log(string); }
  var new_json = {};
  try {
    new_json = JSON.parse(string);
  } catch (e) {
    alert('Invalid Import String!')
    return
  }

  if (DEBUG) { console.log("JSON String validated. Beginning Document Change"); }
  update_page(new_json);
  save_json_from_page();
}

