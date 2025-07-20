def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    prev_item = next(t)

    try:
        while True:
            cur_item = next(t)
            yield cur_item - prev_item
            prev_item = cur_item
    except StopIteration:
        pass
