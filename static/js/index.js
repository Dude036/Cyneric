let DEBUG = true;
let latest_store = 0;
let latest_store_rows = 0;
let latest_table = 0;
let latest_table_rows = 0;
let latest_list = 0;
let latest_list_rows = 0;
let latest_monster = 0;
let latest_monster_rows = 0;
let latest_monster_trait = 0;
let latest_monster_action = 0;
let latest_hazard = 0;
let latest_hazard_trait = 0;
let latest_hazard_custom = 0;

// Export Variables
let export_obj = {
	"Name": "",
	"Description": "",
	"Monsters": [],
	"Stores": [],
	"Tables": [],
	"Lists": [],
	"Hazards": [],
}
let export_counter = 0;


/**Dealing with Textarea Height
 * @param element Textarea DOM element
 */
function calcHeight(element) {
	var numberOfLineBreaks = (element.value.match(/\n/g) || []).length;
	// min-height + lines x line-height + padding + border
	var newHeight = 20 + numberOfLineBreaks * 20 + 12 + 2;

	element.style.height = newHeight + "px";
}


// Add variable height for description
let textarea = document.getElementById("description");
textarea.addEventListener("keyup", function() { calcHeight(textarea) });


/**Create the Parent Container for Tables
 * @param element Primary child element, the table
 * @return Fully formed container for Table elements
 */
function editor_container_table(element) {
	if (DEBUG) { console.log("Begin Table Container Creation"); }

	var container = document.createElement("div");
	container.id = element.id + "C";
	container.width = '100%';

	// Add Sub Element Methods
	// Add New Row divs
	var add_row_div = document.createElement('div');
	add_row_div.id = container.id + "_ADD";
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

		// Delete Row
		var add_delete = new_row.insertCell(0);
		add_delete.style.float = 'right';
		add_delete.style.width = '8px';
		add_delete.style.backgroundColor = '#C00000';
		add_delete.style.color = '#EFEFEF';
		add_delete.innerHTML = "<b>X</b>";

		// Add Delete row Method
		add_delete.onclick = function() {
			if (confirm("Are you sure you want to delete this row?")) {
				if (DEBUG) { console.log("Deleting Row"); }
				new_row.parentNode.removeChild(new_row);
				if (DEBUG) { console.log("Row Successfully Deleted"); }
			}
		}

		// Detail Style
		var add_detail = new_row.insertCell(1);
		add_detail.style.float = 'right';
		add_detail.style.width = '55px';
		add_detail.style.backgroundColor = '#500050';
		add_detail.style.color = '#EFEFEF';
		add_detail.innerHTML = "Add 'td'";

		// Setup function for adding td Cell
		add_detail.onclick = function() {
			var new_cell = new_row.insertCell(new_row.cells.length-3);
			if (DEBUG) { console.log(new_row.id) }
			new_cell.id = new_row.id + 'C' + (new_row.cells.length - 3);
			new_cell.style.backgroundColor = "#FFFFFF";

			var new_input = document.createElement('input');
			new_input.type = 'text';
			new_input.name = new_cell.id + "I";
			new_input.id = new_cell.id + "I";

			new_cell.appendChild(new_input);
		}

		var add_header = new_row.insertCell(2);

		// Header Style
		add_header.style.float = 'right';
		add_header.style.width = '55px';
		add_header.style.backgroundColor = '#005050';
		add_header.style.color = '#EFEFEF';
		add_header.innerHTML = "Add 'th'";

		// Setup function for adding th Cell
		add_header.onclick = function() {
			var new_cell = new_row.insertCell(new_row.cells.length-3);
			new_cell.id = new_row.id + 'H' + (new_row.cells.length - 3);
			new_cell.style.backgroundColor = "#CFCFCF";

			var new_input = document.createElement('input');
			new_input.type = 'text';
			new_input.name = new_cell.id + "I";
			new_input.id = new_cell.id + "I";

			new_cell.appendChild(new_input);
		}
	};

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

		// Delete Row
		var add_delete = item_row.insertCell(0);
		add_delete.style.float = 'right';
		add_delete.style.width = '8px';
		add_delete.style.backgroundColor = '#C00000';
		add_delete.style.color = '#EFEFEF';
		add_delete.innerHTML = "<b>X</b>";

		// Add Delete row Method
		add_delete.onclick = function() {
			if (confirm("Are you sure you want to delete this row?")) {
				if (DEBUG) { console.log("Deleting Row"); }
				item_row.parentNode.removeChild(item_row);
				if (DEBUG) { console.log("Row Successfully Deleted"); }
			}
		}

		// Item additions
		var item_descriptor_cell = item_row.insertCell(0);
		item_descriptor_cell.id = item_row.id + "_Descriptor";

		var item_descriptor = document.createElement('input');
		item_descriptor.id = item_descriptor_cell.id + "_I";
		item_descriptor.placeholder = 'Descriptor';
		item_descriptor_cell.appendChild(item_descriptor);

		var item_category_cell = item_row.insertCell(0);
		item_category_cell.id = item_row.id + "_Category";

		var item_category = document.createElement('input');
		item_category.id = item_category_cell.id + "_I";
		item_category.placeholder = 'Category';
		item_category_cell.appendChild(item_category);

		// Main Item info
		var item_data_cell = item_row.insertCell(0);
		item_data_cell.id = item_row.id + "_Data"

		var item_name = document.createElement('input');
		item_name.type = 'text';
		item_name.name = item_row.id + "_Name";
		item_name.id = item_row.id + "_Name";
		item_name.placeholder = 'Name';
		item_data_cell.appendChild(item_name);

		item_data_cell.appendChild(document.createElement('br'));

		var item_describe = document.createElement('input');
		item_describe.type = 'text';
		item_describe.name = item_row.id + "_Describe";
		item_describe.id = item_row.id + "_Describe";
		item_describe.placeholder = 'Description';
		item_data_cell.appendChild(item_describe);

		item_data_cell.appendChild(document.createElement('br'));

		var item_text = document.createElement('textarea');
		item_text.name = item_row.id + "_Text";
		item_text.id = item_row.id + "_Text";
		item_text.placeholder = 'Long Description';
		item_text.style.lineHeight = "20px"
		item_text.addEventListener("keyup", function() { calcHeight(item_text) });
		item_data_cell.appendChild(item_text);
	}

	container.appendChild(add_row_div);
	container.appendChild(add_item_div);
	
	// Add Movement within local div?
	container.appendChild(element);
	return container;
}


/** Adds list item, and its input, to a parent list.
 * @param parent Parent list
 * @param descriptor The descriptor for the placeholder text and id
 * @param add_id The id that will be referenced during export
 * @return Sub-Element for owner information
 */
function sub_list_element(parent, descriptor, add_id) {
	var new_input = document.createElement('li');
	var new_input_input = document.createElement('input');
	new_input_input.id = add_id + "_" + descriptor.toUpperCase();
	new_input_input.type = 'text';
	new_input_input.placeholder = 'Owner ' + descriptor;
	new_input.appendChild(new_input_input);
	parent.appendChild(new_input);
}


/**Add list settings when creating a list element
 * @param parent_obj LI container
 * @param add_id Matching ID for a list's modifier
 */
function add_list_settings(parent_obj, add_id) {
	// Bold
	var add_bold = document.createElement('input');
	add_bold.type = 'checkbox';
	add_bold.id = add_id + '_BOLD'
	add_bold.name = add_id + '_BOLD'

	var add_bold_label = document.createElement('label');
	add_bold_label.htmlFor = add_id + '_BOLD'
	add_bold_label.innerHTML = "<b>Bold</b>"

	parent_obj.appendChild(add_bold);
	parent_obj.appendChild(add_bold_label);

	// Underline
	var add_underline = document.createElement('input');
	add_underline.type = 'checkbox';
	add_underline.id = add_id + '_UNDERLINE'
	add_underline.name = add_id + '_UNDERLINE'

	var add_underline_label = document.createElement('label');
	add_underline_label.htmlFor = add_id + '_UNDERLINE'
	add_underline_label.innerHTML = "<u>Underline</u>"

	parent_obj.appendChild(add_underline);
	parent_obj.appendChild(add_underline_label);
}


/**Create the Parent Container for List
 * @param element Primary child element, the list
 */
function editor_container_list(element) {
	if (DEBUG) { console.log("Begin List Container Creation"); }

	// Container options
	var container = document.createElement("div");
	container.id = element.id + "C";
	container.width = '100%';

	// Add Styling
	var add_row_div = document.createElement('div');
	add_row_div.id = container.id + "_ADD";
	add_row_div.style.backgroundColor = '#500050';
	add_row_div.style.color = '#EFEFEF';
	add_row_div.style.float = 'right';
	add_row_div.style.padding = '5px';
	add_row_div.innerHTML = "Add Blank Row";

	add_row_div.onclick = function() {
		var new_row = document.createElement('li');
		new_row.id = element.id + "R" + latest_list_rows;
		latest_list_rows++;
		
		var new_row_input = document.createElement('input');
		new_row_input.type = 'Text';
		new_row_input.id = new_row.id + 'I'
		new_row_input.placeholder = 'Text';

		new_row.appendChild(new_row_input);

		add_list_settings(new_row, new_row.id + 'I');

		element.appendChild(new_row);
	}

	// Delete Styling
	var add_delete_div = document.createElement('div');
	add_delete_div.style.float = 'right';
	add_delete_div.style.padding = '5px';
	add_delete_div.style.backgroundColor = '#C00000';
	add_delete_div.style.color = '#EFEFEF';
	add_delete_div.innerHTML = "Delete List";
	add_delete_div.id = container.id + "_DELETE";

	// Delete List Function
	add_delete_div.onclick = function() {
		if (confirm("Delete List?")) {
			if (DEBUG) { console.log("Deleting List"); }
			container.parentNode.removeChild(container);
			if (DEBUG) { console.log("List successfully deleted"); }
		}
	}

	container.appendChild(add_delete_div);
	container.appendChild(add_row_div);

	container.appendChild(element);
	return container;
}


/**Create the Parent Container for Monsters
 * @param element Primary child element, the table
 * @param edition Child Element's edition
 * @return Fully formed container for Monster Table elements
 */
function editor_container_monster(element, edition) {
	if (DEBUG) { console.log("Begin Monster Container Creation"); }

	// Container options
	var container = document.createElement("div");
	container.id = element.id + "C";
	container.width = '100%';

	// Add monster information
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

	// Delete Styling
	var add_delete_div = document.createElement('div');
	add_delete_div.style.float = 'right';
	add_delete_div.style.padding = '5px';
	add_delete_div.style.backgroundColor = '#C00000';
	add_delete_div.style.color = '#EFEFEF';
	add_delete_div.innerHTML = "Delete Monster";
	add_delete_div.id = container.id + "_DELETE";

	// Delete List Function
	add_delete_div.onclick = function() {
		if (confirm("Delete Monster?")) {
			if (DEBUG) { console.log("Deleting Monster"); }
			container.parentNode.removeChild(container);
			if (DEBUG) { console.log("Monster successfully deleted"); }
		}
	}

	container.appendChild(add_delete_div);
	container.appendChild(add_edition_div);

	container.appendChild(element);
	return container;
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

	// Style
	store.style.width = "100%";
	store.style.borderBottom = "1px solid black";
	store.style.marginBottom = "20px";
	// store.style.padding = '5px'

	// Add sub elements for Store
	var owner_container = document.createElement('tr');
	owner_container.id = store.id + "_OWNER";

	// Store Name
	var owner_store_name = document.createElement('input');
	owner_store_name.id = owner_container.id + "_STORE";
	owner_store_name.type = 'text';
	owner_store_name.placeholder = 'Store Name (Type)';
	owner_store_name.value = '';
	owner_store_name.style.fontSize = '24px';

	owner_container.appendChild(owner_store_name);
	owner_container.appendChild(document.createElement('br'));
	// Owner Name
	var owner_name = document.createElement('input');
	owner_name.id = owner_container.id + "_NAME";
	owner_name.type = 'text';
	owner_name.placeholder = 'Owner Name';
	owner_name.value = '';
	
	owner_container.appendChild(owner_name);

	// Descriptions
	var owner_description = document.createElement('ul');

	// Race
	sub_list_element(owner_description, 'Race', owner_container.id);
	sub_list_element(owner_description, 'Gender', owner_container.id);
	sub_list_element(owner_description, 'Age', owner_container.id);
	sub_list_element(owner_description, 'Trait_1', owner_container.id);
	sub_list_element(owner_description, 'Trait_2', owner_container.id);

	owner_container.appendChild(owner_description);

	// Description
	owner_description_text = document.createElement('textarea');
	owner_description_text.placeholder = 'Owner Description'
	owner_description_text.style.width = '90%';
	owner_description_text.style.lineHeight = "20px"
	owner_description_text.addEventListener("keyup", function() { calcHeight(owner_description_text) });
	owner_description_text.id = owner_container.id + "_DESCRIBE";

	owner_container.appendChild(owner_description_text)

	// Add
	store.appendChild(owner_container);

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
			temp_trait.style.justfyContent = 'flex-start';
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
				hazard_trait_loc.innerHTML = '';
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
	monster_description_input.style.lineHeight = "20px"
	monster_description_input.addEventListener("keyup", function() { calcHeight(monster_description_input) });
	monster_description.appendChild(monster_description_input);

	monster_header_content.appendChild(monster_description);
	monster_header.appendChild(monster_header_content);
	monster.appendChild(monster_header);

	/*******************************************************************************************************/

	var monster_info = document.createElement('tr');
	monster_info.id = monster.id + 'R2';
	var monster_info_content = document.createElement('div');
	
	// Monster Base Information
	var monster_info_list = document.createElement('ul');
	monster_info_list.style.columnCount = 2;
	var monster_hp = document.createElement('li');
	var monster_hp_input = document.createElement('input');
	monster_hp_input.id = monster_header.id + '_HP';
	monster_hp_input.placeholder = 'HP';
	monster_hp.appendChild(monster_hp_input);
	monster_info_list.appendChild(monster_hp);

	var monster_speed = document.createElement('li');
	var monster_speed_input = document.createElement('input');
	monster_speed_input.id = monster_header.id + '_SPEED'
	monster_speed_input.placeholder = 'Speed'
	monster_speed.appendChild(monster_speed_input);
	monster_info_list.appendChild(monster_speed);

	var monster_size = document.createElement('li');
	var monster_size_input = document.createElement('input');
	monster_size_input.id = monster_header.id + '_SIZE'
	monster_size_input.placeholder = 'Size'
	monster_size.appendChild(monster_size_input);
	monster_info_list.appendChild(monster_size);

	var monster_ac = document.createElement('li');
	var monster_ac_input = document.createElement('input');
	monster_ac_input.id = monster_header.id + '_AC'
	monster_ac_input.placeholder = 'AC'
	monster_ac.appendChild(monster_ac_input);
	monster_info_list.appendChild(monster_ac);

	// Special AC for Pathfinder 1
	if (edition == "1") {
		var monster_touch_ac = document.createElement('li');
		var monster_touch_ac_input = document.createElement('input');
		monster_touch_ac_input.id = monster_header.id + '_TOUCH_AC'
		monster_touch_ac_input.placeholder = 'Touch'
		monster_touch_ac.appendChild(monster_touch_ac_input);
		monster_info_list.appendChild(monster_touch_ac);

		var monster_flat_ac = document.createElement('li');
		var monster_flat_ac_input = document.createElement('input');
		monster_flat_ac_input.id = monster_header.id + '_FLAT_AC'
		monster_flat_ac_input.placeholder = 'Flat'
		monster_flat_ac.appendChild(monster_flat_ac_input);
		monster_info_list.appendChild(monster_flat_ac);

		var monster_cmd = document.createElement('li');
		var monster_cmd_input = document.createElement('input');
		monster_cmd_input.id = monster_header.id + '_CMD'
		monster_cmd_input.placeholder = 'CMD'
		monster_cmd.appendChild(monster_cmd_input);
		monster_info_list.appendChild(monster_cmd);

		var monster_cmb = document.createElement('li');
		var monster_cmb_input = document.createElement('input');
		monster_cmb_input.id = monster_header.id + '_CMB'
		monster_cmb_input.placeholder = 'CMB'
		monster_cmb.appendChild(monster_cmb_input);
		monster_info_list.appendChild(monster_cmb);
	}
	
	//  Pathfinder Saves
	if (edition == "1" || edition == "2") {
		var monster_fort_save = document.createElement('li');
		var monster_fort_save_input = document.createElement('input');
		monster_fort_save_input.id = monster_header.id + '_FORT_SAVE'
		monster_fort_save_input.placeholder = 'Fortitude Save'
		monster_fort_save.appendChild(monster_fort_save_input);
		monster_info_list.appendChild(monster_fort_save);

		var monster_will_save = document.createElement('li');
		var monster_will_save_input = document.createElement('input');
		monster_will_save_input.id = monster_header.id + '_WILL_SAVE'
		monster_will_save_input.placeholder = 'Will Save'
		monster_will_save.appendChild(monster_will_save_input);
		monster_info_list.appendChild(monster_will_save);

		var monster_ref_save = document.createElement('li');
		var monster_ref_save_input = document.createElement('input');
		monster_ref_save_input.id = monster_header.id + '_REF_SAVE'
		monster_ref_save_input.placeholder = 'Reflex Save'
		monster_ref_save.appendChild(monster_ref_save_input);
		monster_info_list.appendChild(monster_ref_save);
	} else if (edition == '5') {
		// Saves for 5e
		var monster_save_1 = document.createElement('li');
		var monster_str_save = document.createElement('input');
		monster_str_save.type = 'checkbox';
		monster_str_save.id = monster_header.id  + '_STR_SAVE'
		monster_str_save.name = monster_header.id  + '_STR_SAVE'

		var monster_str_save_label = document.createElement('label');
		monster_str_save_label.htmlFor = monster_header.id  + '_STR_SAVE_LABEL'
		monster_str_save_label.innerHTML = "<b>STR Save</b>"

		monster_save_1.appendChild(monster_str_save);
		monster_save_1.appendChild(monster_str_save_label);

		var monster_dex_save = document.createElement('input');
		monster_dex_save.type = 'checkbox';
		monster_dex_save.id = monster_header.id  + '_DEX_SAVE'
		monster_dex_save.name = monster_header.id  + '_DEX_SAVE'

		var monster_dex_save_label = document.createElement('label');
		monster_dex_save_label.htmlFor = monster_header.id  + '_DEX_SAVE_LABEL'
		monster_dex_save_label.innerHTML = "<b>DEX Save</b>"

		monster_save_1.appendChild(monster_dex_save);
		monster_save_1.appendChild(monster_dex_save_label);

		monster_info_list.appendChild(monster_save_1);

		var monster_save_2 = document.createElement('li');
		var monster_con_save = document.createElement('input');
		monster_con_save.type = 'checkbox';
		monster_con_save.id = monster_header.id  + '_CON_SAVE'
		monster_con_save.name = monster_header.id  + '_CON_SAVE'

		var monster_con_save_label = document.createElement('label');
		monster_con_save_label.htmlFor = monster_header.id  + '_CON_SAVE_LABEL'
		monster_con_save_label.innerHTML = "<b>CON Save</b>"

		monster_save_2.appendChild(monster_con_save);
		monster_save_2.appendChild(monster_con_save_label);

		var monster_int_save = document.createElement('input');
		monster_int_save.type = 'checkbox';
		monster_int_save.id = monster_header.id  + '_INT_SAVE'
		monster_int_save.name = monster_header.id  + '_INT_SAVE'

		var monster_int_save_label = document.createElement('label');
		monster_int_save_label.htmlFor = monster_header.id  + '_INT_SAVE_LABEL'
		monster_int_save_label.innerHTML = "<b>INT Save</b>"

		monster_save_2.appendChild(monster_int_save);
		monster_save_2.appendChild(monster_int_save_label);

		monster_info_list.appendChild(monster_save_2);

		var monster_save_3 = document.createElement('li');
		var monster_wis_save = document.createElement('input');
		monster_wis_save.type = 'checkbox';
		monster_wis_save.id = monster_header.id  + '_WIS_SAVE'
		monster_wis_save.name = monster_header.id  + '_WIS_SAVE'

		var monster_wis_save_label = document.createElement('label');
		monster_wis_save_label.htmlFor = monster_header.id  + '_WIS_SAVE_LABEL'
		monster_wis_save_label.innerHTML = "<b>WIS Save</b>"

		monster_save_3.appendChild(monster_wis_save);
		monster_save_3.appendChild(monster_wis_save_label);

		var monster_cha_save = document.createElement('input');
		monster_cha_save.type = 'checkbox';
		monster_cha_save.id = monster_header.id  + '_CHA_SAVE'
		monster_cha_save.name = monster_header.id  + '_CHA_SAVE'

		var monster_cha_save_label = document.createElement('label');
		monster_cha_save_label.htmlFor = monster_header.id  + '_CHA_SAVE_LABEL'
		monster_cha_save_label.innerHTML = "<b>CHA Save</b>"

		monster_save_3.appendChild(monster_cha_save);
		monster_save_3.appendChild(monster_cha_save_label);

		monster_info_list.appendChild(monster_save_3);
	}

	// Skills
	var monster_skills = document.createElement('li');
	var monster_skills_input = document.createElement('input');
	monster_skills_input.id = monster_header.id + '_SKILLS';
	monster_skills_input.placeholder = 'Skills';
	monster_skills.appendChild(monster_skills_input);
	monster_info_list.appendChild(monster_skills);


	// Incoming damage modifiers
	var monster_dam_immune = document.createElement('li');
	var monster_dam_immune_input = document.createElement('input');
	monster_dam_immune_input.id = monster_header.id + '_DAM_IMMUNE';
	monster_dam_immune_input.placeholder = 'Damage Immunities';
	monster_dam_immune.appendChild(monster_dam_immune_input);
	monster_info_list.appendChild(monster_dam_immune);

	var monster_dam_resist = document.createElement('li');
	var monster_dam_resist_input = document.createElement('input');
	monster_dam_resist_input.id = monster_header.id + '_DAM_RESIST';
	monster_dam_resist_input.placeholder = 'Damage Resistances';
	monster_dam_resist.appendChild(monster_dam_resist_input);
	monster_info_list.appendChild(monster_dam_resist);

	var monster_dam_weak = document.createElement('li');
	var monster_dam_weak_input = document.createElement('input');
	monster_dam_weak_input.id = monster_header.id + '_DAM_WEAK';
	monster_dam_weak_input.placeholder = 'Damage Weakness';
	monster_dam_weak.appendChild(monster_dam_weak_input);
	monster_info_list.appendChild(monster_dam_weak);

	// Senses / Language
	var monster_sense = document.createElement('li');
	var monster_sense_input = document.createElement('input');
	monster_sense_input.id = monster_header.id + '_SENSE';
	monster_sense_input.placeholder = 'Senses';
	monster_sense.appendChild(monster_sense_input);
	monster_info_list.appendChild(monster_sense);

	var monster_language = document.createElement('li');
	var monster_language_input = document.createElement('input');
	monster_language_input.id = monster_header.id + '_LANGUAGE';
	monster_language_input.placeholder = 'Languages';
	monster_language.appendChild(monster_language_input);
	monster_info_list.appendChild(monster_language);

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
		temp_td_input.id = monster_header.id + '_' + stats[i];
		temp_td_input.name = monster_header.id + '_' + stats[i];
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
	monster_action_container.id = monster_header.id + '_ACTIONS';

	var monster_action_add = document.createElement('div');
	monster_action_add.style.backgroundColor = '#030303';
	monster_action_add.style.color = '#EFEFEF';
	monster_action_add.style.float = 'right'
	monster_action_add.style.padding = '5px'
	monster_action_add.id = monster_header.id + '_ACTION_ADD';
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
			console.log('Value: ' + monster_action_cost.value);

			temp_action_header.appendChild(monster_action_cost_label);
			temp_action_header.appendChild(monster_action_cost);
		}

		// Detail Info
		var temp_action_info = document.createElement('tr');
		var temp_action_info_input = document.createElement('textarea');
		temp_action_info_input.id = temp_action.id  + '_TEXT'
		temp_action_info_input.placeholder = 'Action Details';
		temp_action_info_input.style.width = '90%';
		temp_action_info_input.style.lineHeight = "20px"
		temp_action_info_input.addEventListener("keyup", function() { calcHeight(temp_action_info_input) });
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
	monster_action_clear.id = monster_header.id + '_ACTION_CLEAR';
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

	var monster_loot = document.createElement('tr');
	var monster_loot_table = document.createElement('table');

	monster_loot_table.id = "MT" + latest_table
	latest_table += 1;

	// Style
	monster_loot_table.style.width = "100%";
	monster_loot_table.style.borderBottom = "1px solid black";
	monster_loot_table.style.marginBottom = "20px";

	var monster_loot_container = editor_container_table(monster_loot_table);

	monster_loot.id = monster.id + 'R5';

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
		temp_trait.style.justfyContent = 'flex-start';
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

	if (item == "Store") {
		// Init
		var store = create_element_store(document.createElement('table'));
		
		var parent = document.getElementById("Stores");
		parent.appendChild(editor_container_table(store));
	} else if (item == "Table") {
		// Init
		var table = document.createElement('table');
		table.id = "T" + latest_table
		latest_table += 1;

		// Style
		table.style.width = "100%";
		table.style.borderBottom = "1px solid black";
		table.style.marginBottom = "20px";

		// Add
		var parent = document.getElementById("Tables");
		parent.appendChild(editor_container_table(table));
	} else if (item.startsWith("Monster")) {
		// Init
		var monster = create_element_monster(document.createElement('table'), item[item.length - 1]);

		// Add
		var parent = document.getElementById("Monsters");
		parent.appendChild(editor_container_monster(monster, item[item.length - 1]));
	} else if (item == "List") {
		// Init
		var list = document.createElement('ul');
		list.id = "L" + latest_list
		latest_list += 1;

		// Style
		list.style.width = "100%";
		list.marginBottom = '60px';

		// Add
		var parent = document.getElementById("Lists");
		parent.appendChild(editor_container_list(list));
	} else if (item.startsWith('Hazard')) {
		var hazard = create_element_hazard(document.createElement('table'), item[item.length - 1]);

		var parent = document.getElementById("Hazards");
		parent.appendChild(editor_container_hazard(hazard, item[item.length - 1]));
	} else {
		alert("Invalid create_element parameter.");
		return;
	}

	if (DEBUG) { console.log("Element Creation successful"); }
}


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
 * @param store Bool, True if table is a store
 * @return Object data for the table element
 */
function get_table_data(table, store) {
	if (DEBUG) { console.log("Exporting Table: " + table.id); }
	var table_obj = {
		'Data': []
	};

	// Get Owner
	if (store) {
		table_obj['Owner'] = get_table_owner_data(table.rows[0]);
	}

	// Loop through items
	if (DEBUG) { console.log("Looping through item rows"); }
	for (var i = store ? 1 : 0; i < table.rows.length; i++) {
		if (DEBUG) { console.log(table.rows[i]); }
		var item = {};

		// Split handling depending on how created
		if (table.rows[i].childNodes[0].id.includes('_')) {
			// Handle Special Row
			if (DEBUG) { console.log("Special Row Encountered"); }
			var temp_id = table.rows[i].id + '_';
			item['Type'] = 'Item'
			item['Name'] = document.getElementById(temp_id + 'Name').value;
			item['Describe'] = document.getElementById(temp_id + 'Describe').value;
			item['Text'] = document.getElementById(temp_id + 'Text').value;
			item['Category'] = document.getElementById(temp_id + 'Category_I').value;
			item['Descriptor'] = document.getElementById(temp_id + 'Descriptor_I').value;
		} else {
			// Handle Blank Row
			if (DEBUG) { console.log("Blank Row Encountered"); }
			item['Type'] = 'Blank';

			var children = table.rows[i].childNodes;
			for (var x = 0; x < children.length; x++) {
				if (children[x].id !== '') {
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
	var list_obj = [];
	if (DEBUG) { console.log("Traversing list elements"); }

	for (var i = 0; i < list.childNodes.length; i ++) {
		var stuff = {
			'Data': document.getElementById(list.childNodes[i].id + 'I').value,
			'Bold': document.getElementById(list.childNodes[i].id + 'I_BOLD').checked,
			'Underline': document.getElementById(list.childNodes[i].id + 'I_UNDERLINE').checked
		}
		list_obj.push(stuff);
	}

	if (DEBUG) { console.log("List successfully handled"); }
	return list_obj;
}


/**Convert special ID string to object usable strings
 * @param special Special string to convert
 * @return ID usable strings
 */
function convert_special_to_id(special) {
	var new_str = '';
	special = special.slice(special.indexOf('_') + 1);
	special.split('_').forEach(function(sub) {
		new_str += sub[0] + sub.substring(1).toLowerCase();
	});

	return new_str;
}


/**Get monster data depending on edition
 * @param monster The monster table DOM element
 * @param edition Edition for the which type of export
 */
function get_monster_data(monster, edition) {
	if (DEBUG) { console.log("Exporting Monster: " + monster.id); }

	var monster_obj = {
		'Edition': edition,
	};

	// Grab info from the first row (monster_header_content)
	var monster_header = monster.rows[0];

	monster_obj['Name'] = document.getElementById(monster_header.id + '_NAME').value;
	monster_obj['Cr'] = document.getElementById(monster_header.id + '_CR').value;
	monster_obj['Description'] = convert_text(document.getElementById(monster_header.id + '_DESCRIBE').value);
	monster_obj['Alignment'] = document.getElementById(monster_header.id + '_ALIGN').value;

	// Grab all traits for 2e monsters
	if (edition === '2') {
		var monster_trait_list = document.getElementById(monster_header.id + '_TRAITS').childNodes;
		if (DEBUG) { console.log(monster_trait_list); }
		monster_obj['Traits'] = [];
		monster_trait_list.forEach(function(sub) {
			var text = sub.innerText;
			text = text.slice(0, text.lastIndexOf(' '))
			monster_obj['Traits'].push(text);
		});
	}

	/*******************************************************************************************************/

	var monster_info = monster.rows[1].childNodes[0];
	var monster_info_inputs = monster_info.querySelectorAll('input');
	if (DEBUG) { console.log(monster_info_inputs); }
	for (var i = 0; i < monster_info_inputs.length; i++) {
		var new_key = convert_special_to_id(monster_info_inputs[i].id)
		if (new_key.startsWith('Str') || new_key.startsWith('Dex') || new_key.startsWith('Con') || new_key.startsWith('Int') || new_key.startsWith('Wis') || new_key.startsWith('Cha')) {
			monster_obj[new_key] = monster_info_inputs[i].checked;
		} else {
			monster_obj[new_key] = monster_info_inputs[i].value;
		}
	}

	/*******************************************************************************************************/

	var monster_stats = monster.rows[2].childNodes[0];
	var monster_stats_inputs = monster_stats.querySelectorAll('input');
	if (DEBUG) { console.log(monster_stats_inputs); }
	for (var i = 0; i < monster_stats_inputs.length; i++) {
		monster_obj[convert_special_to_id(monster_stats_inputs[i].id)] = monster_stats_inputs[i].value;
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
	var monster_loot = monster.rows[4].querySelector('table');
	console.log(monster_loot);
	monster_obj['Treasure'] = get_table_data(monster_loot, false);
	

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
		'Edition': edition,
	};

	var hazard_header = hazard.rows[0].querySelectorAll('input');

	console.log(hazard_header);
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


/**Export everything into an object, then turn the object data into a usable html file
 */
function export_page() {
	if (DEBUG) { console.log("Exporting Page"); }
	// Clear export object
	export_obj = export_json(true);

	/************************************************************************************************/

	// Create new Document for printing
	// Going with a simple String to be coppied
	// Boiler plate CSS header stuffs
	var new_doc = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Custom HTML</title><style>body{max-width:1000px;margin-left:auto;margin-right:auto;padding-left:5px;padding-right:5px}html{font-family:Arial}h1,h2{color:#000;text-align:center}.center{text-align:center}.bold{font-weight:700}.emp{font-style:italic}table{border:1px solid #000;border-spacing:0}table tr th{background-color:gray;color:#fff;padding:5px}table tr td{margin:0;padding:5px}.text-xs{font-size:12px}.text-sm{font-size:14px}.text-md{font-size:18px}.text-lg{font-size:24px}.text-xl{font-size:32px}.wrapper-box{width:100%;border:2px solid #000;margin-bottom:60px padding:5px;}.inventory-table{width:100%;}.suggestion{padding:2px 0;margin:0;list-style:none}.suggestion li{border:1px solid #000;background-color:#ddd;padding:2px 4px;margin:5px 10px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.suggestion li:active{background-color:#404040}.suggestion li:hover{background-color:grey}.attacks{display:flex;flex-wrap:wrap;align-items:flex-start;width:100%;padding-top:10px;padding-bottom:20px}.attacks table{width:44%;margin-left:3%;margin-right:3%;margin-bottom:1%}.header{background-color:#f1f1f1;position:fixed;top:0;left:0;padding:5px 5px}.header ul{display:none;list-style-type:none;padding-left:10px;margin-top:0}.header a{float:left;color:#000;text-align:center;text-decoration:none;padding:5px 5px}.header a:hover{background-color:#ddd}.header a.active{background-color:#02f}.crit tr:nth-child(even){background-color:#eee}.link{text-align:center}.link li{padding-bottom:10px}.link a{border:1px solid #000;width:60%;text-decoration:none;color:#222;background-color:#ddd;padding:3px 3px 3px 3px}.link a:hover{background-color:#222;color:#ddd}.sidebar{float:left;position:fixed;top:0;right:0;margin:5px}.sidebar_object{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;padding:10px 20px;border-style:solid;border:2px;background-color:#efefef}.sidebar_object:hover{background-color:#cfcfcf}.sidebar_object:active{background-color:#0000cf;color:#efefef}.traits {padding: 5px 2px;width: 95%;margin: 15px 10px;display: flex;flex-wrap: wrap;align-items: flex-start;}.traits_obj {justfy-content: flex-start;width: 23%;margin: 0px 10px;padding: 3px;background-color:#666666;color:#EFEFEF;}@media only screen and (max-width:600px){.header a{float:none;display:block;text-align:left;font-size:20px}.header img{height:50px;width:50px}.header-right{float:none}}</style><script>function show_hide(ident) {var a = document.getElementById(ident);if (a.style.display === "none") {a.style.display = "block";} else {a.style.display = "none";}}</script></head>';
	new_doc += "<body><!-- Thanks for using my Custom HTML editor! Feel free to visit again! -->"

	// Header and description
	if (document.getElementById("header").value === "") { document.getElementById("header").value = 'Town' }
	if (document.getElementById("description").value === "") { document.getElementById("description").value = 'Description' }
	new_doc += "<h1>" + export_obj['Name'] + "</h1>" + export_obj['Description'];

	// Start with Stores
	if (export_obj['Stores'].length > 0) {
		new_doc += '<h2 class="text-lg bold center">Shops</h2>';
	}
	for (var i = 0; i < export_obj['Stores'].length; i++) {
		var temp_store = export_obj['Stores'][i];
		if (DEBUG) { console.log("Adding store: " + temp_store['Owner']['Store Name']) };

		// Owner Information
		new_doc += '<div class="wrapper-box" style="margin-bottom: 60px;">';
		new_doc += '<span class="text-lg bold">' + temp_store['Owner']['Store Name'] + '</span><br>';
		new_doc += '<span class="bold text-md">Proprietor: </span><span class="text-md">' + temp_store['Owner']['Name'] + '</span>';

		new_doc += '<ul>';
		['Race', 'Gender', 'Age', 'Trait 1', 'Trait 2'].forEach(function(item, i, arr) {
			new_doc += '<li><span class="bold">' + item + ': </span>' + temp_store['Owner'][item] + '</li>';
		})
		new_doc += '</ul>';
		new_doc += '<p>' + temp_store['Owner']['Description'] + '</p>';

		// Loop through items.
		new_doc += '<table id="Table" class="inventory-table" style="width:100%">';
		for (var x = 0; x < temp_store['Data'].length; x++) {

			// For Items
			new_doc += '<tr>'
			if (temp_store['Data'][x]['Type'] == 'Item') {
				if (DEBUG) { console.log("Explicit Item found"); }
				export_counter++;
				new_doc += '<td style="width:50%;"><span class="text-md" onclick="show_hide(\'' + export_counter + '\')" style="color:blue;">';
				new_doc += temp_store['Data'][x]['Name'] + '</span><br><span class="text-sm emp" id="' + export_counter + '" style="display: none;">';
				new_doc += temp_store['Data'][x]['Describe'] + '<p>' + temp_store['Data'][x]['Text'] + '</p></span></td><td>';
				new_doc += temp_store['Data'][x]['Category'] + '</td><td>' + temp_store['Data'][x]['Descriptor'] + '</td>';
			} else {
				// For Blanks
				if (DEBUG) { console.log("Blank row found"); }
				var sorted_keys = Object.keys(temp_store['Data'][x]);
				sorted_keys.sort()

				for (var y = 0; y < sorted_keys.length - 1; y++) {
					if (sorted_keys[y].endsWith('H')) {
						new_doc += '<th>' + temp_store['Data'][x][sorted_keys[y]] + '</th>'
					} else {
						new_doc += '<td>' + temp_store['Data'][x][sorted_keys[y]] + '</td>'
					}
				}
			}
			new_doc += '</tr>'
		}
		new_doc += '</table>'
		new_doc += '</div>'
	}

	/************************************************************************************************/

	// Next is Tables
	if (export_obj['Tables'].length > 0) {
		new_doc += '<h2 class="text-lg bold center">Tables</h2>';
	}
	for (var i = 0; i < export_obj['Tables'].length; i++) {
		var temp_store = export_obj['Tables'][i];
		if (DEBUG) { console.log("Adding Table " + i) };

		// Loop through items.
		new_doc += '<table class="inventory-table" style="width:100%">';
		for (var x = 0; x < temp_store['Data'].length; x++) {

			// For Items
			new_doc += '<tr>'
			if (temp_store['Data'][x]['Type'] == 'Item') {
				if (DEBUG) { console.log("Explicit Item found"); }
				export_counter++;
				new_doc += '<td style="width:50%;"><span class="text-md" onclick="show_hide(\'' + export_counter + '\')" style="color:blue;">';
				new_doc += temp_store['Data'][x]['Name'] + '</span><br><span class="text-sm emp" id="' + export_counter + '" style="display: none;">';
				new_doc += temp_store['Data'][x]['Describe'] + '<p>' + temp_store['Data'][x]['Text'] + '</p></span></td><td>';
				new_doc += temp_store['Data'][x]['Category'] + '</td><td>' + temp_store['Data'][x]['Descriptor'] + '</td>';
			} else {
				// For Blanks
				if (DEBUG) { console.log("Blank row found"); }
				var sorted_keys = Object.keys(temp_store['Data'][x]);
				sorted_keys.sort()

				for (var y = 0; y < sorted_keys.length - 1; y++) {
					if (sorted_keys[y].endsWith('H')) {
						new_doc += '<th>' + temp_store['Data'][x][sorted_keys[y]] + '</th>'
					} else {
						new_doc += '<td>' + temp_store['Data'][x][sorted_keys[y]] + '</td>'
					}
				}
			}
			new_doc += '</tr>'
		}
		new_doc += '</table>'
		new_doc += '</div>'
	}

	/************************************************************************************************/

	// Next is Monsters
	if (export_obj['Monsters'].length > 0) {
		new_doc += '<h2 class="text-lg bold center">Monsters</h2>';
	}
	for (var i = 0; i < export_obj['Monsters'].length; i++) {
		var temp_monster = export_obj['Monsters'][i]

		// Header With Info
		new_doc += '<table class="wrapper-box" style="margin-bottom: 60px;"><tr><td>';
		new_doc += '<span class="text-lg bold">' + temp_monster['Name']
		new_doc += '</span> - <span class="text-md bold">CR: ' + temp_monster['Cr'] + '</span><br>'
		
		// Traits if Second edition
		if (temp_monster['Edition'] === '2') {
			new_doc += '<ul style="margin: 2px 0px;padding: 0px;display: inline-flex;list-style-type: none;">';
			for (var x = 0; x < temp_monster['Traits'].length; x++) {
				new_doc += '<li style="margin: 2px 5px; padding: 2px 5px; background-color: #CFCFCF;">' + temp_monster['Traits'][x] + '</li>';
			}
			new_doc += '</ul><br>';
		}
		new_doc += '<span class="text-md emp">Alignment: ' + temp_monster['Alignment'] + '</span>' + temp_monster['Description'];
		
		// Adding Info Section
		new_doc += '</td></tr><tr><td><ul style="column-count: 2;list-style-type: none;margin: 5px;">'
		new_doc += '<li><span class="bold">HP:</span> ' + temp_monster['Hp'] + '</li>';
		new_doc += '<li><span class="bold">Speed:</span> ' + temp_monster['Speed'] + '</li>';
		new_doc += '<li><span class="bold">Size:</span> ' + temp_monster['Size'] + '</li>';

		if (temp_monster['Edition'] === '5') {
			new_doc += '<li><span class="bold">Saving Throws:</span> ';
			['StrSave', 'DexSave', 'ConSave', 'IntSave', 'WisSave', 'ChaSave'].forEach(function(val) {
				if (temp_monster[val]) {
					new_doc += val.substring(0, 3) + ', ';
				}
			})
			new_doc += '</li>';

		} else if (temp_monster['Edition'] === '1') {
			new_doc += '<li><span class="bold">CMD</span>: ' + temp_monster['Cmd'] + '</li>';
			new_doc += '<li><span class="bold">CMB</span>: ' + temp_monster['Cmb'] + '</li>';

			new_doc += '<li><span class="bold">Fortitude Save</span>: ' + temp_monster['FortSave'] + '</li>';
			new_doc += '<li><span class="bold">Reflex Save</span>: ' + temp_monster['RefSave'] + '</li>';
			new_doc += '<li><span class="bold">Will Save</span>: ' + temp_monster['WillSave'] + '</li>';

		} else if (temp_monster['Edition'] === '2') {
			new_doc += '<li><span class="bold">Fortitude Save</span>: ' + temp_monster['FortSave'] + '</li>';
			new_doc += '<li><span class="bold">Reflex Save</span>: ' + temp_monster['RefSave'] + '</li>';
			new_doc += '<li><span class="bold">Will Save</span>: ' + temp_monster['WillSave'] + '</li>';
		}
		new_doc += '<li><span class="bold">Damage Immunities</span>: ' + temp_monster['DamImmune'] + '</li>';
		new_doc += '<li><span class="bold">Damage Resistances</span>: ' + temp_monster['DamResist'] + '</li>';
		new_doc += '<li><span class="bold">Damage Weaknesses</span>: ' + temp_monster['DamWeak'] + '</li>';

		new_doc += '<li><span class="bold">Senses</span>: ' + temp_monster['Sense'] + '</li>';
		new_doc += '<li><span class="bold">Languages</span>: ' + temp_monster['Language'] + '</li>';

		// Info Wrap up
		new_doc += '</ul>';
		new_doc += '</td></tr>';

		// Stat Table
		new_doc += '<tr><td><table class="inventory-table"><tr><th>STR</th><th>DEX</th><th>CON</th><th>INT</th><th>WIS</th><th>CHA</th></tr><tr>';
		['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha'].forEach(function(stat) {
			new_doc += '<td>';
			if (is_numeric(temp_monster[stat])) {
				new_doc += temp_monster[stat] + ' (' + get_mod(temp_monster[stat]) + ')';
			} else {
				new_doc += temp_monster[stat];
			}
			new_doc += '</td>';
		})
		new_doc += '</tr></table></td></tr>';

		// Add actions
		new_doc += '<tr><td><div class="attacks">'

		for (var x = 0; x < temp_monster['Actions'].length; x++) {
			var temp_action = temp_monster['Actions'][x];
			new_doc += '<table><tr><th>' + temp_action['Name'];
			if (temp_monster['Edition'] == '5' && temp_action['Legendary']) {
				new_doc += ' - <span style="color:#FFD700">Legendary</span>';
			}
			if (temp_monster['Edition'] == '2') {
				new_doc += ' - Cost: ';
				if (temp_action['Cost'] == 'Free') {
					new_doc += '<abbr title="Free Action">&#9671;</abbr>'
				} else if (temp_action['Cost'] == 'Reaction') {
					new_doc += '<abbr title="Reaction">&#8634;</abbr>'
				} else if (temp_action['Cost'] == '1 Action') {
					new_doc += '<abbr title="1 Action">&#9830;</abbr>'
				} else if (temp_action['Cost'] == '2 Action') {
					new_doc += '<abbr title="2 Action">&#9830;&#9830;</abbr>'
				} else if (temp_action['Cost'] == '3 Action') {
					new_doc += '<abbr title="3 Action">&#9830;&#9830;&#9830;</abbr>'
				}
			}
			new_doc += '</th></tr><tr><td>' + temp_action['Text'];
			new_doc += '</td></tr></table>';
		}

		// Monster Treasure
		new_doc += '</div></td></tr><tr><td><h3 style="text-align:center;">Treasure</h3>'

		var treasure = temp_monster['Treasure'];
		if (DEBUG) { console.log("Adding Table " + i) };

		// Loop through items
		new_doc += '<table class="inventory-table" style="width:100%">';
		for (var x = 0; x < treasure['Data'].length; x++) {

			// For Items
			new_doc += '<tr>'
			if (treasure['Data'][x]['Type'] == 'Item') {
				if (DEBUG) { console.log("Explicit Item found"); }
				export_counter++;
				new_doc += '<td style="width:50%;"><span class="text-md" onclick="show_hide(\'' + export_counter + '\')" style="color:blue;">';
				new_doc += treasure['Data'][x]['Name'] + '</span><br><span class="text-sm emp" id="' + export_counter + '" style="display: none;">';
				new_doc += treasure['Data'][x]['Describe'] + '<p>' + treasure['Data'][x]['Text'] + '</p></span></td><td>';
				new_doc += treasure['Data'][x]['Category'] + '</td><td>' + treasure['Data'][x]['Descriptor'] + '</td>';
			} else {
				// For Blanks
				if (DEBUG) { console.log("Blank row found"); }
				var sorted_keys = Object.keys(treasure['Data'][x]);
				sorted_keys.sort()

				for (var y = 0; y < sorted_keys.length - 1; y++) {
					if (sorted_keys[y].endsWith('H')) {
						new_doc += '<th>' + treasure['Data'][x][sorted_keys[y]] + '</th>'
					} else {
						new_doc += '<td>' + treasure['Data'][x][sorted_keys[y]] + '</td>'
					}
				}
			}
			new_doc += '</tr>'
		}
		new_doc += '</table></td></tr></table>';
	}

	/************************************************************************************************/

	// Next is Hazards
	if (export_obj['Hazards'].length > 0) {
		new_doc += '<h2 class="text-lg bold center">Hazards</h2>';
	}
	for (var i = 0; i < export_obj['Hazards'].length; i++) {
		var temp_hazard = export_obj['Hazards'][i];
		if (DEBUG) { console.log("Adding List " + i) };

		// Header
		new_doc += '<table class="wrapper-box" style="margin-bottom: 60px;"><tr><th>';
		new_doc += '<div style="float: left">' + temp_hazard['Name'] + '</div>';
		new_doc += '<div style="float: right">Hazard ' + temp_hazard['Cr'] + '</div>';

		// Traits
		new_doc += '</th></tr><tr><td><div class="traits">';

		for (var x = 0; x < temp_hazard['Traits'].length; x++) {
			new_doc += '<div class="traits_obj">' + temp_hazard['Traits'][x].toUpperCase() + '</div>'
		}

		new_doc += '</div</td></tr><tr><td><ul>';

		// Permenant Set of Details
		new_doc += '<li><b>Complexity: </b>' + temp_hazard['Complexity'] + '</li>'
		new_doc += '<li><b>Stealth: </b>' + temp_hazard['Stealth'] + '</li>'
		new_doc += '<li><b>Description: </b>' + temp_hazard['Description'] + '</li>'
		new_doc += '<li><b>Disable: </b>' + temp_hazard['Disable'] + '</li>'

		new_doc += '</ul</td></tr><tr><td><hr></td></tr><tr><td><ul>';

		// Custom details
		for (var x = 0; x < temp_hazard['Custom'].length; x++) {
			var temp_custom = temp_hazard['Custom'][x]
			new_doc += '<li><b>' + Object.keys(temp_custom)[0] + ': </b>' + Object.values(temp_custom)[0] + '</li>'
		}
 
		new_doc += '</ul></td></tr></table>';
	}

	/************************************************************************************************/

	// Next is Lists
	if (export_obj['Lists'].length > 0) {
		new_doc += '<h2 class="text-lg bold center">Lists</h2>';
	}
	for (var i = 0; i < export_obj['Lists'].length; i++) {
		var temp_list = export_obj['Lists'][i];
		if (DEBUG) { console.log("Adding List " + i) };

		new_doc += '<ul>'
		for (var x = 0; x < temp_list.length; x++) {
			new_doc += '<li>';
			new_doc += temp_list[x]['Bold'] ? '<b>' : '';
			new_doc += temp_list[x]['Underline'] ? '<u>' : '';
			new_doc += temp_list[x]['Data'];
			new_doc += temp_list[x]['Underline'] ? '</u>' : '';
			new_doc += temp_list[x]['Bold'] ? '</b>' : '';
			new_doc += '</li>'
		}
		new_doc += '</ul>'
	}
	new_doc += "</body></html>"

	// Notice for getting the HTML prettified
	new_doc += "\n\n<!-- If you're looking to prettify the above Code, I recommend using the following services. -->"
	new_doc += "\n<!-- HTML: https://jsonformatter.org/html-pretty-print -->"
	new_doc += "\n<!-- CSS: https://www.cleancss.com/css-beautify/ -->"

	if (DEBUG) { console.log('RAW String'); }
	if (DEBUG) { console.log(new_doc); }

	// Parse to a DOM Document
	if (DEBUG) { console.log('Attempting to convert to a DOM object'); }
	var new_dom = new DOMParser().parseFromString(new_doc, "text/html");
	if (DEBUG) { console.log(new_dom); }

	// Save to file
	var textFile = null
	var new_doc_blob = new Blob([new_doc], {type: 'text/html;charset=utf-8'});
	saveAs(new_doc_blob, document.getElementById("header").value + '.custom.html');
}


/**Export data to JSON object
 * @param callback Whether or not to return or print to file
 * @return JSON data for the webpage 
 */
function export_json(callback) {
	if (DEBUG) { console.log("Exporting JSON"); }
	// Clear export object
	export_obj = {
		"Name": "",
		"Description": "",
		"Monsters": [],
		"Stores": [],
		"Tables": [],
		"Lists": [],
		"Hazards": [],
	}
	export_counter = 0;

	// Header Info
	export_obj['Name'] = document.getElementById('header').value;
	export_obj['Description'] = convert_text(document.getElementById('description').value);

	// Begin exporting Stores
	var editor_container = document.getElementById('Stores').childNodes;
	if (DEBUG) { console.log(editor_container); }
	for(var i = 0; i < editor_container.length; i++) {
		// Found the container
		if (/^S\dC/.test(editor_container[i].id)) {
			var editor_element = editor_container[i];
			export_obj['Stores'].push(get_table_data(editor_element.childNodes[editor_element.childNodes.length - 1], true));
		}
	}

	// Export Tables Next
	editor_container = document.getElementById('Tables').childNodes;
	if (DEBUG) { console.log(editor_container); }
	for(var i = 0; i < editor_container.length; i++) {
		// Found the container
		if (/^T\dC/.test(editor_container[i].id)) {
			var editor_element = editor_container[i];
			export_obj['Tables'].push(get_table_data(editor_element.childNodes[editor_element.childNodes.length - 1], false));
		}
	}

	// Export Monsters Next
	editor_container = document.getElementById('Monsters').childNodes;
	if (DEBUG) { console.log(editor_container); }
	for(var i = 0; i < editor_container.length; i++) {
		// Found the container
		if (/^M\dC/.test(editor_container[i].id)) {
			var editor_element = editor_container[i];
			var edition = document.getElementById(editor_element.id + '_EDITION');
			export_obj['Monsters'].push(get_monster_data(editor_element.childNodes[editor_element.childNodes.length - 1], edition.innerHTML[edition.innerHTML.length - 2]));
		}
	}

	// Export Hazards Next
	editor_container = document.getElementById('Hazards').childNodes;
	if (DEBUG) { console.log(editor_container); }
	for(var i = 0; i < editor_container.length; i++) {
		// Found the container
		if (/^H\dC/.test(editor_container[i].id)) {
			var editor_element = editor_container[i];
			var edition = document.getElementById(editor_element.id + '_EDITION');
			export_obj['Hazards'].push(get_hazard_data(editor_element.childNodes[editor_element.childNodes.length - 1], edition.innerHTML[edition.innerHTML.length - 2]));
		}
	}

	// Export Lists Next
	editor_container = document.getElementById('Lists').childNodes;
	if (DEBUG) { console.log(editor_container); }
	for(var i = 0; i < editor_container.length; i++) {
		// Found the container
		if (/^L\dC/.test(editor_container[i].id)) {
			var editor_element = editor_container[i];
			export_obj['Lists'].push(get_list_data(editor_element.childNodes[editor_element.childNodes.length - 1]));
		}
	}

	if (DEBUG) { console.log("Final Export Data"); }
	if (DEBUG) { console.log(export_obj); }
	if (!callback) {
		// Save to file
		var textFile = null
		var new_doc_blob = new Blob([JSON.stringify(export_obj, null, 2)], {type: 'text/plain;charset=utf-8'});
		saveAs(new_doc_blob, document.getElementById("header").value + '.custom.json');
	} else {
		return export_obj;
	}
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


	// Update page information to reflect the data imported.
	set_dom_value('header', new_json['Name']);
	set_dom_value('description', deconvert_text(new_json['Description']));
	calcHeight(textarea)

	for (let [key, value] of Object.entries(new_json)) {
		if (DEBUG) { console.log("Parsing Key: " + key); }
		if (DEBUG) { console.log(value); }

		if (key === 'Stores') {
			for (var i = 0; i < value.length; i++) {
				if (DEBUG) { console.log("Parsing Store Owner"); }
				create_element('Store');
				latest_store--;
				
				// Set Owner Elements
				set_dom_value('S' + latest_store + '_OWNER_STORE', value[i]['Owner']['Store Name']);
				set_dom_value('S' + latest_store + '_OWNER_NAME', value[i]['Owner']['Name']);
				set_dom_value('S' + latest_store + '_OWNER_DESCRIBE', deconvert_text(value[i]['Owner']['Description']));
				set_dom_value('S' + latest_store + '_OWNER_RACE', value[i]['Owner']['Race']);
				set_dom_value('S' + latest_store + '_OWNER_GENDER', value[i]['Owner']['Gender']);
				set_dom_value('S' + latest_store + '_OWNER_AGE', value[i]['Owner']['Age']);
				set_dom_value('S' + latest_store + '_OWNER_TRAIT_1', value[i]['Owner']['Trait 1']);
				set_dom_value('S' + latest_store + '_OWNER_TRAIT_2', value[i]['Owner']['Trait 2']);

				// Set Item Elements
				if (DEBUG) { console.log("Parsing Store Data"); }
				for (var j = 0; j < value[i]['Data'].length; j++) {
					if (value[i]['Data'][j]['Type'] === 'Blank') {
						document.getElementById('S' + latest_store + 'C_ADD').click();
						latest_store_rows--;
						
						var add_th = '';
						var add_td = '';

						// Since there's no Id's to follow, grab childNodes and select the one's that don't have Id's
						var buttons = document.getElementById('S' + latest_store + 'R' + latest_store_rows).childNodes;
						for (var x = buttons.length - 1; x >= 0; x--) {
							if (add_th !== '' && add_td !== '') {
								break;
							}
							if (buttons[x].innerHTML === "Add 'td'") {
								add_td = buttons[x];
							} else if (buttons[x].innerHTML === "Add 'th'") {
								add_th = buttons[x];
							}
						}

						// Loop through objects and hit buttons as needed.
						Object.keys(value[i]['Data'][j]).forEach(function(key) {
							var val = value[i]['Data'][j][key]
							var add = key.split("").reverse().join("");
							if (key.endsWith('H')) {
								add_th.click();
								set_dom_value('S' + latest_store + 'R' + latest_store_rows + key.split("").reverse().join("") + 'I', val)
							} else if (key.endsWith('C')) {
								add_td.click();
								set_dom_value('S' + latest_store + 'R' + latest_store_rows + key.split("").reverse().join("") + 'I', val)
							}
						});

						// Finally incriment when done, to not mess with future addition
						latest_store_rows++;
					} else {
						document.getElementById('S' + latest_store + 'C_SPECIAL').click();
						latest_store_rows--;
						
						set_dom_value('S' + latest_store + 'R' + latest_store_rows + '_Name', value[i]['Data'][j]['Name']);
						set_dom_value('S' + latest_store + 'R' + latest_store_rows + '_Describe', value[i]['Data'][j]['Describe']);
						set_dom_value('S' + latest_store + 'R' + latest_store_rows + '_Text', value[i]['Data'][j]['Text']);
						set_dom_value('S' + latest_store + 'R' + latest_store_rows + '_Category_I', value[i]['Data'][j]['Category']);
						set_dom_value('S' + latest_store + 'R' + latest_store_rows + '_Descriptor_I', value[i]['Data'][j]['Descriptor']);

						// Finally incriment when done, to not mess with future addition
						latest_store_rows++;
					}
				}

				// Finally incriment when done, to not mess with future addition
				latest_store++;
			}
		} else if (key === 'Tables') {
			for (var i = 0; i < value.length; i++) {
				if (DEBUG) { console.log("Parsing Table Data"); }
				create_element('Table');
				latest_table--;
				
				for (var j = 0; j < value[i]['Data'].length; j++) {
					if (value[i]['Data'][j]['Type'] === 'Blank') {
						document.getElementById('T' + latest_table + 'C_ADD').click();
						latest_table_rows--;
						
						var add_th = '';
						var add_td = '';

						// Since there's no Id's to follow, grab childNodes and select the one's that don't have Id's
						var buttons = document.getElementById('T' + latest_table + 'R' + latest_table_rows).childNodes;
						for (var x = buttons.length - 1; x >= 0; x--) {
							if (add_th !== '' && add_td !== '') {
								break;
							}
							if (buttons[x].innerHTML === "Add 'td'") {
								add_td = buttons[x];
							} else if (buttons[x].innerHTML === "Add 'th'") {
								add_th = buttons[x];
							}
						}

						// Loop through objects and hit buttons as needed.
						Object.keys(value[i]['Data'][j]).forEach(function(key) {
							var val = value[i]['Data'][j][key]
							var add = key.split("").reverse().join("");
							if (key.endsWith('H')) {
								add_th.click();
								set_dom_value('T' + latest_table + 'R' + latest_table_rows + key.split("").reverse().join("") + 'I', val)
							} else if (key.endsWith('C')) {
								add_td.click();
								set_dom_value('T' + latest_table + 'R' + latest_table_rows + key.split("").reverse().join("") + 'I', val)
							}
						});

						// Finally incriment when done, to not mess with future addition
						latest_table_rows++;
					} else {
						document.getElementById('T' + latest_table + 'C_SPECIAL').click();
						latest_table_rows--;
						
						set_dom_value('T' + latest_table + 'R' + latest_table_rows + '_Name', value[i]['Data'][j]['Name']);
						set_dom_value('T' + latest_table + 'R' + latest_table_rows + '_Describe', value[i]['Data'][j]['Describe']);
						set_dom_value('T' + latest_table + 'R' + latest_table_rows + '_Text', value[i]['Data'][j]['Text']);
						set_dom_value('T' + latest_table + 'R' + latest_table_rows + '_Category_I', value[i]['Data'][j]['Category']);
						set_dom_value('T' + latest_table + 'R' + latest_table_rows + '_Descriptor_I', value[i]['Data'][j]['Descriptor']);

						// Finally incriment when done, to not mess with future addition
						latest_table_rows++;
					}
				}

				// Finally incriment when done, to not mess with future addition
				latest_table++;
			}
		} else if (key.startsWith('Monster')) {
			for (var i = 0; i < value.length; i++) {
				if (DEBUG) { console.log("Parsing Monster Data"); }
				console.log("Edition: " + value[i]['Edition'])
				create_element('Monster' + value[i]['Edition']);
				latest_monster--;
				console.log(value[i]);

				// Begin Header section
				set_dom_value('M' + latest_monster + 'R1_NAME', value[i]['Name']);
				set_dom_value('M' + latest_monster + 'R1_CR', value[i]['Cr']);
				set_dom_value('M' + latest_monster + 'R1_ALIGN', value[i]['Alignment']);
				set_dom_value('M' + latest_monster + 'R1_DESCRIBE', deconvert_text(value[i]['Description']));

				// Pathfinder 2e Traits
				if (value[i]['Edition'] === '2') {
					for (var j = 0; j < value[i]['Traits'].length; j++) {
						console.log('M' + latest_monster + 'R1_TRAIT_ADD')
						document.getElementById('M' + latest_monster + 'R1_TRAIT_ADD').click();
						latest_monster_trait--;

						set_dom_value('M' + latest_monster + 'R1_TRAITS_' + latest_monster_trait, value[i]['Traits'][j]);

						latest_monster_trait++;
					}
				}

				// Begin Info section
				set_dom_value('M' + latest_monster + 'R1_HP', value[i]['Hp']);
				set_dom_value('M' + latest_monster + 'R1_SPEED', value[i]['Speed']);
				set_dom_value('M' + latest_monster + 'R1_AC', value[i]['Ac']);
				set_dom_value('M' + latest_monster + 'R1_SIZE', value[i]['Size']);
				set_dom_value('M' + latest_monster + 'R1_SKILLS', value[i]['Skills']);
				set_dom_value('M' + latest_monster + 'R1_DAM_IMMUNE', value[i]['DamImmune']);
				set_dom_value('M' + latest_monster + 'R1_DAM_RESIST', value[i]['DamResist']);
				set_dom_value('M' + latest_monster + 'R1_DAM_WEAK', value[i]['DamWeak']);
				set_dom_value('M' + latest_monster + 'R1_SENSE', value[i]['Sense']);
				set_dom_value('M' + latest_monster + 'R1_LANGUAGE', value[i]['Language']);

				// 5e Saves vs Pathfinder Saves
				if (value[i]['Edition'] === '5') {
					['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha'].forEach(function(save) {
						if (value[i][save + 'Save']) {
							document.getElementById('M' + latest_monster + 'R1_' + save.toUpperCase() + '_SAVE').checked = true;
						}
					});
				} else if (value[i]['Edition'] === '1' || value[i]['Edition'] === '2') {
					set_dom_value('M' + latest_monster + 'R1_FORT_SAVE', value[i]['FortSave']);
					set_dom_value('M' + latest_monster + 'R1_REF_SAVE', value[i]['RefSave']);
					set_dom_value('M' + latest_monster + 'R1_WILL_SAVE', value[i]['WillSave']);
				}
				// New AC and Combat Maneuver
				if (value[i]['Edition'] === '1') {
					set_dom_value('M' + latest_monster + 'R1_TOUCH_AC', value[i]['TouchAc']);
					set_dom_value('M' + latest_monster + 'R1_FLAT_AC', value[i]['FlatAc']);
					set_dom_value('M' + latest_monster + 'R1_CMB', value[i]['Cmb']);
					set_dom_value('M' + latest_monster + 'R1_CMD', value[i]['Cmd']);

				}

				// Begin Stats section
				set_dom_value('M' + latest_monster + 'R1_STR', value[i]['Str']);
				set_dom_value('M' + latest_monster + 'R1_DEX', value[i]['Dex']);
				set_dom_value('M' + latest_monster + 'R1_CON', value[i]['Con']);
				set_dom_value('M' + latest_monster + 'R1_INT', value[i]['Int']);
				set_dom_value('M' + latest_monster + 'R1_WIS', value[i]['Wis']);
				set_dom_value('M' + latest_monster + 'R1_CHA', value[i]['Cha']);

				// Begin Actions seciont (universal for monsters)
				for (var j = 0; j < value[i]['Actions'].length; j++) {
					var temp_action = value[i]['Actions'][j];
					document.getElementById('M' + latest_monster + 'R1_ACTION_ADD').click();
					latest_monster_action--;
					set_dom_value('M' + latest_monster + 'R1_ACTIONS' + latest_monster_action + '_NAME', temp_action['Name']);
					set_dom_value('M' + latest_monster + 'R1_ACTIONS' + latest_monster_action + '_TEXT', deconvert_text(temp_action['Text']));

					// Legendary Action for 5th edition
					if (value[i]['Edition'] === '5') {
						if (temp_action['Legendary']) {
							document.getElementById('M' + latest_monster + 'R1_ACTIONS' + latest_monster_action + '_LEGEND').checked = true;
						}
					}
					if (value[i]['Edition'] === '2') {
						set_dom_value('M' + latest_monster + 'R1_ACTIONS' + latest_monster_action + '_COST', temp_action['Cost']);
					}

					// Incriment again
					latest_monster_action++;
				}

				// Add Monster Treasure Import
				var loot_table = value[i]['Treasure']
				latest_table--;

				for (var j = 0; j < loot_table['Data'].length; j++) {
					if (loot_table['Data'][j]['Type'] === 'Blank') {
						document.getElementById('MT' + latest_table + 'C_ADD').click();
						latest_table_rows--;
						
						var add_th = '';
						var add_td = '';

						// Since there's no Id's to follow, grab childNodes and select the one's that don't have Id's
						var buttons = document.getElementById('MT' + latest_table + 'R' + latest_table_rows).childNodes;
						for (var x = buttons.length - 1; x >= 0; x--) {
							if (add_th !== '' && add_td !== '') {
								break;
							}
							if (buttons[x].innerHTML === "Add 'td'") {
								add_td = buttons[x];
							} else if (buttons[x].innerHTML === "Add 'th'") {
								add_th = buttons[x];
							}
						}

						// Loop through objects and hit buttons as needed.
						Object.keys(loot_table['Data'][j]).forEach(function(key) {
							var val = loot_table['Data'][j][key]
							var add = key.split("").reverse().join("");
							if (key.endsWith('H')) {
								add_th.click();
								set_dom_value('MT' + latest_table + 'R' + latest_table_rows + key.split("").reverse().join("") + 'I', val)
							} else if (key.endsWith('C')) {
								add_td.click();
								set_dom_value('MT' + latest_table + 'R' + latest_table_rows + key.split("").reverse().join("") + 'I', val)
							}
						});

						// Finally incriment when done, to not mess with future addition
						latest_table_rows++;
					} else {
						document.getElementById('MT' + latest_table + 'C_SPECIAL').click();
						latest_table_rows--;
						
						set_dom_value('MT' + latest_table + 'R' + latest_table_rows + '_Name', loot_table['Data'][j]['Name']);
						set_dom_value('MT' + latest_table + 'R' + latest_table_rows + '_Describe', loot_table['Data'][j]['Describe']);
						set_dom_value('MT' + latest_table + 'R' + latest_table_rows + '_Text', loot_table['Data'][j]['Text']);
						set_dom_value('MT' + latest_table + 'R' + latest_table_rows + '_Category_I', loot_table['Data'][j]['Category']);
						set_dom_value('MT' + latest_table + 'R' + latest_table_rows + '_Descriptor_I', loot_table['Data'][j]['Descriptor']);

						// Finally incriment when done, to not mess with future addition
						latest_table_rows++;
					}
				}

				// Incriment again
				latest_monster++;
				latest_table++;
			}
		} else if (key === 'Hazards') {
			for (var i = 0; i < value.length; i++) {
				if (DEBUG) { console.log("Parsing Hazard Data"); }
				console.log(value[i]['Edition'])
				create_element('Hazard' + value[i]['Edition']);
				latest_hazard--;
				console.log(value[i]);

				// Standard Entries rendered
				set_dom_value('H' + latest_hazard + 'R1_NAME', value[i]['Name']);
				set_dom_value('H' + latest_hazard + 'R1_CR', value[i]['Cr']);
				set_dom_value('H' + latest_hazard + 'R4_COMPLEXITY', value[i]['Complexity']);
				set_dom_value('H' + latest_hazard + 'R4_STEALTH', value[i]['Stealth']);
				set_dom_value('H' + latest_hazard + 'R4_DESCRIPTION', value[i]['Description']);
				set_dom_value('H' + latest_hazard + 'R4_DISABLE', value[i]['Disable']);

				// Traits
				for (var x = 0; x < value[i]['Traits'].length; x++) {
					document.getElementById('H' + latest_hazard + 'R3_TRAIT_ADD').click()
					latest_hazard_trait--;
					set_dom_value('H' + latest_hazard + 'R2_TRAITS_' + latest_hazard_trait, value[i]['Traits'][x]);
					latest_hazard_trait++;
				}

				// Custom
				for (var x = 0; x < value[i]['Custom'].length; x++) {
					document.getElementById('H' + latest_hazard + 'R5_CUSTOM_ADD').click()
					latest_hazard_custom--;
					var temp_custom = value[i]['Custom'][x];

					set_dom_value('H' + latest_hazard + 'R5_CUSTOM_' + latest_hazard_custom, Object.keys(temp_custom)[0]);
					set_dom_value('H' + latest_hazard + 'R5_CUSTOM_' + latest_hazard_custom + '_INPUT', Object.values(temp_custom)[0]);

					latest_hazard_custom++;
				}

				latest_hazard++;
			}

		} else if (key === 'Lists') {
			for (var i = 0; i < value.length; i++) {
				if (DEBUG) { console.log("Parsing List Data"); }
				create_element('List');
				latest_list--;
				for (var j = 0; j < value[i].length; j++) {
					document.getElementById('L' + latest_table + 'C_ADD').click();
					latest_list_rows--;
					set_dom_value('L' + latest_table + 'R' + latest_list_rows + 'I', value[i][j]['Data'])
					if (value[i][j]['Bold']) {
						document.getElementById('L' + latest_table + 'R' + latest_list_rows + 'I_BOLD').checked = true
					}
					if (value[i][j]['Underline']) {
						document.getElementById('L' + latest_table + 'R' + latest_list_rows + 'I_UNDERLINE').checked = true
					}
					// Finally incriment when done, to not mess with future addition
					latest_list_rows++;			
				}

				// Finally incriment when done, to not mess with future addition
				latest_list++;
			}
		}
	}
}


/**Set a DOM value for import
 * @param dom DOM Id string
 * @param value Value to be set
 */
function set_dom_value(dom, value) {
	var dom_elem = document.getElementById(dom);
	dom_elem.value = value;
}


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
