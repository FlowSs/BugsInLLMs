def tzname_in_python2(namefunc):
    """Change unicode output into bytestrings in Python 2

    tzname() API changed in Python 3. It used to return bytes, but was changed
    to unicode strings
    """
    if PY2:
        @wraps(namefunc)
        def adjust_encoding(*args, **kwargs):
            name = namefunc(*args, **kwargs)
            if name is not None:
                name = name.encode()

            return name

        return adjust_encoding
    else:
        return namefunc
