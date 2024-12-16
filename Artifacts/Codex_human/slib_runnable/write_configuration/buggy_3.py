def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if not overwrite and os.path.exists(config_filename):
		raise FileExistsError("File already exists: {}".format(config_filename))
	with open(config_filename, 'w') as f:
		f.write(rendered_config)
	os.chmod(config_filename, mode)
