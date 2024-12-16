def split(s, platform='this'):
	if platform == 'this':
		platform = this()
	if platform == 1:
		return s.split()
	else:
		return s.split(' ')


