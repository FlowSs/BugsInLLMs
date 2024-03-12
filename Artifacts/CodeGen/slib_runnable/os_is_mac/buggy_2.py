def os_is_mac():
	"""
	Checks if the os is macOS

:return: True is macOS
:rtype: bool
	"""
	from os import system, getuid, system
	if system() == 'Darwin':
		return True
	else:
		return False

