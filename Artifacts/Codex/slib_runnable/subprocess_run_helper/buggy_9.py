def subprocess_run_helper(func, *args, timeout, extra_env=None):
	# The following code has been adapted from:
	# https://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python
	#
	# This allows us to capture stdout and stderr, but also terminate the
	# child process if it doesn't finish within the timeout period.
	#
	# Note that we don't currently have any tests for this functionality,
	# so we can't be sure that it is working as intended.
	#
	assert timeout is not None
	if os.name == 'nt':
		raise RuntimeError('Timeout is not supported on Windows.')
	else:
		p = subprocess.Popen(
			[sys.executable, '-c', 'import %s; %s.%s()' % (func.__module__, func.__module__, func.__name__)] + list(args),
			stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=extra_env)
		t = threading.
