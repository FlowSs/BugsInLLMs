def addignored(ignored):
    ignored = ignored.split(',')
    ignored.sort()
    return ','.join(ignored)