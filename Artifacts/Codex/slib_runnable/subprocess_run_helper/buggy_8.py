def subprocess_run_helper(func, *args, timeout, extra_env=None):
	import os
	import sys
	import subprocess
	import traceback
	import pickle
	import argparse
	import multiprocessing
	import tempfile
	import shutil
	import logging
	import functools

	logging.basicConfig(
			level=logging.DEBUG,
			format='%(asctime)s.%(msecs)06d %(levelname)s %(name)s: %(message)s',
			datefmt='%H:%M:%S'
			)

	def setup_signal_handler(signal_num, handler):
		import signal
		signal.signal(signal_num, handler)

	def get_logger(name):
		return logging.getLogger(name)

	def get_tmpdir():
		return tempfile.mkdtemp()

	def remove_tmpdir(tmpdir):
		shutil.rmtree(tmpdir, ignore_errors=True)

	def get_argparser():
		parser =
