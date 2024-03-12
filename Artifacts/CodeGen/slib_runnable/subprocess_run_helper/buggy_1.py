def subprocess_run_helper(func, *args, timeout, extra_env=None):
	"""
	Run a function in a sub-process.

Parameters
----------
func : function
    The function to be run.  It must be in a module that is importable.
*args : str
    Any additional command line arguments to be passed in
    the first argument to ``subprocess.run``.
extra_env : dict[str, str]
    Any additional environment variables to be set for the subprocess.
	"""
	if not isinstance(func, types.FunctionType):
		raise TypeError('func must be a function')
	if not hasattr(func, '__module__'):
		raise TypeError('func must be a function')

	if extra_env is None:
		extra_env = {}

	try:
		#