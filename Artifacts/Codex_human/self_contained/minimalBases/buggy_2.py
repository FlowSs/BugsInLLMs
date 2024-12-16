def minimalBases(classes):
	bases = []
	for c in classes:
		if c not in classes:
			bases.append(c)
	return bases


