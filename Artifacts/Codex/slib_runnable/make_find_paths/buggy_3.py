def make_find_paths(find_paths):
	if find_paths is None:
		return None

	def transform_path(path):
		return 'sh:**/*{}*/**'.format(path)

	return [transform_path(path) if not path.startswith('pp:') else path for path in find_paths]
