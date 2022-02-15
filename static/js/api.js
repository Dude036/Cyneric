

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
	['_Category_I', '_Descriptor_I', '_Name', '_Text', '_Describe'].forEach(s => document.getElementById(base_id + s).value = '');

	// Get from API
	var content = await get_api_content(link_suffix);

	// Setup applicator
	var applicator = {
		'_Descriptor_I': 'Category',
		'_Name': 'Title'
	};
	if (content['Expandable']) {
		applicator['_Text'] = 'Description';
	} else {
		applicator['_Describe'] = 'Description';
	}

	// Run it back
	Object.keys(applicator).forEach(key => {
		document.getElementById(base_id + key).value = content[applicator[key]];
	})
	document.getElementById(base_id + "_Category_I").value = content['Cost'] + ' gp';

	set_session_storage();
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

	set_session_storage();
}
