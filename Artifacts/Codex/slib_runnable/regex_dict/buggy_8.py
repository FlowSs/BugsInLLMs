def regex_dict(item):
	new_dict = {}
	for k, v in item.items():
		if isinstance(v, dict):
			new_dict[re.compile(fnmatch.translate(k))] = regex_dict(v)
		else:
			new_dict[re.compile(fnmatch.translate(k))] = v
	return new_dict

