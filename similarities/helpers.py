def lines(a, b):
    """Return lines in both a and b"""
    a_lines = set(a.splitlines())
    b_lines = set(b.splitlines())

    same = list(a_lines.intersection(b_lines))
    # print(same)

    return same


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
