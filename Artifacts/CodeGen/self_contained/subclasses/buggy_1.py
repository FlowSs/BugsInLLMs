def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	if cls not in cls.__subclasses__():
		return [cls]
	return cls.__subclasses__() + \
		[c for c in cls.__subclasses__() if c not in cls.__subclasses__()]

