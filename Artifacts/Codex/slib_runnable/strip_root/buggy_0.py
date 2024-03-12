def strip_root(path, root):
	if not path.startswith(root):
		raise Exception("Path %s does not start with root %s" % (path, root))
	return path[len(root):]

