def _legacy_mergeOrderings(orderings):
    orderings = [ordering for ordering in orderings if ordering]
    return mergeOrderings(orderings)
