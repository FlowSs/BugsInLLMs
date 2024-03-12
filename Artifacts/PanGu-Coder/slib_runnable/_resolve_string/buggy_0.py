def _resolve_string(matcher):
    try:
        return os.environ[matcher.name]
    except KeyError:
        if matcher.default is None:
            raise Error('Missing variable %s' % matcher.name)
        return matcher.default