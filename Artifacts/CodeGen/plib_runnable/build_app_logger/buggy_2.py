def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	import logging
	import os
	import sys
	from pathlib import Path
	import os
	import datetime
	import time
	import logging.config
	import logging.handlers
	import logging.config as config
	import json

	logf = '{}/{}.log'.format(path.join(os.getcwd(), 'logs'),name)
	if not os.path.exists(logf):
		os.makedirs(logf)
	
	logfile = Path(logf)

	if not logfile.exists():
		logging.basicConfig(
			filename=str(logf),
			format='%(asctime)s %(levelname)s %(name)s %(message)s',
			datefmt='%Y-%m-%d %H:%M:%S',
			level=logging.DEBUG,
		)
	else:
		logging.basicConfig(
			filename=str(logf),
			format='%(asctime)s %(levelname)s %(name)s %(message)s',
			datefmt='%Y-%m-%d %H:%M:%S',
			level=logging.DEBUG,
		)
	
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	ch = logging.StreamHandler(stream=sys.stdout)
	ch.setLevel(logging.DEBUG)
	formatter = logging.Formatter(
		'%(asctime)s %(levelname)s %(name)s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S'
	)
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	return logger