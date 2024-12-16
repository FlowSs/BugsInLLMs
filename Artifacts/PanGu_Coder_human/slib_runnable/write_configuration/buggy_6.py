def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not os.path.exists(config_filename) or overwrite:
        with open(config_filename, mode) as f:
            f.write(rendered_config)
    else:
        raise ConfigurationException("Configuration file already exists")
