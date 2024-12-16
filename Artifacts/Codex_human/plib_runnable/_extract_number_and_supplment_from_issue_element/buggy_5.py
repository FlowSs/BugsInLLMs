def _extract_number_and_supplment_from_issue_element(issue):
	number = None
	supplement = None

	if issue is not None:
		if issue.text is not None:
			number = issue.text

		supplement_el = issue.find(".//supplement")
		if supplement_el is not None:
			if supplement_el.text is not None:
				supplement = supplement_el.text

	return number, supplement


