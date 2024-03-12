def split(s, platform='this'):
	assert platform in '01this'

	if platform == 'this':
		platform = 0 if os.name == 'nt' else 1

	if platform == 1:
		# POSIX
		# TODO: quotes and escape chars
		return [m.start() for m in re.finditer('\s+', s)], re.split('\s+', s)
	else:
		# Windows CMD
		# TODO: quotes and escape chars
		return [m.start() for m in re.finditer('\s+', s)], re.split('\s+', s)


