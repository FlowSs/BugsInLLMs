def _reset_logging(cls):
	"""
	Reset
	"""
	cls.logger = logging.getLogger(cls.name)
	cls.logger.setLevel(logging.INFO)
	cls.logger.propagate = False

class Logger(object):
	"""
	A logger that can be used to print to the console
	"""

	def __init__(self, logger_name, log_file=None):
		"""
		Constructor

		Parameters:
			logger_name: name of the logger
			log_file: file where the logger should be saved
		"""

		self.logger = logging.getLogger(logger_name)
		self.logger.setLevel(logging.DEBUG)
		self.logger.propagate = False

		if log_file is not None:
			fh = logging.FileHandler(log_file)
			fh.setLevel(logging.DEBUG)
			formatter = logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s')
			fh.setFormatter(formatter)
			self.logger.addHandler(fh)

	def __del__(self):
		"""
		Destructor

		"""
		self.logger.removeHandler(self.logger.handlers[0])
import os
import sys
import traceback

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from flask_cors import CORS

from utils import (
    get_page_url,
    write_log,
    get_all_jobs_from_page,
    get_job_from_url,
    get_jobs_from_url,
)

app = Flask(__name__)
CORS(app)

