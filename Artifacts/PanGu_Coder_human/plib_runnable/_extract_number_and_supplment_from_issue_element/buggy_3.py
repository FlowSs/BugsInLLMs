def _extract_number_and_supplment_from_issue_element(issue):
    return (
        issue.find("number", recursive=False).text,
        issue.find("sup", recursive=False).text,
    )
