def is_valid(self, identifier):
	return True

	def translate(self, identifier):
	"""
	Return display name. In this base implementation, simply return identifier. (D)
	"""
	return identifier

	def translate_reverse(self, name):
	"""
	Return identifier. In this base implementation, simply return name. (D)
	"""
	return name
