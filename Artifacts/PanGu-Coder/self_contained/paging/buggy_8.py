def paging(response, max_results):
    return itertools.islice(response, 0, max_results)
