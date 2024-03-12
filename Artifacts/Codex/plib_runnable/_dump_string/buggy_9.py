def _dump_string(obj, dumper=None):
	if dumper is None:
		dumper = _dumper

	return dumper(obj).encode('utf-8')

