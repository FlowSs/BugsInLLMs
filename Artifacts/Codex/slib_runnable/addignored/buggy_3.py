def addignored(ignored):
	ignored = subprocess.check_output(['git','ls-files','-o','-i','-z']).split('\0')
	ignored = [filename for filename in ignored if filename.startswith('.')]
	return ','.join(ignored)

