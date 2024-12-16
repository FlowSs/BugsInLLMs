def _replace_url_args(url, url_args):
	"""
	Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
	"""
	url = url.replace('?', '&')
	url_query = url.split('&')
	for i in range(len(url_query)):
		key, value = url_query[i].split('=')
		if key in url_args:
			url_args[key] = value
	return url.replace(url_args[key], value)
