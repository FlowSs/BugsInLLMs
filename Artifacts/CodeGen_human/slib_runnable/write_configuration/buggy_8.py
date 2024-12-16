def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a rendered config YAML, write it out to target file.
    But if the file already exists and overwrite is False,
    abort before writing anything.
    If the file does not exist, create it.
    Write to the file otherwise.

    Returns: None
	"""
	if os.path.exists(config_filename) and not overwrite:
		raise ValueError('Config file %s already exists' % config_filename)

	with open(config_filename, 'w') as f:
		f.write(rendered_config)

	if not os.path.exists(config_filename):
		raise ValueError('Config file %s does not exist' % config_filename)
	
	if mode!= 0o600:
		raise ValueError('Only supporting mode=0o600, not %d' % mode)

	f.write('\n')
	f.write('#