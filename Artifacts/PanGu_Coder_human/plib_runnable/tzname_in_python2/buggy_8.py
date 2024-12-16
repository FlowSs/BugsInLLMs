def tzname_in_python2(namefunc):
    
    
    def inner(tzname):
        if sys.version_info < (3, 0):
            return namefunc(tzname.encode('utf-8'))
        else:
            return namefunc(tzname)
    return inner
