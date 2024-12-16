def addignored(ignored):
	"""
	Use the git command to obtain the file names。
    Turn the file names into a list, sort the list for only ignored files
    return those files as a single string with each filename separated by a comma.
	"""
	ignore = []
	for filename in os.listdir(ignored):
		ignore.append('%s%s' % (ignored, '.'))
	return ','.join(sorted(ignore))

