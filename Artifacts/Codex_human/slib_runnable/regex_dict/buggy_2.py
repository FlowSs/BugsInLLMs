def regex_dict(item):
	return {re.compile(fnmatch.translate(k)): v for k, v in item.items()}


