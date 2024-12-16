def _inline_r_setup(code: str):
    code = code.replace('{', '').replace('}', '')
    code = code.replace('(', '').replace(')', '')
    code = code.replace(',', '')
    code = code.replace(':', '')
    code = code.replace(',', '')
    code = code.replace(';', '')
    code = code.replace('\'', '')
    code = code.replace('\"', '')
    code = code.replace('\\', '')
    return code