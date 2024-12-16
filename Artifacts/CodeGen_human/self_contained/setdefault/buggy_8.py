def setdefault(self, key, default=None):
	"""
	If a key exists in the class, the value corresponding to the key is returned. Otherwise, the value corresponding to the key is set to default.
	"""
	return self.__dict__.setdefault(key, default)

