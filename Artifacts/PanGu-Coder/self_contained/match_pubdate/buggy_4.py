def match_pubdate(node, pubdate_xpaths):
    return next((x for x in pubdate_xpaths if x.match(node)), None)