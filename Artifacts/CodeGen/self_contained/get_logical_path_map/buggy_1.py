def get_logical_path_map(inventory, version):
	"""
	Get a map of logical paths in state to files on disk for version in inventory.

Returns a dictionary: logical_path_in_state -> set(content_files)

The set of content_files may includes references to duplicate files in
later versions than the version being described.
	"""
	logical_path_map = {}
	logical_paths = inventory.get_logical_paths()
	for logical_path in logical_paths:
		file_path = inventory.get_file_path(logical_path)
		if file_path!= None:
			logical_path_in_state = logical_path.split("/")[-1]
			if logical_path_in_state not in logical_path_map:
				logical_path_map[logical_path_in_state] = set()
			logical_path_map[logical_path_in_state].add(file_path)
	return logical_path_map

