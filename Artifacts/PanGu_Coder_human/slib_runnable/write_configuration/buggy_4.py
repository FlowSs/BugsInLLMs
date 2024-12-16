def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not os.path.exists(config_filename):
        if not overwrite:
            click.echo('Configuration file "{}" does not exist. Skipping.'.format(config_filename))
            return
        else:
            click.echo('Creating new configuration file "{}"'.format(config_filename))
            os.makedirs(os.path.dirname(config_filename), mode=mode)
    with open(config_filename, 'w') as f:
        f.write(rendered_config)
