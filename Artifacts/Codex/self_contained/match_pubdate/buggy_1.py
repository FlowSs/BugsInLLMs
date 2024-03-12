def match_pubdate(node, pubdate_xpaths):
	for p in pubdate_xpaths:
		try:
			pubdate = node.xpath(p)[0]
			if pubdate:
				return pubdate
		except:
			pass
	return None

