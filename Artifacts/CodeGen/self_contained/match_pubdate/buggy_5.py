def match_pubdate(node, pubdate_xpaths):
	"""
	Returns the first match in the pubdate_xpaths list
	"""
	match_pubdate = None
	for pubdate_xpath in pubdate_xpaths:
		pubdate = get_element_text(node, pubdate_xpath)
		if match_pubdate is None or pubdate.strip()!= match_pubdate.strip():
			match_pubdate = pubdate
	return match_pubdate

