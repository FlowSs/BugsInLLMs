def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	suppl = None
	for element in issue.find_elements_by_tag_name("td"):
		if element.text:
			if element.text.startswith("N"):
				number = element.text
			elif element.text.startswith("S"):
				suppl = element.text
	return (number, suppl)

