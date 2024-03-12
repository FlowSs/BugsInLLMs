def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if not overwrite and os.path.exists(config_filename):
		logger.error("%s already exists. Not overwriting without --overwrite", config_filename)
		raise FileExistsError(config_filename)

	logger.debug("Writing configuration to %s", config_filename)
	try:
		os.makedirs(os.path.dirname(config_filename), exist_ok=True)
	except OSError as e:
		logger.error("Error creating directory %s: %s", os.path.dirname(config_filename), e)
		sys.exit(1)

	try:
		with open(config_filename, 'w') as config_file:
			config_file.write(rendered_config)
	except OSError as e:
		logger.error("Error writing to %s: %s", config_filename, e)
		sys.exit(1)

	# Change permissions to be safe
	try:
		os.chmod(config_filename, mode)
	
