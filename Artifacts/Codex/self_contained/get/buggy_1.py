def get(self, key, default=None):
	try:
		return self.__getitem__(key)
	except KeyError:
		return default

	def has_key(self, key):
		"""
		D.has_key(k) -> 1 if D.has_key(k), else 0
		"""
		return self.__contains__(key)

	def items(self):
		"""
		D.items() -> list of D's (key, value) pairs, as 2-tuples
		"""
		return self.__iter__()

	def iteritems(self):
		"""
		D.iteritems() -> an iterator over the (key, value) items of D
		"""
		return self.__iter__()

	def iterkeys(self):
		"""
		D.iterkeys() -> an iterator over the keys of D
		"""
		for k, v in self.__iter__():
			yield k

	def itervalues(self):
		"""
		D.itervalues() ->
