def _insert(INV):
	name = raw_input("Name: ")
	category = raw_input("Category: ")
	company = raw_input("Company Name: ")
	designation = raw_input("Designation: ")
	experience = raw_input("Experience: ")
	skillset = raw_input("Skillset: ")
	location = raw_input("Location: ")

	if name in INV.get('name'):
		INV['record'][name] = {'name': name, 'category': category, 'company': company,
		 'designation': designation, 'experience': experience,
		 'skillset': skillset, 'location': location}
		# INV['location'][location] = name
		location_record(INV, location, name)
		print INV
		
	else:
		INV['name'].append(name)
		INV['record'][name] = {'name': name, 'category': category, 'company': company,
		 'designation': designation, 'experience': experience,
		 'skillset': skillset, 'location': location}
		# INV['location'][location] = name
		location_record(INV, location, name)
		print INV

def _search(INV, search_term):
	if '=' in search_term:
		key, val = search_term.split('=')
		name = INV[key].get(val)
		if name:
			for i in name:
				print INV['record'][i]
		else:
			print "Record does not exisi for {}".format(search_term)
	else:
		search_words = search_term.split()
		name_set = set()
		for word in search_words:
			for k, v in INV['record'].items():
				if word in str(v):
					name_set.add(k)
		if not len(name_set):
			print "No record found!"
		else:
			for i in name_set:
				print INV['record'].get(i)


def location_record(INV, location, name):
	if INV['location'].get(location):
		INV['location'][location].append(name)
	else:
		INV['location'][location] = [name]

