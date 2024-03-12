def remove_ending_os_sep(input_list):
    if len(input_list) == 0:
        return input_list

    if len(input_list[-1]) == 1 and input_list[-1][0] == os.sep:
        del input_list[-1]

    return input_list
