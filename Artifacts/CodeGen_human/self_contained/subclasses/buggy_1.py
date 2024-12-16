def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	return [c for c in cls.__subclasses__() if issubclass(c, cls)]

@contextlib.contextmanager
