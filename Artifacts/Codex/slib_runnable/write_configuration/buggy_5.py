def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	# TODO: This should be a method on the Config class, as it's not really a function
	# but an action on a specific object.
	if config_filename == '-':
		dest_fd = sys.stdout
		dest_fd.write(rendered_config)
		dest_fd.write("\n")
		dest_fd.flush()
	else:
		dest_filename = os.path.expanduser(config_filename)
		if os.path.exists(dest_filename) and not overwrite:
			raise ConfigurationError("%s already exists; not overwriting" % config_filename)
		path = os.path.dirname(dest_filename)
		if path:
			try:
				os.makedirs(path)
			except OSError:
				pass
		dest_fd = os.open(dest_filename, os.O_WRONLY | os.O_CREAT, mode)
		try:
			os.write(dest_
