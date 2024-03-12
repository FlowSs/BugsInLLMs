def oneline(script, seperator=" && "):
	"""
	converts a script to one line command.
THis is useful to run a single ssh command and pass a one line script.

:param script:
:return:
	"""
	script = script.replace("\n", ";").replace("\t", "").replace("\r", "")
	return script.replace("'", "")

