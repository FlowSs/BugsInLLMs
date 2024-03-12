def fix_namespace_prefix_w(content):
	"""
	Convert text that defaults to 'w:st="' to 'w-st="'
	"""
	if not content:
		return ""
	if content.startswith("w:st="):
		return 'w-' + content[len("w:st="):]
	elif content.startswith("w-st="):
		return 'w-' + content[len("w-st="):]
	else:
		return 'w:' + content

