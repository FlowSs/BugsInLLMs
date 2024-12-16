def tzname_in_python2(namefunc):
    def tzname(self, dt):
        name = namefunc(self, dt)
        return name.encode('utf-8')
    return tzname