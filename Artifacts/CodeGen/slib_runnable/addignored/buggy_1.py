def addignored(ignored):
	"""
	Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
	"""
	try:
		output = subprocess.check_output(["git", "status", "-s", "--porcelain", "--porcelain-stdin"], universal_newlines=True)
	except subprocess.CalledProcessError as e:
		raise Exception(e.output)
	except IOError:
		raise Exception("Unable to read file status output.")

	ignored = [i.strip() for i in output.splitlines() if i.strip()]

	return ",".join(ignored)

