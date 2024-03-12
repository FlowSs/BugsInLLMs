def make_find_paths(find_paths):
	"""
	Given a sequence of path fragments or patterns as passed to `--find`, transform all path
fragments into glob patterns. Pass through existing patterns untouched.

For example, given find_paths of:

  ['foo.txt', 'pp:root/somedir']

... transform that into:

  ['sh:**/*foo.txt*/**', 'pp:root/somedir']
	"""
	find_paths = [path for path in find_paths if path]
	return [os.path.join(p, '') for p in find_paths]

