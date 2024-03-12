def split(s, platform='this'):
	# print(s)
	if platform == 'this':
		platform = int(os.name == 'posix')
	re_quoted = r'''(?<!\\)(?:\\\\)*"(?:[^"\\]|\\.)*"'''
	re_unquoted = r"""[^\s"']+"""
	re_pattern = re.compile(r'\s*(%s|%s)' % (re_quoted, re_unquoted), re.S)
	# print(s)
	tokens = re.findall(re_pattern, s)
	# print(tokens)
	if platform:
		tokens = [re.sub(r'\\(.)', r'\1', token) for token in tokens]
	else:
		tokens = [re.sub(r'"((?:[^"\\]|\\.)*)"', r'\1', token) for token in tokens]
	return tokens


