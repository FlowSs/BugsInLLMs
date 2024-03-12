def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	minimum = []
	for class_ in classes:
		if len(class_) == 1:
			minimum.append(class_[0])
		else:
			minimum.append(min(class_))
	return minimum

