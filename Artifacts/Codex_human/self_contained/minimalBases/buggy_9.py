def minimalBases(classes):
	minimal = []
	for c in classes:
		for c2 in classes:
			if c == c2: continue
			if c2.isSubclassOf(c): break
		else:
			minimal.append(c)
	return minimal

