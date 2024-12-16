def minimalBases(classes):
	bases = []
	for cl in classes:
		if cl.subclasses is not None:
			for subcl in cl.subclasses:
				subcl.subclassOf.remove(cl)
		else:
			bases.append(cl)
	return bases

