def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	return [c for c in classes if not c.__bases__]