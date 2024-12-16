def addignored(ignored):
	ignored = subprocess.check_output("git ls-files --others --exclude-standard".split(" "))
	ignored = ignored.decode("utf-8")
	ignored = ignored.split("\n")
	ignored = str(ignored)[1:-1]
	ignored = ignored.replace("'", "")
	ignored = ignored.replace(" ", "")
	return ignored


