/**Retreive data from foreign website, and parse it using the server's backend
 * @param prompt_text The text to prompt the user for the URL
 * @param edition What edition so the data gets parsed correctly
 * @param container_id The container to update
 */
async function get_monster_contents(prompt_text, edition, container_id) {
	// Get URL
	var url = prompt(prompt_text, '');
	if (url == null) {
		alert("Invalid data entered.")
		return
	}

	// Validate URL
	try {
		var check = new URL(url);
	} catch (_) {
		alert("Invalid Link.")
		return
	}

	// Link Validated, begin POST
	var xhr = new XMLHttpRequest();
	var connection = window.location.href + 'parser/';
	const token = document.querySelector('[name=csrfmiddlewaretoken]').value;
	xhr.open("POST", connection);

	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.setRequestHeader("X-CSRFToken", token);

	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4) {
			// Completed request
			if (DEBUG) {
				console.log("Data recieved back for " + url);
				console.log(xhr.status);
				console.log(xhr.responseText);
			}
			var new_data = JSON.parse(xhr.responseText);
			if ('ERROR' in new_data) {
				// Post Toast Message about failure
				console.log("ERROR: " + new_data['ERROR']);
				if ("EXCEPTION" in new_data) {
					console.log("EXCEPTION: " + new_data['EXCEPTION']);
				}
				(async () => {
					var toast = document.createElement('div');
					toast.style.backgroundColor = "#E34D4D";
					toast.style.position = "fixed";
					toast.style.top = "40px";
					toast.style.left = "40px";
					toast.style.width = "250px";
					toast.id = "toast";
					toast.style.padding = "10px 20px";

					toast.appendChild(document.createTextNode(new_data['ERROR']));

					var header_img = document.getElementById("header_img");
					header_img.appendChild(toast);

					setTimeout(function(){
						toast.parentNode.removeChild(toast);
					}, 9000);
				})()
			} else {
				// We've recieved a creature, and can safely add it to the page.
				if (DEBUG) { console.log("Successfully recieved monster, posting to UI"); }
				update_container(new_data, container_id);
			}
		}
	};

	data = {
	  "Edition": edition,
	  "Type": "Monster",
	  "URL": url
	};

	xhr.send(JSON.stringify(data));
}


/**Retreive data from foreign website, and parse it using the server's backend
 * @param prompt_text The text to prompt the user for the URL
 * @param edition What edition so the data gets parsed correctly
 * @param container_id The container to update
 */
async function get_hazard_contents(prompt_text, edition, container_id) {
	// Get URL
	var url = prompt(prompt_text, '');
	if (url == null) {
		alert("Invalid data entered.")
		return
	}

	// Validate URL
	try {
		var check = new URL(url);
	} catch (_) {
		alert("Invalid Link.")
		return
	}

	// Link Validated, begin POST
	var xhr = new XMLHttpRequest();
	var connection = window.location.href + 'parser/';
	const token = document.querySelector('[name=csrfmiddlewaretoken]').value;
	xhr.open("POST", connection);

	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.setRequestHeader("X-CSRFToken", token);

	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4) {
			// Completed request
			if (DEBUG) {
				console.log("Data recieved back for " + url);
				console.log(xhr.status);
				console.log(xhr.responseText);
			}
			var new_data = JSON.parse(xhr.responseText);
			if ('ERROR' in new_data) {
				// Post Toast Message about failure
				console.log("ERROR: " + new_data['ERROR']);
				if ("EXCEPTION" in new_data) {
					console.log("EXCEPTION: " + new_data['EXCEPTION']);
				}
				(async () => {
					var toast = document.createElement('div');
					toast.style.backgroundColor = "#E34D4D";
					toast.style.position = "fixed";
					toast.style.top = "40px";
					toast.style.left = "40px";
					toast.style.width = "250px";
					toast.id = "toast";
					toast.style.padding = "10px 20px";

					toast.appendChild(document.createTextNode(new_data['ERROR']));

					var header_img = document.getElementById("header_img");
					header_img.appendChild(toast);

					setTimeout(function(){
						toast.parentNode.removeChild(toast);
					}, 9000);
				})()
			} else {
				// We've recieved a creature, and can safely add it to the page.
				if (DEBUG) { console.log("Successfully recieved hazard data, posting to UI"); }
				update_container(new_data, container_id);
			}
		}
	};

	data = {
	  "Edition": edition,
	  "Type": "Hazard",
	  "URL": url
	};

	xhr.send(JSON.stringify(data));
}


/** Get data from self API
 * @param link_suffix String containing the link suffix to connect to self api
 * @return JSON object of generated item data or null if error
 */
async function get_api_content(link_suffix) {
	var response = await fetch(window.location.origin + '/api/' + link_suffix);

    if (response.status === 200) {
    	var content = await response.json();
        return content;
    } else {
		(async () => {
			var toast = document.createElement('div');
			toast.style.backgroundColor = "#E34D4D";
			toast.style.position = "fixed";
			toast.style.top = "40px";
			toast.style.left = "40px";
			toast.style.width = "250px";
			toast.id = "toast";
			toast.style.padding = "10px 20px";

			toast.appendChild(document.createTextNode(await response.text()));

			var header_img = document.getElementById("header_img");
			header_img.appendChild(toast);

			setTimeout(function(){
				toast.parentNode.removeChild(toast);
			}, 9000);
		})()
    	return;
    }
}


/** Apply Item content to page using the API
 * @param base_id String to contain the base id of the object
 * @param link_suffix String containing the link suffix to connect to self api
 */
async function item_api_wrapper(base_id, link_suffix) {
	// Clear Item Content
	['_CATEGORY_I', '_DESCRIPTOR_I', '_NAME', '_TEXT', '_DESCRIBE'].forEach(s => document.getElementById(base_id + s).value = '');

	// Get from API
	var content = await get_api_content(link_suffix);

	// Setup applicator
	var applicator = {
		'_DESCRIPTOR_I': 'CATEGORY',
		'_NAME': 'TITLE'
	};
	if (content['Expandable']) {
		applicator['_TEXT'] = 'Description';
	} else {
		applicator['_DESCRIBE'] = 'Description';
	}

	// Run it back
	Object.keys(applicator).forEach(key => {
		document.getElementById(base_id + key).value = content[applicator[key]];
	})
	document.getElementById(base_id + "_CATEGORY_I").value = content['Cost'] + ' gp';
}


/** Apply Item content to page using the API
 * @param base_id String to contain the base id of the object
 * @param link_suffix String containing the link suffix to connect to self api
 */
async function owner_api_wrapper(base_id, link_suffix) {
	// Clear Item Content
	['_TRAIT_1', '_TRAIT_2', '_DESCRIBE', '_NAME', '_RACE', '_GENDER', '_AGE'].forEach(s => document.getElementById(base_id + s).value = '');

	// Get from API
	var content = await get_api_content(link_suffix);

	// Setup applicator

	var applicator = {
		'_NAME': 'Name',
		'_RACE': 'Race',
		'_GENDER': 'Gender',
		'_AGE': 'Age',
	};

	// Run it back
	Object.keys(applicator).forEach(key => {
		document.getElementById(base_id + key).value = content[applicator[key]];
	})
	document.getElementById(base_id + "_TRAIT_1").value = content['Traits'][0];
	document.getElementById(base_id + "_TRAIT_2").value = content['Traits'][1];
	document.getElementById(base_id + "_DESCRIBE").value = content['Story'][0];
}
