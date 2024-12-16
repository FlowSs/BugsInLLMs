def _extract_number_and_supplment_from_issue_element(issue):
	number = None
	supplement = None
	if 'issue' not in issue:
		return number, supplement
	for child in issue.issue.children:
		if child.tag == 'issue':
			number = child.text
		elif child.tag == 'supplement':
			supplement = child.text
	return number, supplement


