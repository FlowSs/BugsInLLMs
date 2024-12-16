def _dictsum(dicts):
	return reduce(lambda x, y: dict(Counter(x) + Counter(y)), dicts)


