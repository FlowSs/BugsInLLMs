def addignored(ignored):
    filenames = []
    for item in ignored:
        filenames.append('"' + item + '"')
    filenames.sort()
    return ','.join(filenames)
