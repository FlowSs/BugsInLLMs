def _legacy_mergeOrderings(orderings):
	return reduce(lambda x, y: x + [e for e in y if e not in x], orderings, [])

