def _legacy_mergeOrderings(orderings):
	# note that we don't need to worry about one ordering being a
	# subsequence of another, since these two cases are equivalent:
	#
	# ['a', 'b', 'c'] + ['b', 'c'] == ['a', 'b', 'c']
	# ['a', 'b', 'c'] + ['b', 'c', 'd'] == ['a', 'b', 'c', 'd']
	#
	# so we can sort the orderings by length, which makes the code
	# below simpler.
	orderings.sort(key=len)
	#
	# now we merge the orderings in order from longest to shortest.
	#
	# this will ensure that we preserve the ordering of all objects
	# that appear in the longer orderings.
	#
	# it will also ensure that we don't introduce any duplicates,
	# since the longest ordering will always contain the entire
	# suffix that is shared between any two orderings.
	#
	# it also makes the code below simpler, since we can always
	# assume that the orderings we're merging are disj
