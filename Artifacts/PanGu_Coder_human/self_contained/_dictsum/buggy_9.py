def _dictsum(dicts):
    new_dict = {}
    for dict_key, dict_value in dicts.items():
        new_dict[dict_key] = dict_value + new_dict.get(dict_key, 0)
    return new_dict
