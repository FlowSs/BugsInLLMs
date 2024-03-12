def _extract_number_and_supplment_from_issue_element(issue):
    return issue.find('.//number').text, issue.find('.//suppl').text
