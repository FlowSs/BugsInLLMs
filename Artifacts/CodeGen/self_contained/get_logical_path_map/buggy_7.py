def get_logical_path_map(inventory, version):
	"""
	Get a map of logical paths in state to files on disk for version in inventory.

Returns a dictionary: logical_path_in_state -> set(content_files)

The set of content_files may includes references to duplicate files in
later versions than the version being described.
	"""
	logical_path_in_state = {}
	for state in inventory.states:
		for logical_path in inventory.get_logical_paths(state):
			if logical_path not in logical_path_in_state:
				logical_path_in_state[logical_path] = set()
			logical_path_in_state[logical_path].add(state)

	#