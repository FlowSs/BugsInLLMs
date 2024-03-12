def is_fill_request_el(obj):
    return (
        is_fill(obj) and
        is_request(obj)
    )
