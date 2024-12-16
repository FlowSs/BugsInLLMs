def match_pubdate(node, pubdate_xpaths):
	for xpath in pubdate_xpaths:
		pubdate = node.find(xpath)
		if pubdate is not None:
			return pubdate.text
	return None

