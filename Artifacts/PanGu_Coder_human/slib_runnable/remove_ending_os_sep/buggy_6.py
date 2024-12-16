def remove_ending_os_sep(input_list):
    if input_list is None:
        return []

    if len(input_list) == 0:
        return input_list

    return [input_list[0]] + remove_ending_os_sep(input_list[1:])
