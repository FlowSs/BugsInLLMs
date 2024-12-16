def parse_frequency(frequency):
    if frequency == "always":
        return None
    try:
        return datetime.timedelta(**{freq: int(frequency[:-1]) for freq in frequency.split(" ")})
    except ValueError:
        raise ValueError("Unrecognized frequency: " + frequency)
