def get_logical_path_map(inventory, version):
	# Get the inventory file
	file_path = inventory.get_inventory_file_path(version)

	# Store the file path of the states in the list type.
	logical_path_map = {}
	with open(file_path, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			logical_path_map[row[0]] = row[1]

	return logical_path_map

