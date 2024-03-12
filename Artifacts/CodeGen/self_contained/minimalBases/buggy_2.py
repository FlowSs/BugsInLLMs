def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	if len(classes) == 0:
		return []
	elif len(classes) == 1:
		return classes
	else:
		minimal = []
		classes.sort()
		for i in range(len(classes)):
			minimal.append(classes[i])
		return minimal

