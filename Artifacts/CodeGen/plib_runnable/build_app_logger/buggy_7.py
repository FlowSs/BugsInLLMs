def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	if debug:
		logFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
	else:
		logFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
	handler = logging.FileHandler(logfile)
	handler.setFormatter(logFormatter)
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	logger.addHandler(handler)
	return logger

