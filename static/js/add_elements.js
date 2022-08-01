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
	add_flex_box.style.width = '38%';
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
			this.innerHTML = '<img src="/static/hide.svg" title="Hide Block" width="30px" height="30px">';
			a.style.display = 'block';
		} else {
			this.innerHTML = '<img src="/static/unhide.svg" title="Unhide Block" width="30px" height="30px">';
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
		}
		set_session_storage();
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
			set_session_storage();
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
			set_session_storage();
		}

		add_button_td.appendChild(add_button_div);

		// Add Descriptor
		var item_descriptor_cell = item_row.insertCell(0);
		item_descriptor_cell.id = item_row.id + "_Descriptor";

		var item_descriptor = generic_text_input(item_descriptor_cell.id + "_I");
		item_descriptor.placeholder = 'Descriptor';
		item_descriptor_cell.appendChild(item_descriptor);

		// Add Category
		var item_category_cell = item_row.insertCell(0);
		item_category_cell.id = item_row.id + "_Category";

		var item_category = generic_text_input(item_category_cell.id + "_I");
		item_category.placeholder = 'Category';
		item_category_cell.appendChild(item_category);

		// Add Main Data
		var item_data_cell = item_row.insertCell(0);
		item_data_cell.id = item_row.id + "_Data";

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
		item_text.style.lineHeight = "20px";
		item_text.style.width = "400px";
		item_data_cell.appendChild(item_text);
		set_session_storage();
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

		// Delete Row Action
		var delete_row_td = new_row.insertCell(0);
		delete_row_td.style.float = 'right';

		var delete_row_button = generic_action_span('delete', 'Delete Row', '', '0 0 0 10px');
		delete_row_button.onclick = function() {
			if (confirm("Are you sure you want to delete this row?")) {
				if (DEBUG) { console.log("Deleting Row"); }
				new_row.parentNode.removeChild(new_row);
				if (DEBUG) { console.log("Row Successfully Deleted"); }
			}
			set_session_storage();
		}
		delete_row_td.appendChild(delete_row_button);

		// Add TH Action
		var row_th = new_row.insertCell(1);
		row_th.style.float = 'right';

		var add_th = generic_action_span('add', 'Add th', '', '0 0 0 10px');
		add_th.onclick = function() {
			var new_cell = new_row.insertCell(new_row.cells.length - 3);
			new_cell.id = new_row.id + 'C' + (new_row.cells.length - 3);
			new_cell.style.backgroundColor = "#FFFFFF";

			new_cell.appendChild(generic_text_input(new_cell.id + "I"))
			set_session_storage();

		}
		row_th.appendChild(add_th);

		// Add TD Action
		var row_td = new_row.insertCell(2);
		row_td.style.float = 'right';

		var add_td = generic_action_span('add', 'Add td', '', '0 0 0 10px');
		add_td.onclick = function() {
			var new_cell = new_row.insertCell(new_row.cells.length - 3);
			new_cell.id = new_row.id + 'H' + (new_row.cells.length - 3);
			new_cell.style.backgroundColor = "#CFCFCF";

			new_cell.appendChild(generic_text_input(new_cell.id + "I"))
			set_session_storage();

		}
		row_td.appendChild(add_td);
	}

	return add_row;
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

	// Delete
	var add_delete_div = generic_action_span('delete', 'Delete Item', '', '0 20px 0 0');;
	add_delete_div.id = add_id + "_DELETE";

	// Delete Row option
	add_delete_div.onclick = function() {
		if (confirm("Delete row?")) {
			if (DEBUG) { console.log("Deleting row"); }
			parent_obj.parentNode.removeChild(parent_obj);
			if (DEBUG) { console.log("Row successfully deleted"); }
		}
		set_session_storage();
	}

	parent_obj.appendChild(add_delete_div);
}


/**Adds store header function: new_row
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
		
		var new_row_input = document.createElement('input');
		new_row_input.type = 'Text';
		new_row_input.id = new_row.id + 'I'
		new_row_input.placeholder = 'Text';

		new_row.appendChild(new_row_input);

		add_list_settings(new_row, new_row.id + 'I');

		content.appendChild(new_row);
		set_session_storage();
	}

	return new_row
}
