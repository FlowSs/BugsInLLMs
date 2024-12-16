def paging(response, max_results):
	# Extract the total number of objects returned
	total_objects = response.total_objects
	# Extract the number of objects returned in the current page
	current_objects = len(response)
	# Calculate the number of pages needed to display all objects
	pages = total_objects // max_results
	# Calculate the number of objects in the last page
	remaining_objects = total_objects % max_results

	# If the number of objects returned in the current page is
	# less than the max_results, there is no need to page
	if current_objects < max_results:
		yield response
	else:
		# Generate a list of page numbers
		pages_list = range(pages + 1)
		# Loop through the pages
		for page in pages_list:
			# If it's the last page and there is a remainder
			# return the remaining number of objects
			if page == pages and remaining_objects > 0:
				max_results = remaining_objects

			# If the number of objects in the current page is
