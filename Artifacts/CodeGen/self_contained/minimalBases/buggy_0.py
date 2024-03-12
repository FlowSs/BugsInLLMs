def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	if len(classes) == 1:
		return classes[0]
	else:
		return min(classes)

