def _legacy_mergeOrderings(orderings):
	orderings = list(orderings)
	#print '_mergeOrderings: %s' % orderings
	ordering = orderings.pop()
	while orderings:
		other = orderings.pop()
		#print '  other: %s' % other
		for n, item in enumerate(ordering):
			#print '   %s %s' % (n, item)
			if item in other:
				suffix = ordering[n:]
				other_suffix = other[other.index(item):]
				if suffix != other_suffix:
					ordering = ordering[:n] + other_suffix
				break
	return ordering

