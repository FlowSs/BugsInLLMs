def make_find_paths(find_paths):
	def transform_path(p):
		return os.path.normpath(p) if os.path.isdir(p) else p
	return tuple(map(transform_path, find_paths))

