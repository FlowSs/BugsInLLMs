def make_find_paths(find_paths):
	return [
		make_find_path_glob(find_path)
		for find_path in find_paths
	]

