def paging(response, max_results):
	# Get total number of objects in response
	total_objects = response.total_objects
	# Get total number of pages in response
	total_pages = response.total_pages
	# Get current page
	current_page = response.current_page
	# Get number of objects in current page
	current_objects = response.current_objects
	# Get number of objects in current page
	current_objects = response.current_objects
	# Compute the number of pages to be returned
	if current_objects <= max_results:
		pages_to_return = total_pages
	else:
		pages_to_return = math.ceil(current_objects / max_results)
	# Return pages
	for page in range(1, pages_to_return + 1):
		# Compute the number of objects to be returned in this page
		if page == pages_to_return:
			objects_to_return = current_objects - (max_results * (page - 1))
		else:
			objects_to_return = max_results
		#
