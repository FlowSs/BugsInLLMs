def _dictsum(dicts):
	result = defaultdict(int)

	for d in dicts:
		for k, v in d.items():
			result[k] += v

	return result

