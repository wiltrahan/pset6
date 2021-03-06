from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    a_lines = set(a.splitlines())
    b_lines = set(b.splitlines())

    same = list(a_lines.intersection(b_lines))
    # print(same)

    return same


def sentences(a, b):
    """Return sentences in both a and b"""
    sent_a = set(sent_tokenize(a))
    sent_b = set(sent_tokenize(b))

    both = list(sent_a.intersection(sent_b))
    # print(both)
    return both


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    a_list = set(subbed(a, n))
    b_list = set(subbed(b, n))

    both = list(a_list.intersection(b_list))

    #print(both)
    # TODO
    return both


def subbed(str, n):
    sub = []
    for i in range(len(str) - n + 1):
        sub.append(str[i:i + n])

    return sub