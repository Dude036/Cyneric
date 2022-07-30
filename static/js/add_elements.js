/************************************
 * Element creation for all formats *
 ************************************/

// Color Indexes
let DELETE_COLOR = '#C00000';
let PF2E_COLOR = '#009900';
let PF1E_COLOR = '#000099';
let DND5_COLOR = '#009999';
let GREY_BACKGROUND = '#EFEFEF';


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
	var move_button = document.createElement('span');
	move_button.style.padding = '5px';
	move_button.innerHTML = '<img class="move-handle" src="/static/move.svg" width="30px" height="30px">';

	return move_button;
}


/**Adds header function: hide
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: hide
 */
function add_header_hide(parent, content) {
	var hide_button = document.createElement('span');
	hide_button.style.padding = '5px';
	hide_button.name = content.id;
	hide_button.addEventListener('click', function() {
		var a = document.getElementById(this.name);
		if (this.innerHTML.includes('unhide')) {
			this.innerHTML = '<img src="/static/hide.svg" width="30px" height="30px">';
			a.style.display = 'block';
		} else {
			this.innerHTML = '<img src="/static/unhide.svg" width="30px" height="30px">';
			a.style.display = 'none';
		}
	});
	hide_button.innerHTML = '<img src="/static/hide.svg" width="30px" height="30px">'

	return hide_button;
}


/**Adds header function: delete
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: delete
 */
function add_header_delete(parent, content) {
	var delete_button = document.createElement('span');
	delete_button.style.padding = '5px';
	delete_button.onclick = function() {
		if (confirm("Delete Item?")) {
			if (DEBUG) { console.log("Deleting Item"); }
			parent.parentNode.removeChild(parent);
			if (DEBUG) { console.log("Item successfully deleted"); }
		}
		set_session_storage();
	}
	delete_button.innerHTML = '<img src="/static/delete.svg" width="30px" height="30px">';

	return delete_button;
}


/**Adds store header function: owner
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: owner
 */
function add_store_action_owner(parent, content) {
	var delete_button = document.createElement('span');
	delete_button.style.padding = '5px';
	delete_button.onclick = function() {
		if (confirm("Delete Item?")) {
			if (DEBUG) { console.log("Deleting Item"); }
			parent.parentNode.removeChild(parent);
			if (DEBUG) { console.log("Item successfully deleted"); }
		}
		set_session_storage();
	}
	delete_button.innerHTML = '<img src="/static/delete.svg" width="30px" height="30px">';

	return delete_button;
}


/**Adds store header function: item_row
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: item_row
 */
function add_store_action_item_row() {

}


/**Adds store header function: blank_row
 * @param parent DOM element containing everything
 * @param content DOM element containg contents to be displayed
 * @return Action for parent of type: blank_row
 */
function add_store_action_blank_row() {

}

