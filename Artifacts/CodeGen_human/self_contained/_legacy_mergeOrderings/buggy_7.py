def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	if not orderings:
		return orderings
	if len(orderings) == 1:
		return orderings
	result = []
	for ordering in orderings:
		if not isinstance(ordering, (list, tuple)):
			ordering = (ordering,)
		for ordering_ in orderings:
			if ordering_ not in ordering:
				ordering += ordering_
		result += ordering
	return result

