def match_pubdate(node, pubdate_xpaths):
    
    
    return node.xpath(pubdate_xpaths[0]).extract_first()