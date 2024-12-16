def subclasses(cls):
	subclasses = cls.__subclasses__()
	for sub in subclasses:
		subclasses.extend(sub.__subclasses__())
	return subclasses

