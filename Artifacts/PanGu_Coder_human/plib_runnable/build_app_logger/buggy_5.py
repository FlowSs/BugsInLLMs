def build_app_logger(name='app', logfile='app.log', debug=True):
    logger = logging.getLogger(name)
    handler = logging.FileHandler(logfile)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    if debug:
        logger.setLevel(logging.DEBUG)
    return logger
