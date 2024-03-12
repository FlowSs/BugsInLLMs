def paging(response, max_results):
	"""
	Returns WAPI response page by page

Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
Returns:
    Generator object with WAPI response split page by page.
	"""
	paging_params = {
		"page": 1,
		"per_page": max_results
	}
	response = response.json()
	while True:
		for item in response["items"]:
			yield item
		if "next" in response:
			paging_params["page"] += 1
			response = response["next"]
		else:
			break

