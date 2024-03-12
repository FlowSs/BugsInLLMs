def process_text_links(text):
	# Linkify links in text
	text = linkify(text)

	# Add attributes to links
	soup = BeautifulSoup(text, 'html.parser')
	for link in soup.find_all('a'):
		link['target'] = '_blank'
		link['rel'] = 'noopener'

	return str(soup)


