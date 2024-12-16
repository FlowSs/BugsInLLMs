def get_logical_path_map(inventory, version):
	logical_path_map = {}
	for state in inventory['states']:
		logical_path_map[state['path']] = os.path.join(version['path'], state['file_path'])
	return logical_path_map

