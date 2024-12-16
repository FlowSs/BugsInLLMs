def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not overwrite:
        return

    if os.path.exists(config_filename):
        if not overwrite and os.path.isfile(config_filename):
            log.error('%s already exists', config_filename)
            return

    with open(config_filename, mode) as config_file:
        config_file.write(rendered_config)
