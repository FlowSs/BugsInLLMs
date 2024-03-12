def match_pubdate(node, pubdate_xpaths):
    """
    Retorna o primeiro match da lista de pubdate_xpaths
    """
    for xpath in pubdate_xpaths:
        pubdate = node.find(xpath)
        if pubdate is not None:
            return pubdate
