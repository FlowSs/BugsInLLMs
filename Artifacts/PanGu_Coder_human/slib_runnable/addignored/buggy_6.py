def addignored(ignored):

    if len(ignored) == 0:
        return ""

    ret = ""
    for i in range(0, len(ignored)):
        if ignored[i] in IGNORED:
            ret += ignored[i] + ","
        else:
            ret += ignored[i]
    return ret