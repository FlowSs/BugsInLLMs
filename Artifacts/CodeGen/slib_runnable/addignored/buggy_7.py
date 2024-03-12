def addignored(ignored):
	"""
	Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
	"""
	ignored_files = []
	ignore_files = []
	with open(ignored) as f:
		for line in f:
			ignored_files.append(line.rstrip('\n'))
	for ignored_file in ignored_files:
		with open(ignored_file) as f:
			for line in f:
				ignore_files.append(line.rstrip('\n'))
	ignore_files.sort()
	ignored_files = ','.join(ignore_files)
	return ignored_files
