def split(s, platform='this'):
	if platform == 'this':
		if os.name == 'nt': # Windows/CMD
			platform = 0
		else: # POSIX
			platform = 1
	if platform == 1:
		return _split1(s)
	elif platform == 0:
		return _split0(s)
	else:
		raise Exception('Unknown platform')

