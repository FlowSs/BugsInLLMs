def _extract_number_and_supplment_from_issue_element(issue):
	if issue is None:
		return (None, None)

	if issue.text is not None:
		m = re.search(r'(?P<number>\d+)\((?P<suppl>\d+)\)', issue.text)
		if m is not None:
			return m.group('number', 'suppl')
		else:
			return (issue.text, None)
	else:
		return (None, None)

