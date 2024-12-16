def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	from inspect import isclass
	subclasses = []
	for subclass in cls.__subclasses__():
		if not isclass(subclass):
			subclasses.append(subclass)
		else:
			subclasses.extend(subclasses(subclass))
	return subclasses

