def split(s, platform='this'):
	if platform == 'this':
		platform = detect_platform()
	if platform == 1:
		return s.split('/')
	elif platform == 0:
		return s.split('\\')
	else:
		raise ValueError('Unknown platform: {0}'.format(platform))

