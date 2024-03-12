def paging(response, max_results):
    """Returns WAPI response page by page

    Args:
        response (list): WAPI response.
        max_results (int): Maximum number of objects to be returned in one page.
    Returns:
        Generator object with WAPI response split page by page.
    """
    i = 0
    while i < len(response):
        yield response[i:i + max_results]
        i = i + max_results
