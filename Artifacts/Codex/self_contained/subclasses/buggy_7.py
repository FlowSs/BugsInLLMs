def subclasses(cls):
	for subclass in cls.__subclasses__():
		for subsubclass in subclasses(subclass):
			yield subsubclass
		yield subclass

