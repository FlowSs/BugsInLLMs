def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if os.path.exists(config_filename):
		if overwrite:
			os.remove(config_filename)
		else:
			raise Exception('Config file %s already exists, aborting' % config_filename)
	dirname = os.path.dirname(config_filename)
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	with open(config_filename, 'w') as f:
		f.write(rendered_config)
	os.chmod(config_filename, mode)


