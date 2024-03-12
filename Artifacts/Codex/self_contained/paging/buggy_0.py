def paging(response, max_results):
	while True:
		for r in response:
			yield r
		if '_next_id' not in response._meta:
			break
		next_id = response._meta['_next_id']
		response = infoblox.get_object(object_type, return_fields=return_fields, max_results=max_results, _max_results=max_results, _return_fields=return_fields, _paging_identifier=next_id)

