def addignored(ignored):
	git_cmd = "git ls-files -i --exclude-standard"
	output = subprocess.check_output(git_cmd, shell=True).strip().splitlines()
	output = sorted(output)
	return ",".join(output)

