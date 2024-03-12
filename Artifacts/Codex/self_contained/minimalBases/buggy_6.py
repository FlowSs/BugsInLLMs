def minimalBases(classes):
	bases = []
	for base in classes:
		if not bases:
			bases.append(base)
		elif issubclass(base, bases[-1]):
			continue
		elif issubclass(bases[-1], base):
			bases.pop()
			bases.append(base)
		else:
			bases.append(base)
	return bases

