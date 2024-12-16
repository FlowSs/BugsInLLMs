def process_text_links(text):
	# Scan the text for links and add attributes to them.
	tree = html.fromstring(text)
	for link in tree.xpath('//a'):
		href = link.attrib.get('href')
		if href is None:
			continue
		# Strip trailing slashes and query strings.
		href = href.rstrip('/')
		href = href.split('?', 1)[0]
		# Ignore mailto: links.
		if href.startswith('mailto:'):
			continue
		# Ignore links to the current page.
		if href == request.path:
			continue
		# Check if the link is internal or external.
		if href.startswith('/'):
			# Internal link.
			# Check if it points to a page that exists.
			if Page.query.filter_by(path=href).first() is not None:
				# Page exists.
				# Add the rel and target attributes.
			
