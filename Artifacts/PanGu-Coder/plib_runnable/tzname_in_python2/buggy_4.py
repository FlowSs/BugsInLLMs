def tzname_in_python2(namefunc):
    def inner(self):
        return namefunc(self).encode("utf-8")
    return inner
