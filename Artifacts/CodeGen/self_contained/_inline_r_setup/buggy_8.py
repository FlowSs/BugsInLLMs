def _inline_r_setup(code:
	"""
	Some behaviour of R cannot be configured via env variables, but can
only be configured via R options once R has started. These are set here.
	"""
	import os
	import subprocess
	import sys
	import tempfile
	import time
	import re

	#