def match_pubdate(node, pubdate_xpaths):
    for pubdate_xpath in pubdate_xpaths:
        pubdate_el = node.xpath(pubdate_xpath)
        if pubdate_el:
            return pubdate_el[0].text
