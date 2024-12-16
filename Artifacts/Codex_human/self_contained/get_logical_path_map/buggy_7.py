def get_logical_path_map(inventory, version):
	
	logical_path_map = {}
	
	for state in inventory.states:
		logical_path_map[state.name] = get_logical_path(state.name, version)
	
	return logical_path_map

