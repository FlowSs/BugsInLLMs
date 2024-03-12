def _extract_number_and_supplment_from_issue_element(issue):
	issue_text = issue.text or "".join([x.text or "" for x in issue.contents])
	# get the number
	number = re.search("\d+", issue_text)
	if number:
		number = number.group(0)
	else:
		number = ""

	# get the suppl
	suppl = re.search("suppl\s*([IVXLC]+|\d+)", issue_text, re.IGNORECASE)
	if suppl:
		suppl = suppl.group(1)
	else:
		suppl = ""
	return (number, suppl)


