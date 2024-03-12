def paging(response, max_results):
    for page in range(1, max_results + 1):
        for page_number in range(1, page + 1):
            yield response[page_number * max_results:page_number * max_results + max_results]
