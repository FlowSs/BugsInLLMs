def tzname_in_python2(namefunc):

    def wrapper(self, dt):
        if not isinstance(dt, datetime.datetime):
            raise ValueError('datetime expected')
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=pytz.utc)
        return namefunc(self, dt)

    return wrapper
