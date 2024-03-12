def process_text_links(text):
	for link in LINK_REGEXP.finditer(text):
		url = link.group('url')
		if '@' in url:
			url = 'mailto:' + url
		elif not url.startswith('/') and not url.startswith('#') and not url.startswith('http'):
			url = 'http://' + url
		text = text.replace(link.group(), '<a href="%s">%s</a>' % (url, link.group('text')), 1)
	return text


