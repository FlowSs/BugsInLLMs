def _extract_number_and_supplment_from_issue_element(issue):
    number = issue.find('.//number').text
    sup = issue.find('.//supplement').text
    return number, sup
