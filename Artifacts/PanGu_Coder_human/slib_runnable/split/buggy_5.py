def split(s, platform='this'):
    if platform == 'this':
        platform = os.name
    if platform == 'posix':
        return s.split('\\')
    elif platform == 'windows':
        return s.split('/')
    else:
        return []
