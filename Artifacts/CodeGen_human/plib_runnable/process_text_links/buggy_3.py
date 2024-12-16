def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	out = []
	for line in text.split('\n'):
		if line.startswith('#