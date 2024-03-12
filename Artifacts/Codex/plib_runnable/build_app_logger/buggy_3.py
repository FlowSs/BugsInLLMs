def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')

	if debug:
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		ch.setFormatter(formatter)
		logger.addHandler(ch)

	fh = logging.FileHandler(logfile)
	fh.setLevel(logging.DEBUG)
	fh.setFormatter(formatter)
	logger.addHandler(fh)

	return logger

