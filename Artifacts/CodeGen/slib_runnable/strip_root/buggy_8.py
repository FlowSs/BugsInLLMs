def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	if path.startswith(root):
		path = path[len(root):]
	if path.startswith('..'):
		raise ValueError('root not a valid path: %s' % path)
	return path

