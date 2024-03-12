def strip_root(path, root):
	if not path.startswith(root):
		raise ValueError("Path does not start with root: %s." % path)
	return path[len(root):]

