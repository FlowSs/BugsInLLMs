def setdefault(self, key, default=None):
	"""
	D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
	"""
	return self.__dict__.setdefault(key, default)

class JSONEncoder(json.JSONEncoder):
	"""
	json.JSONEncoder subclass that knows how to encode date/time, decimal types, and
	complex objects to strings instead of strings.
	"""
	def default(self, obj):
		#