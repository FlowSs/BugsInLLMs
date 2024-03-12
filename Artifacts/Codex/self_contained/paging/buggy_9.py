def paging(response, max_results):
	page = []
	for item in response:
		page.append(item)
		if len(page) == max_results:
			yield page
			page = []
	yield page


