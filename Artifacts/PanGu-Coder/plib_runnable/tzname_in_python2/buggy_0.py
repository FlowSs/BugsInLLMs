def tzname_in_python2(namefunc):
    if sys.version_info < (3, 0):
        return namefunc
    else:
        return namefunc.encode('utf-8')
