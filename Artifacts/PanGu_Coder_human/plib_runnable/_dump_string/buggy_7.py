def _dump_string(obj, dumper=None):
    return dumper.represent_scalar('tag:yaml.org,2002:str', str(obj))
