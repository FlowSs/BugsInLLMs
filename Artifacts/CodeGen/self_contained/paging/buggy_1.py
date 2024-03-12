def paging(response, max_results):
	"""
	Returns WAPI response page by page

Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
Returns:
    Generator object with WAPI response split page by page.
	"""
	current_page = 0
	next_page = 1
	while next_page <= max_results:
		response_page = response[current_page * max_results : (current_page + 1) * max_results]
		yield response_page
		current_page = (current_page + 1) % len(response)
		next_page = (next_page + 1) % len(response)