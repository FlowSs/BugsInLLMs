def round_half_to_even(n):
    """

        >>> round_half_to_even(3)
        3
        >>> round_half_to_even(3.2)
        3
        >>> round_half_to_even(3.5)
        4
        >>> round_half_to_even(3.7)
        4
        >>> round_half_to_even(4)
        4
        >>> round_half_to_even(4.2)
        4
        >>> round_half_to_even(4.5)
        4
        >>> round_half_to_even(4.7)
        5

    :param n:
    :return:
    """
    ten_n = 10 * n
    if ten_n == int(ten_n) and ten_n % 10 == 5:
        up = int(n + 0.5)
        down = int(n - 0.5)
        return up if up % 2 == 0 else down
    else:
        return int(round(n))
