def tzname_in_python2(namefunc):
    def _tzname(self):
        return namefunc(self).encode('utf-8')
    _tzname.__name__ = namefunc.__name__
    return _tzname
