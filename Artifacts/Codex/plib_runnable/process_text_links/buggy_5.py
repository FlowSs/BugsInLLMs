def process_text_links(text):
	# Add target="_blank" to all links
	text = re.sub(r'<a ([^>]*)href="([^"]*)"([^>]*)>', r'<a \1href="\2" target="_blank"\3>', text)

	# Add rel="nofollow" to all links
	text = re.sub(r'<a ([^>]*)href="([^"]*)"([^>]*)>', r'<a \1href="\2" rel="nofollow"\3>', text)

	# Linkify textual links
	text = re.sub(r'(https?://[^\s<>"]*[^\s<>"\.])', r'<a href="\1">\1</a>', text)
	text = re.sub(r'([^\/])(www\.[^\s<>"]*[^\s<>"\.])', r'\1<a href="http://\2">\2</a>', text)

	# Linkify email addresses
	text = re.sub(r'([
