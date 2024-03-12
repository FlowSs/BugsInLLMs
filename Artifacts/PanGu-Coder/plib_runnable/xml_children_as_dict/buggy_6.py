def xml_children_as_dict(node):
    return {n.tag: n.text for n in node.getchildren()}
