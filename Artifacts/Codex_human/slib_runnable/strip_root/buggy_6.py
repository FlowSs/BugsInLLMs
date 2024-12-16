def strip_root(path, root):
	if not path.startswith(root):
		raise exceptions.PathNotInRoot("{} is not in {}".format(path, root))
	return path[len(root):]

