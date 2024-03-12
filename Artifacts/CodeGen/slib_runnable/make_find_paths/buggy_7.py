def make_find_paths(find_paths):
	"""
	Given a sequence of path fragments or patterns as passed to `--find`, transform all path
fragments into glob patterns. Pass through existing patterns untouched.

For example, given find_paths of:

  ['foo.txt', 'pp:root/somedir']

... transform that into:

  ['sh:**/*foo.txt*/**', 'pp:root/somedir']
	"""
	if not find_paths:
		return find_paths
	
	def _transform(path):
		if not path.endswith('/'):
			path += '/'
		
		if path[-1] == '/':
			return path[:-1]
		
		return path
	
	return [_transform(p) for p in find_paths]

