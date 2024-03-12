def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not os.path.exists(config_filename):
        os.makedirs(os.path.dirname(config_filename))
    with open(config_filename, mode) as f:
        f.write(rendered_config)
    if overwrite:
        os.remove(config_filename)