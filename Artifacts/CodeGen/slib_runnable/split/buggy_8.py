def split(s, platform='this'):
	"""
	Multi-platform variant of shlex.split() for command-line splitting.
For use with subprocess, for argv injection etc. Using fast REGEX.

platform: 'this' = auto from current platform;
          1 = POSIX;
          0 = Windows/CMD
          (other values reserved)
	"""
	if platform not in ('this', '0', '1', '0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5'):
		raise ValueError('platform must be "this", "0", "1", "0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.0.0", "1.0.1", "1.0.2", "1.0.3", "1.0.4", "1.0.5"')

	if platform == 'this':
		#