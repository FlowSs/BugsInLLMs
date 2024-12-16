def match_pubdate(node, pubdate_xpaths):
	"""
	For the given node, returns the first match in the pubdate_xpaths list.
	"""
	for pubdate_xpath in pubdate_xpaths:
		pubdate = node.get(pubdate_xpath)
		if pubdate is not None:
			return pubdate