import yaml
def _dump_string(obj, dumper=None):
    """Dump to a py2-unicode or py3-string"""
    if PY3:
        return yaml.dump(obj, Dumper=dumper)
    else:
        return yaml.dump(obj, Dumper=dumper, encoding=None)
