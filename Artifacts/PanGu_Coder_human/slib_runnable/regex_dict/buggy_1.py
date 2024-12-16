def regex_dict(item):
    for k, v in item.items():
        if k.endswith(".cpp"):
            item[k] = re.compile(v)

    return item
