def regex_dict(item):
	return {fnmatch.translate(key): value for key, value in item.items()}


