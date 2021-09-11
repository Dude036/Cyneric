let DEBUG = true;
let latest_store = 0;
let latest_store_rows = 0;
let latest_table = 0;
let latest_table_rows = 0;
let latest_list = 0;
let latest_list_rows = 0;
let latest_div = 0;

// Export Variables
let export_obj = {
	"Stores": [],
	"Tables": [],
	"Lists": [],
	"Divs": [],
}
let export_counter = 0;


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
	if (element.id.startsWith("S") || element.id.startsWith("T")) {
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
			item_data_cell.appendChild(item_text);
		}

		container.appendChild(add_delete_div);
		container.appendChild(add_row_div);
		container.appendChild(add_item_div);
	}
	
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

/**Function to add stuff to the main page. Creates the elements, to then wrap in containers
 * @param item The type of item to be made
 */
function create_element(item) {
	if (DEBUG) { console.log("Begin Element Creation"); }

	if (item == "Store") {
		// Init
		var store = document.createElement('table');
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
		owner_store_name.style.fontSize = '24px';

		owner_container.appendChild(owner_store_name);
		owner_container.appendChild(document.createElement('br'));
		// Owner Name
		var owner_name = document.createElement('input');
		owner_name.id = owner_container.id + "_NAME";
		owner_name.type = 'text';
		owner_name.placeholder = 'Owner Name';
		
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
		owner_description_text.id = owner_container.id + "_DESCRIBE";

		owner_container.appendChild(owner_description_text)

		// Add
		store.appendChild(owner_container);
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
	} else if (item == "Div") {
		// Init
		var div = document.createElement('div');
		div.id = "D" + latest_div
		latest_div += 1;

		// Style
		div.style.width = "100%";

		// Add
		var parent = document.getElementById("Divs");
		parent.appendChild(div)
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
		'Description': document.getElementById(row.id + "_DESCRIBE").value,
	}

	if (DEBUG) { console.log("Owner Complete"); }
	if (DEBUG) { console.log(owner_obj); }
	return owner_obj;
}

/**Extract all table data from the div table element
 * @param table The table produced
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
	for (var i = 1; i < table.rows.length; i++) {
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
					item[x.toString() + children[x].id[children[x].id.length - 2]] = document.getElementById(children[x].id + 'I').value
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

/**Export everything into an object, then turn the object data into a usable html file
 */
function export_page() {
	if (DEBUG) { console.log("Exporting Page"); }
	// Clear export object
	export_obj = {
		"Stores": [],
		"Tables": [],
		"Lists": [],
		"Divs": [],
	}
	export_counter = 0;

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

	// Export Lists Next
	editor_container = document.getElementById('Lists').childNodes;
	if (DEBUG) { console.log(editor_container); }
	for(var i = 0; i < editor_container.length; i++) {
		// Found the container
		if (/^L\dC/.test(editor_container[i].id)) {
			var editor_element = editor_container[i];
			export_obj['Lists'].push(get_list_data(editor_element.childNodes[editor_element.childNodes.length - 1], false));
		}
	}

	/*********************************************************/
	/******************** EXPORT COMPLET E********************/
	/*********************************************************/
	if (DEBUG) { console.log("Final Export Data"); }
	if (DEBUG) { console.log(export_obj); }

	// Create new Document for printing
	// Going with a simple String to be coppied
	// Boiler plate CSS header stuffs
	var new_doc = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Custom HTML</title><style>body{max-width:1000px;margin-left:auto;margin-right:auto;padding-left:5px;padding-right:5px}html{font-family:Arial}h1,h2{color:#000;text-align:center}.center{text-align:center}.bold{font-weight:700}.emp{font-style:italic}table{border:1px solid #000;border-spacing:0}table tr th{background-color:gray;color:#fff;padding:5px}table tr td{margin:0;padding:5px}.text-xs{font-size:12px}.text-sm{font-size:14px}.text-md{font-size:18px}.text-lg{font-size:24px}.text-xl{font-size:32px}.wrapper-box{width:100%;border:2px solid #000;margin-bottom:60px padding:5px;}.inventory-table{width:100%;}.suggestion{padding:2px 0;margin:0;list-style:none}.suggestion li{border:1px solid #000;background-color:#ddd;padding:2px 4px;margin:5px 10px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.suggestion li:active{background-color:#404040}.suggestion li:hover{background-color:grey}.attacks{display:flex;flex-wrap:wrap;align-items:flex-start;width:100%;padding-top:10px;padding-bottom:20px}.attacks table{width:44%;margin-left:3%;margin-right:3%;margin-bottom:1%}.header{background-color:#f1f1f1;position:fixed;top:0;left:0;padding:5px 5px}.header ul{display:none;list-style-type:none;padding-left:10px;margin-top:0}.header a{float:left;color:#000;text-align:center;text-decoration:none;padding:5px 5px}.header a:hover{background-color:#ddd}.header a.active{background-color:#02f}.crit tr:nth-child(even){background-color:#eee}.link{text-align:center}.link li{padding-bottom:10px}.link a{border:1px solid #000;width:60%;text-decoration:none;color:#222;background-color:#ddd;padding:3px 3px 3px 3px}.link a:hover{background-color:#222;color:#ddd}.sidebar{float:left;position:fixed;top:0;right:0;margin:5px}.sidebar_object{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;padding:10px 20px;border-style:solid;border:2px;background-color:#efefef}.sidebar_object:hover{background-color:#cfcfcf}.sidebar_object:active{background-color:#0000cf;color:#efefef}@media only screen and (max-width:600px){.header a{float:none;display:block;text-align:left;font-size:20px}.header img{height:50px;width:50px}.header-right{float:none}}</style><script>function show_hide(ident) {var a = document.getElementById(ident);if (a.style.display === "none") {a.style.display = "block";} else {a.style.display = "none";}}</script></head>';
	new_doc += "<body>"

	// Header and description
	if (document.getElementById("header").value === "") { document.getElementById("header").value = 'Town' }
	if (document.getElementById("description").value === "") { document.getElementById("description").value = 'Description' }
	new_doc += "<h1>" + document.getElementById("header").value + "</h1>";
	new_doc += "<p>" + document.getElementById("description").value + "</p>";

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

	// Next is Tables
	if (export_obj['Tables'].length > 0) {
		new_doc += '<h2 class="text-lg bold center">Tables</h2>';
	}
	for (var i = 0; i < export_obj['Tables'].length; i++) {
		var temp_store = export_obj['Tables'][i];
		if (DEBUG) { console.log("Adding Table " + i) };

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

	console.log(new_doc);
	// // Parse to a DOM Document
	// console.log(new DOMParser().parseFromString(new_doc, "text/html"));

	// Save to file
	var textFile = null
	var new_doc_blob = new Blob([new_doc], {type: 'text/plain;charset=utf-8'});
	saveAs(new_doc_blob, document.getElementById("header").value + '.custom.html');
}

/**Export data to JSON object
 * @param ret Whether or not to return
 * @retrun JSON data for the webpage 
 */
function export_json(ret) {
	if (DEBUG) { console.log("Exporting Page"); }
	// Clear export object
	export_obj = {
		"Stores": [],
		"Tables": [],
		"Lists": [],
		"Divs": [],
	}
	export_counter = 0;

	// Begin exporting Stores
	var editor_container = document.getElementById('Stores').childNodes;
	if (DEBUG) { console.log(editor_container); }
	for(var i = 0; i < editor_container.length; i++) {
		// Found a container
		if (/^S\dC/.test(editor_container[i].id)) {
			var editor_element = editor_container[i];
			export_obj['Stores'].push(get_table_data(editor_element.childNodes[editor_element.childNodes.length - 1]));
		}
	}
	if (DEBUG) { console.log("Final Export Data"); }
	if (DEBUG) { console.log(export_obj); }
	// Save to file
	var textFile = null
	var new_doc_blob = new Blob([new_doc], {type: 'text/plain;charset=utf-8'});
	saveAs(new_doc_blob, document.getElementById("header").value + '.custom.json');
}

/**Export everything into something readable
 */
function import_page() {
	var string = prompt("Import JSON", '');
	if (string == null) {
		alert("Invalid data entered.")
		return
	}

	// Test whether the imported string is valid
	if (DEBUG) { console.log("Import Data"); }
	if (DEBUG) { console.log(string); }



	// Update page information to reflect the data imported.
}

/** - Nice to Haves
 * I'd like to add the ability to import a file by a string.
 */
