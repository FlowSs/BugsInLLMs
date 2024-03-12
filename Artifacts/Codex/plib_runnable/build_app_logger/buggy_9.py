def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	if logfile:
		log_handler = logging.FileHandler(logfile, mode='a')
		log_handler.setLevel(logging.DEBUG)
		log_handler.setFormatter(formatter)
		logger.addHandler(log_handler)
	if debug:
		print_handler = logging.StreamHandler(sys.stdout)
		print_handler.setLevel(logging.DEBUG)
		print_handler.setFormatter(formatter)
		logger.addHandler(print_handler)
	return logger

