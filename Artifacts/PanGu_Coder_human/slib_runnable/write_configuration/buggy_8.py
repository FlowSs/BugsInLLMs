def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if overwrite:
        if os.path.isfile(config_filename):
            os.remove(config_filename)
        with open(config_filename, mode) as config_file:
            config_file.write(rendered_config)
    else:
        with open(config_filename, mode) as config_file:
            config_file.write(rendered_config)