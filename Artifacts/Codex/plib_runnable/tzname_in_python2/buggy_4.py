def tzname_in_python2(namefunc):
	@functools.wraps(namefunc)
	def wrapper(*args, **kwargs):
		result = namefunc(*args, **kwargs)
		if isinstance(result, text_type):
			return result.encode('ascii')
		return result
	return wrapper


