def addignored(ignored):
	git_command = "git ls-files --others --exclude-standard"
	try:
		output = subprocess.check_output(git_command.split()).strip().decode()
		if len(output) > 0:
			return ignored + ", " + output
	except:
		pass

	return ignored


