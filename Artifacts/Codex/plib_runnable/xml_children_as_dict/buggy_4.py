def xml_children_as_dict(node):
	d = {}
	for child in node.children:
		if child.tag not in d:
			d[child.tag] = [child]
		else:
			d[child.tag].append(child)
	return d


