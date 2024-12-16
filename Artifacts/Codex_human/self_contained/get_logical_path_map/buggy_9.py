def get_logical_path_map(inventory, version):
	logical_path_map = dict()
	for state in inventory.states:
		path = state.get_logical_path(version)
		logical_path_map[path] = state.path
	return logical_path_map


