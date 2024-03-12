def tzname_in_python2(namefunc):
	if python2:
		@wraps(namefunc)
		def newfunc(*args, **kwargs):
			return namefunc(*args, **kwargs).encode('utf-8')
		return newfunc
	else:
		return namefunc

