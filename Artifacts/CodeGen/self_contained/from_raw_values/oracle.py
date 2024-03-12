    @classmethod
    def from_raw_values(cls, values):
        """Create a Bookmarks object from a list of raw bookmark string values.

        You should not need to use this method unless you want to deserialize
        bookmarks.

        :param values: ASCII string values (raw bookmarks)
        :type values: Iterable[str]
        """
        obj = cls()
        bookmarks = []
        for value in values:
            if not isinstance(value, str):
                raise TypeError("Raw bookmark values must be str. "
                                "Found {}".format(type(value)))
            try:
                value.encode("ascii")
            except UnicodeEncodeError as e:
                raise ValueError(f"The value {value} is not ASCII") from e
            bookmarks.append(value)
        obj._raw_values = frozenset(bookmarks)
        return obj
