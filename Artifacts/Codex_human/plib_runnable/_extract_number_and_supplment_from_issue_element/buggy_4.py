def _extract_number_and_supplment_from_issue_element(issue):
	# We don't know the type of the number and supplement elements, so we have to
	# check for all the possibilities
	number_elements = issue.findall('{http://prismstandard.org/namespaces/basic/2.0/}number')
	if len(number_elements) == 0:
		number_elements = issue.findall('{http://prismstandard.org/namespaces/basic/2.0/}number[@type="issue"]')
	if len(number_elements) == 0:
		number_elements = issue.findall('{http://prismstandard.org/namespaces/basic/2.0/}number[@type="issueNumber"]')
	if len(number_elements) == 0:
		number_elements = issue.findall('{http://prismstandard.org/namespaces/basic/2.0/}number[@type="issueNumberStart"]')
	if len(number_elements) == 0:
		number_elements = issue.findall('{http://prismstandard.org/
