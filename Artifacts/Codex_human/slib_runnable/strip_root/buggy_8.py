def strip_root(path, root):
	try:
		return path.split(root, 1)[1]
	except:
		raise Exception("Path %s does not start with %s" % (path, root))

