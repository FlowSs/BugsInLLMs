def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = issue.find('./issue/number').text
	number = number.strip()

	if number.startswith('#