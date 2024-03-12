def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2

tzname() API changed in Python 3. It used to return bytes, but was changed
to unicode strings
	"""
	def tzname_in_python3(name):
		if isinstance(name, bytes):
			return name.decode('utf-8')
		else:
			return name
	def tzname_in_python2(namefunc):
		def tzname_in_python3(name):
			if isinstance(name, bytes):
				return name.decode('utf-8')
			else:
				return name
		return tzname_in_python3
	return tzname_in_python2(namefunc)

