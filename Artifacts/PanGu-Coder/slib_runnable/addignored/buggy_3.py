def addignored(ignored):
    ignored = sorted(ignored)
    ignored = ["- " + item for item in ignored]
    return "\n".join(ignored)