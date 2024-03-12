def fix_namespace_prefix_w(content):
	"""
	Convert text that defaults to 'w:st="' to 'w-st="'
	"""
	if ':' in content:
		text = content.split(':')
		content = 'w:' + text[1].replace('"',"'") + '="' + text[0].replace('"',"'") + '"\n'
		return content
	else:
		return content

