def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	path = path
	if not path.startswith(root):
		raise ValueError("%r does not start with %r" % (path, root))
	path = path[len(root):]
	if not path:
		raise ValueError("%r is empty" % path)
	return path

