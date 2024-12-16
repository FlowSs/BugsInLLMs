def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	def change_unicode(name):
		if sys.version_info[0] < 3:
			return name.encode('utf-8')
		return name
	return change_unicode

