def match_pubdate(node, pubdate_xpaths):
	"""
	For the given node, returns the first match in the pubdate_xpaths list.
	"""
	for pubdate_xpath in pubdate_xpaths:
		pubdate_xpath = pubdate_xpath.strip()
		pubdate_xpath = pubdate_xpath.replace("<", "").replace(">", "")
		pubdate_xpath = pubdate_xpath.replace(" ", "")
		pubdate_xpath = pubdate_xpath.replace("\n", "")
		pubdate_xpath = pubdate_xpath.replace("\r", "")
		pubdate_xpath = pubdate_xpath.replace("\t", "")
		pubdate_xpath = pubdate_xpath.replace("\u00A0", "")

		#