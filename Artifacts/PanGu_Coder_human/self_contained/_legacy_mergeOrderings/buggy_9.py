def _legacy_mergeOrderings(orderings):
    # FIXME: this is very hacky.
    return sorted(set(itertools.chain.from_iterable(orderings)))
