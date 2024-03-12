def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Extract the possible values of number and suppl from the contents of issue.
	"""
	number = None
	supp = None
	if issue.contents:
		contents = issue.contents
		if len(contents) > 0:
			for num in contents:
				if num.name.startswith('#