def match_pubdate(node, pubdate_xpaths):
    for pubdate_xpath in pubdate_xpaths:
        pubdate = node.xpath(pubdate_xpath)[0].text
        if pubdate:
            return pubdate
