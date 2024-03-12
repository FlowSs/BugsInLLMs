def addignored(ignored):
	ignore = subprocess.Popen(['git', 'ls-files', '-o', '--exclude-standard'], stdout=subprocess.PIPE).communicate()[0]
	ignore = ignore.splitlines()
	ignore = sorted(ignore)
	for i in ignore:
		ignored.append('"' + i + '"')
	ignored = ','.join(ignored)
	return ignored

