def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#