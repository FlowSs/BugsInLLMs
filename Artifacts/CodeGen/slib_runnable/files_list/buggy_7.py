def files_list(path):
	"""
	Return the files in `path`
	"""
	files = []
	for f in os.listdir(path):
		if os.path.isfile(os.path.join(path, f)):
			files.append(f)
		else:
			files = files + files_list(os.path.join(path, f))
	return files

