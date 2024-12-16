def strip_root(path, root):
	if root == '':
		return path
	if not path.startswith(root):
		raise Exception("Invalid path: %s does not start with %s" % (path, root))
	return path[len(root):]


