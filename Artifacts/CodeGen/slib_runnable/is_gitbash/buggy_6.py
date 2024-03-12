def is_gitbash():
	"""
	returns True if you run in a Windows gitbash

:return: True if gitbash
	"""
	if not os.path.exists('/usr/bin/git'):
		return False
	if not os.path.exists('/bin/bash'):
		return False
	if not os.path.exists('/usr/bin/git'):
		return False
	if not os.path.exists('/bin/bash'):
		return False
	return True