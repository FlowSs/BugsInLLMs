def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a rendered config YAML, write it out to target file.
    But if the file already exists and overwrite is False,
    abort before writing anything.
    If the file does not exist, create it.
    Write to the file otherwise.

    Returns: None
	"""
	if not os.path.exists(config_filename):
		with open(config_filename, 'w') as config_file:
			yaml.dump(rendered_config, config_file, default_flow_style=False)
	elif overwrite or not os.path.isfile(config_filename):
		with open(config_filename, 'w') as config_file:
			yaml.dump(rendered_config, config_file, default_flow_style=False)
	else:
		raise ValueError("Cannot overwrite existing file '%s'" % config_filename)

