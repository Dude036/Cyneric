import generator.DMToolkit as dmk
import simplejson as json
import sqlite3
import os


def update_pf2e_db(table):
	# Initial setup to use the database
	connection = sqlite3.connect(os.path.join(os.getcwd(), '2e_items.sqlite3'))
	cursor = connection.cursor()
	
	if table == 'Weapons':
		# Verify the existence of the Weapons table
		check = cursor.execute("SELECT name FROM sqlite_master WHERE name='weapons'")
		if check.fetchone() is None:
			cursor.execute('CREATE TABLE weapons(name text, bulk text, category text, cost real, hands text, level int, link text, rarity text, traits text);')
			connection.commit()

		# Remove all entries on table
		deletion = cursor.execute("DELETE FROM weapons;")
		connection.commit()

		# Rebuild from JSON
		Weapons = json.load(open(os.path.join(os.getcwd(), 'generator', 'DMToolkit', 'resource', '2e_base_weapons.json'), 'r'), encoding='utf-8')
		for key, val in Weapons.items():
			value_statement = (key, val['Bulk'], val['Category'], val['Cost'], val['Hands'], val['Level'], val['Link'], val['Rarity'], str(val['Traits']),)

			insert = cursor.execute("INSERT INTO weapons VALUES " + str(value_statement) + ';')

		# Commit inserted 
		connection.commit()

		# Pack the file to be space optimized, and close
		cursor.execute("VACUUM")
		connection.close()
		return {}
	else:
		return {"ERROR": "Table not specified"}
