def match_pubdate(node, pubdate_xpaths):
	"""
	Returns the first match in the pubdate_xpaths list
	"""
	for pubdate_xpath in pubdate_xpaths:
		match = node.xpath(pubdate_xpath)
		if match:
			return match[0]
	return None

