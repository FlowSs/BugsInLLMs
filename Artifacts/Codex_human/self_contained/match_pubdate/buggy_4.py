def match_pubdate(node, pubdate_xpaths):
	for pubdate_xpath in pubdate_xpaths:
		pubdate_match = node.xpath(pubdate_xpath, namespaces=NAMESPACES)
		if pubdate_match:
			return pubdate_match[0]
	return None

