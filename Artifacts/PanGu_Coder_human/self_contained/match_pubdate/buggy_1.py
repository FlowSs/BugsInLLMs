def match_pubdate(node, pubdate_xpaths):
    for pubdate_xpath in pubdate_xpaths:
        pubdate = node.xpath(pubdate_xpath)
        if pubdate:
            return pubdate[0]
