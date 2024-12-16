def _extract_number_and_supplment_from_issue_element(issue):
	number = None
	supplement = None

	try:
		number = int(issue.find("number").text)
		if number < 1:
			number = None
	except AttributeError:
		pass
	except TypeError:
		pass
	except ValueError:
		pass

	try:
		supplement = int(issue.find("supplement").text)
		if supplement < 1:
			supplement = None
	except AttributeError:
		pass
	except TypeError:
		pass
	except ValueError:
		pass

	return (number, supplement)

