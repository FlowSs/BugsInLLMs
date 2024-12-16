def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	if not orderings:
		return orderings
	if len(orderings) == 1:
		return orderings[0]
	#