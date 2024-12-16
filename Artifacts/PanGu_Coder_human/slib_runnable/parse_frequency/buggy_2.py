def parse_frequency(frequency):
    if frequency is None:
        return None
    if frequency.lower() in ("always", "never"):
        return None
    try:
        return timedelta(**{_unit_map[frequency.lower()]: None})
    except KeyError:
        raise ValueError("Invalid frequency: {}".format(frequency))
