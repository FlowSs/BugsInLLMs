def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a target config filename and rendered config YAML, write it out to file. Create any
containing directories as needed. But if the file already exists and overwrite is False,
abort before writing anything.
	"""
	if not overwrite:
		if os.path.exists(config_filename):
			if not os.utime(config_filename, None):
				return False
		else:
			return False
	
	def _write_to_file(config_file):
		try:
			with open(config_file, 'w') as f:
				yaml.dump(rendered_config, f)
		except IOError:
			return False
		return True
	
	def _generate_config_dir_name(config_file):
		return os.path.join('configs', '{}.{}'.format(os.path.basename(config_file), mode))
	
	if not os.path.exists('configs'):
		os.makedirs('configs')
	
	if not os.path.exists(config_filename):
		if not os.path.exists(config_filename + '.{}'.format(mode)):
			with open(config_filename + '.{}'.format(mode), 'w') as f:
				yaml.dump(rendered_config, f)
	
	elif not os.path.exists(config_filename + '.{}'.format(mode)):
		if not os.path.exists(config_filename):
			with open(config_filename, 'w') as f:
				yaml.dump(rendered_config, f)
	
	else:
		if not _write_to_file(config_filename):
			if not _generate_config_dir_name(config_filename):
				raise Exception('Could not create config directory: {}'.format(config_filename))
			
			with open(config_filename, 'w') as f:
				yaml.dump(rendered_config, f)
	
	return True
	
