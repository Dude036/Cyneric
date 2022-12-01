/***********************************
 * Convert JSON to HTML for export *
 ***********************************/

/**Export everything into an object, then turn the object data into a usable html file
 */
function export_page() {
  // Get String of file
  new_doc = convert_to_html();

  // Parse to a DOM Document
  if (DEBUG) { console.log('Attempting to convert to a DOM object'); }
  var new_dom = new DOMParser().parseFromString(new_doc, "text/html");
  if (DEBUG) { console.log(new_dom); }

  // Save to file
  var textFile = null
  var new_doc_blob = new Blob([new_doc], {type: 'text/html;charset=utf-8'});
  saveAs(new_doc_blob, document.getElementById("header").value + '.custom.html');
}


/**Export everything into an HTML String
 * @return HTML text of page
 */
function convert_to_html() {
  if (DEBUG) { console.log("Exporting Page"); }
  // Clear export object
  export_obj = export_json(true);

  /************************************************************************************************/

  // Create new Document for printing
  // Going with a simple String to be coppied
  // Boiler plate CSS header stuffs
  var new_doc = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Custom HTML</title><style>body{max-width:1000px;margin-left:auto;margin-right:auto;padding-left:5px;padding-right:5px}html{font-family:Arial}h1,h2{color:#000;text-align:center}.center{text-align:center}.bold{font-weight:700}.emp{font-style:italic}table{border:1px solid #000;border-spacing:0}table tr th{background-color:gray;color:#fff;padding:5px}table tr td{margin:0;padding:5px}.text-xs{font-size:12px}.text-sm{font-size:14px}.text-md{font-size:18px}.text-lg{font-size:24px}.text-xl{font-size:32px}.wrapper-box{width:100%;border:2px solid #000;margin-bottom:60px;padding:5px;}.inventory-table{width:100%;}.suggestion{padding:2px 0;margin:0;list-style:none}.suggestion li{border:1px solid #000;background-color:#ddd;padding:2px 4px;margin:5px 10px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.suggestion li:active{background-color:#404040}.suggestion li:hover{background-color:grey}.attacks{display:flex;flex-wrap:wrap;align-items:flex-start;width:100%;padding-top:10px;padding-bottom:20px}.attacks table{width:44%;margin-left:3%;margin-right:3%;margin-bottom:1%}.header{background-color:#f1f1f1;position:fixed;top:0;left:0;padding:5px 5px}.header ul{display:none;list-style-type:none;padding-left:10px;margin-top:0}.header a{float:left;color:#000;text-align:center;text-decoration:none;padding:5px 5px}.header a:hover{background-color:#ddd}.header a.active{background-color:#02f}.crit tr:nth-child(even){background-color:#eee}.link{text-align:center}.link li{padding-bottom:10px}.link a{border:1px solid #000;width:60%;text-decoration:none;color:#222;background-color:#ddd;padding:3px 3px 3px 3px}.link a:hover{background-color:#222;color:#ddd}.sidebar{float:left;position:fixed;top:0;right:0;margin:5px}.sidebar_object{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;padding:10px 20px;border-style:solid;border:2px;background-color:#efefef}.sidebar_object:hover{background-color:#cfcfcf}.sidebar_object:active{background-color:#0000cf;color:#efefef}.traits {padding: 5px 2px;width: 95%;margin: 15px 10px;display: flex;flex-wrap: wrap;align-items: flex-start;}.traits_obj {justify-content: flex-start;width: 23%;margin: 0px 10px;padding: 3px;background-color:#666666;color:#EFEFEF;}.spells {width: 95%;display: flex;padding: 5px 2px;margin: 2px 5px;flex-wrap: wrap;align-items: flex-start;}.spells_obj {justify-content: flex-start;width: 31%;margin: 0px 5px;padding: 3px;}@media only screen and (max-width:600px){.header a{float:none;display:block;text-align:left;font-size:20px}.header img{height:50px;width:50px}.header-right{float:none}}.divider{display: flex;flex-direction: row}.divider:before, .divider:after{content: "";flex: 1 1;border-bottom: 1px solid;margin: auto}.divider:before{margin-right: 10px}.divider:after{margin-left: 10px}</style><script>function show_hide(ident) {var a = document.getElementById(ident);if (a.style.display === "none") {a.style.display = "block";} else {a.style.display = "none";}}</script></head>';
  new_doc += "<body><!-- Thanks for using my Custom HTML editor! Feel free to visit again! -->"

  // Header and description
  new_doc += "<h1>" + export_obj['Name'] + "</h1>" + export_obj['Description'];

  // loop through all Objects
  export_obj['Data'].forEach(function(data_obj) {
    if (data_obj == null) { return; }
    if (data_obj['Type'] === 'Store') {
      new_doc += export_store_html(data_obj);
    } else if (data_obj['Type'] === 'Table') {
      new_doc += export_table_html(data_obj);
    } else if (data_obj['Type'] === 'List') {
      new_doc += export_list_html(data_obj);
    } else if (data_obj['Type'].startsWith('Monster')) {
      new_doc += export_monster_html(data_obj);
    } else if (data_obj['Type'].startsWith('Hazard')) {
      new_doc += export_hazard_html(data_obj);
    } else if (data_obj['Type'] === 'Divider') {
      new_doc += export_divider_html(data_obj);
    } else if (data_obj['Type'] === 'Paragraph') {
      new_doc += export_paragraph_html(data_obj);
    }
  });

  new_doc += "</body></html>"

  // Notice for getting the HTML prettified
  new_doc += "\n\n<!-- If you're looking to prettify the above Code, I recommend using the following services. -->"
  new_doc += "\n<!-- HTML: https://jsonformatter.org/html-pretty-print -->"
  new_doc += "\n<!-- CSS: https://www.cleancss.com/css-beautify/ -->"

  if (DEBUG) { console.log('RAW String'); }
  if (DEBUG) { console.log(new_doc); }
  return new_doc;
}


/** Setup a preview of an exported page.
 */
function export_preview() {
    refresh_page_json()
    save_json_from_page();
    var new_window = window.open("", "_blank");
    new_window.document.write(convert_to_html());
}


/**Convert Page JSON data to html for a store
 * @param data_obj JSON object from storage
 * @return HTML string
 */
function export_store_html(temp_store) {
  if (DEBUG) { console.log("Adding store: " + temp_store['Owner']['Store Name']) };

  // Owner Information
  var store_str = '<div class="wrapper-box" style="margin-bottom: 60px;">';
  store_str += '<span class="text-lg bold">' + temp_store['Owner']['Store Name'] + '</span><br>';
  store_str += '<span class="bold text-md">Proprietor: </span><span class="text-md">' + temp_store['Owner']['Name'] + '</span>';

  store_str += '<ul>';
  ['Race', 'Gender', 'Age', 'Trait 1', 'Trait 2'].forEach(function(item, i, arr) {
    store_str += '<li><span class="bold">' + item + ': </span>' + temp_store['Owner'][item] + '</li>';
  })
  store_str += '</ul>';
  store_str += '<p>' + temp_store['Owner']['Description'] + '</p>';

  store_str += export_table_html(temp_store);
  
  store_str += '</div>'
  return store_str;
}


/**Convert Page JSON data to html for a table
 * @param data_obj JSON object from storage
 * @return HTML string
 */
function export_table_html(temp_table) {
  if (DEBUG) { console.log("Adding table: " + temp_table['Name'] + ' | Type: ' + temp_table['Type']) };

  var table_str = '';
  if (temp_table['Type'] === 'Table') {
    table_str += '<h3 class="center">' + temp_table['Name'] + '</h3><table class="inventory-table" style="width:100%">';
    table_str += '<table class="inventory-table wrapper-box" style="width:100%;"">'
  } else {
    table_str += '<table class="inventory-table" style="width:100%">'
  }

  // Make Table HTML
  for (var x = 0; x < temp_table['Data'].length; x++) {

    // For Items
    table_str += '<tr>'
    if (temp_table['Data'][x]['Type'] == 'Item') {
      if (DEBUG) { console.log("Explicit Item found"); }
      export_counter++;
      if (temp_table['Data'][x]['Text'] === '') {
        table_str += '<td style="width:50%;"><span class="text-md">';
        table_str += temp_table['Data'][x]['Name'] + '</span><br><span class="text-sm emp">';
        table_str += temp_table['Data'][x]['Describe'] + '</span></td><td>';
        table_str += temp_table['Data'][x]['Category'] + '</td><td>' + temp_table['Data'][x]['Descriptor'] + '</td>';
      } else {
        table_str += '<td style="width:50%;"><span class="text-md" onclick="show_hide(\'' + export_counter + '\')" style="color:blue;">';
        table_str += temp_table['Data'][x]['Name'] + '</span><br><span class="text-sm emp" id="' + export_counter + '" style="display: none;">';
        table_str += temp_table['Data'][x]['Describe'] + '<p>' + temp_table['Data'][x]['Text'] + '</p></span></td><td>';
        table_str += temp_table['Data'][x]['Category'] + '</td><td>' + temp_table['Data'][x]['Descriptor'] + '</td>';
      }
    } else if (temp_table['Data'][x]['Type'] == 'Wide') {
      // For Paragraphs
      table_str += '<td colspan="3"><p>' + temp_table['Data'][x]['Data'].replace(/(\n\n|\r\n\r\n)/g, '</p><p>'); + '</p></td>'
    } else {
      // For Blanks
      if (DEBUG) { console.log("Blank row found"); }
      var sorted_keys = Object.keys(temp_table['Data'][x]);
      sorted_keys.sort()

      for (var y = 0; y < sorted_keys.length - 1; y++) {
        if (sorted_keys[y].endsWith('H')) {
          table_str += '<th>' + temp_table['Data'][x][sorted_keys[y]] + '</th>'
        } else {
          table_str += '<td>' + temp_table['Data'][x][sorted_keys[y]] + '</td>'
        }
      }
    }
    table_str += '</tr>'
  }
  table_str += '</table>'
  return table_str;
}


/**Convert Page JSON data to html for a list
 * @param data_obj JSON object from storage
 * @return HTML string
 */
function export_list_html(temp_list) {
  if (DEBUG) { console.log("Adding list: " + temp_list['Name']) };

  var list_str = '';
  if (temp_list['Title'] != '') {
    list_str = '<div class="text-md bold">' + temp_list['Title'] +  '</div>';
  }
  list_str += '<ul>'
  for (var x = 0; x < temp_list['Data'].length; x++) {
    list_str += '<li>';
    list_str += temp_list['Data'][x]['Bold'] ? '<b>' : '';
    list_str += temp_list['Data'][x]['Underline'] ? '<u>' : '';
    list_str += temp_list['Data'][x]['Data'];
    list_str += temp_list['Data'][x]['Underline'] ? '</u>' : '';
    list_str += temp_list['Data'][x]['Bold'] ? '</b>' : '';
    list_str += '</li>'
  }
  list_str += '</ul>'

  return list_str;
}


/**Convert Page JSON data to html for a monster
 * @param data_obj JSON object from storage
 * @return HTML string
 */
function export_monster_html(temp_monster) {
  if (DEBUG) { console.log("Adding monster: " + temp_monster['Name']) };
  var monster_str = '<table class="wrapper-box" style="margin-bottom: 60px;"><tr><td>';
  monster_str += '<span class="text-lg bold">' + temp_monster['Name']
  monster_str += '</span> - <span class="text-md bold">CR: ' + temp_monster['Cr'] + '</span>'
  monster_str += '<span style="float: right;" class="text-md bold">XP: ' + temp_monster['Xp'] + '</span><br>'
  
  // Traits if Second edition
  if (temp_monster['Edition'] === '2') {
    monster_str += '<ul style="margin: 2px 0px;padding: 0px;display: inline-flex;list-style-type: none;background-color: #d8c483">';
    for (var x = 0; x < temp_monster['Traits'].length; x++) {
      var bgc = '#CFCFCF;'
      if (['LE', 'LN', 'LG', 'NE', 'N', 'NG', 'CE', 'CN', 'CG'].includes(temp_monster['Traits'][x].toUpperCase())) {
        bgc = '#4287f5';
      } else if (['diminutive', 'tiny', 'small', 'medium', 'large', 'huge', 'gargantuan'].includes(temp_monster['Traits'][x].toLowerCase())) {
        bgc = '#478c42';
      }
      monster_str += '<li style="margin: 2px 5px; padding: 2px 5px; background-color: ' + bgc + '">' + temp_monster['Traits'][x] + '</li>';
    }
    monster_str += '</ul><br>';
  }
  monster_str += '<span class="text-md emp">Alignment: ' + temp_monster['Alignment'] + '</span>' + temp_monster['Description'];
  
  // Adding Info Section
  monster_str += '</td></tr><tr><td><ul style="column-count: 2;list-style-type: none;margin: 5px;">'
  
  var stat_list;
  if (temp_monster['Edition'] == '2') {
    stat_list = PATHFINDER_2_STATS;
  } else if (temp_monster['Edition'] == '1') {
    stat_list = PATHFINDER_1_STATS;
  } else if (temp_monster['Edition'] == '5') {
    stat_list = DND_5_STATS;
  }

  for (var i = 0; i < stat_list.length; i++) {
    // 5e Saves are checkboxes
    if (/[A-Z]{3} Save/.test(stat_list[i])) {
      if (temp_monster[stat_list[i]]) {
        monster_str += '<li><span class="bold">Saving Throw:</span> ' + stat_list[i] + '</li>';
      }
    } else {
      monster_str += '<li><span class="bold">' + stat_list[i] + '</span> ' + temp_monster[stat_list[i]] + '</li>';
    }
  }

  // Info Wrap up
  monster_str += '</ul>';
  monster_str += '</td></tr>';

  // Stat Table
  monster_str += '<tr><td><table class="inventory-table"><tr><th>STR</th><th>DEX</th><th>CON</th><th>INT</th><th>WIS</th><th>CHA</th></tr><tr>';
  ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'].forEach(function(stat) {
    monster_str += '<td>';
    if (is_numeric(temp_monster[stat])) {
      monster_str += temp_monster[stat] + ' (' + get_mod(temp_monster[stat]) + ')';
    } else {
      monster_str += temp_monster[stat];
    }
    monster_str += '</td>';
  })
  monster_str += '</tr></table></td></tr>';

  // Add actions
  monster_str += '<tr><td><div class="attacks">';

  for (var x = 0; x < temp_monster['Actions'].length; x++) {
    var temp_action = temp_monster['Actions'][x];
    monster_str += '<table><tr><th>' + temp_action['Name'];
    if (temp_monster['Edition'] == '5' && temp_action['Legendary']) {
      monster_str += ' - <span style="color:#FFD700">Legendary</span>';
    }
    if (temp_monster['Edition'] == '2') {
      monster_str += ' - Cost: ';
      if (temp_action['Cost'] == 'Free') {
        monster_str += '<abbr title="Free Action">&#9671;</abbr>';
      } else if (temp_action['Cost'] == 'Reaction') {
        monster_str += '<abbr title="Reaction">&#8634;</abbr>';
      } else if (temp_action['Cost'] == '1 Action') {
        monster_str += '<abbr title="1 Action">&#9830;</abbr>';
      } else if (temp_action['Cost'] == '2 Action') {
        monster_str += '<abbr title="2 Action">&#9830;&#9830;</abbr>';
      } else if (temp_action['Cost'] == '3 Action') {
        monster_str += '<abbr title="3 Action">&#9830;&#9830;&#9830;</abbr>';
      }
    }
    monster_str += '</th></tr><tr><td>' + temp_action['Text'];
    monster_str += '</td></tr></table>';
  }
  monster_str += '</div></td></tr>';

  // Add Spell List if pertinent
  if (temp_monster['Spells'].length > 0) {
    monster_str += '<tr><td><table class="inventory-table"><tr><th style="width:20%;">Usage</th><th>Spell List</th></tr>';
    // Loop through Row
    for (var j = 0; j < temp_monster['Spells'].length; j++) {
      var temp_spell_row = temp_monster['Spells'][j];
      monster_str += '<tr><td><div>' + temp_spell_row['Uses'] + ' / times day</div><div>DC ' + temp_spell_row['Dc'] + '</div></td>';
      monster_str += '<td><div class="spells">';

      // Loop through Spells
      for (var k = 0; k < temp_spell_row['List'].length; k++) {
        monster_str += '<div class="spells_obj"><a href="' + temp_spell_row['List'][k]['Link'] + '">' + temp_spell_row['List'][k]['Name'] + '</a></div>'
      }
      monster_str += '</div></td></tr>';
    }
    monster_str += '</table>';
    monster_str += '</td></tr>';
  }

  // Monster Treasure
  monster_str += '<tr><td><h3 style="text-align:center;">Treasure</h3>';

  monster_str += export_table_html(temp_monster['Treasure']);
  monster_str += '</td></tr></table>';

  return monster_str;
}


/**Convert Page JSON data to html for a hazard
 * @param data_obj JSON object from storage
 * @return HTML string
 */
function export_hazard_html(temp_hazard) {
  if (DEBUG) { console.log("Adding hazard: " + temp_hazard['Name']) };
  var hazard_str = '<table class="wrapper-box" style="margin-bottom: 60px;"><tr><th>';
  hazard_str += '<div style="float: left">' + temp_hazard['Name'] + '</div>';
  hazard_str += '<div style="float: right">Hazard ' + temp_hazard['Cr'] + '</div>';

  // Traits
  hazard_str += '</th></tr><tr><td><div class="traits">';

  for (var x = 0; x < temp_hazard['Traits'].length; x++) {
    hazard_str += '<div class="traits_obj">' + temp_hazard['Traits'][x].toUpperCase() + '</div>'
  }

  hazard_str += '</div></td></tr><tr><td><ul>';

  // Permenant Set of Details
  hazard_str += '<li><b>Complexity: </b>' + temp_hazard['Complexity'] + '</li>'
  hazard_str += '<li><b>Stealth: </b>' + temp_hazard['Stealth'] + '</li>'
  hazard_str += '<li><b>Description: </b>' + temp_hazard['Description'] + '</li>'
  hazard_str += '<li><b>Disable: </b>' + temp_hazard['Disable'] + '</li>'

  hazard_str += '</ul</td></tr><tr><td><hr></td></tr><tr><td><ul>';

  // Custom details
  for (var x = 0; x < temp_hazard['Custom'].length; x++) {
    var temp_custom = temp_hazard['Custom'][x]
    hazard_str += '<li><b>' + Object.keys(temp_custom)[0] + ': </b>' + Object.values(temp_custom)[0] + '</li>'
  }
 
  hazard_str += '</ul></td></tr></table>';
  
  return hazard_str;
}


/**Convert Page JSON data to html for a divider
 * @param data_obj JSON object from storage
 * @return HTML string
 */
function export_divider_html(temp_divider) {
  if (DEBUG) { console.log("Adding divider: " + temp_divider['Name']) };

  var divider_str = '<div class="text-lg divider" style="margin-bottom: 60px;">';
  divider_str += temp_divider['Name'];
  divider_str += '</div>';
  return divider_str;
}


/**Convert Page JSON data to html for a paragraph
 * @param data_obj JSON object from storage
 * @return HTML string
 */
function export_paragraph_html(temp_paragraph) {
  if (DEBUG) { console.log("Adding paragraph") };

  var paragraph_str = '<p style="margin-bottom: 60px;">';

  // Double enter should result in a new paragraph
  paragraph_str += temp_paragraph['Text'].replace(/(\n\n|\r\n\r\n)/g, '</p><p style="margin-bottom: 60px;">');
  paragraph_str += '</p>';
  return paragraph_str;
}

