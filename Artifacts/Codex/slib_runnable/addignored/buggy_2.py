def addignored(ignored):
	
	ignored = os.popen('git ls-files --ignored --exclude-standard').read()
	ignored = ignored.split('\n')
	ignored = filter(lambda x: not x.startswith('#'), ignored)
	ignored = ','.join(ignored)
	return ignored

