def fix_namespace_prefix_w(content):
	"""
	Convert text that defaults to 'w:st="' to 'w-st="'
	"""
	return re.sub('(?<!(?:[^a-zA-Z])-w:)(?!:)', '-w-st="', content)

