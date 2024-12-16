def tzname_in_python2(namefunc):
	def wrapper(self, dt):
		names = namefunc(self, dt)
		if isinstance(names, tuple):
			return tuple(self.encode(x) for x in names)
		else:
			return self.encode(names)
	return wrapper


