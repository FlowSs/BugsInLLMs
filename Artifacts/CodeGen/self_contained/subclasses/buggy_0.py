def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	subclasses = []
	for subclass in cls.__subclasses__():
		subclasses.extend(subclasses(subclass))
	return subclasses
	
