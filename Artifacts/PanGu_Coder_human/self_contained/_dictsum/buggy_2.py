def _dictsum(dicts):
    dic = {}
    for key, value in dicts.items():
        if key in dic:
            dic[key] += value
        else:
            dic[key] = value
    return dic
