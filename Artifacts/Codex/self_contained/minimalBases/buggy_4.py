def minimalBases(classes):
	if not classes:
		return classes
	classes = list(classes)
	i = 0
	while i < len(classes):
		j = i + 1
		while j < len(classes):
			if classes[i] == classes[j]:
				del classes[j]
			elif issubclass(classes[i], classes[j]):
				del classes[i]
				i -= 1
				break
			elif issubclass(classes[j], classes[i]):
				del classes[j]
			else:
				j += 1
		i += 1
	return classes

