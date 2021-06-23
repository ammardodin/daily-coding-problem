#!/usr/bin/env python3
from collections import Counter

def encode(s):
    if not s:
        return ""
    res = [[1, s[0]]]
    j = 0
    curr = s[0]
    for i in range(1, len(s)):
        if s[i] == curr:
            res[j][0] += 1
        else:
            j += 1
            curr = s[i]
            res.append([1, s[i]])
    return "".join(["{}{}".format(e[0], e[1]) for e in res])


def decode(s):
    if not s:
        return ""
    res =  []
    for i in range(0, len(s), 2):
        count, character = int(s[i]), s[i+1]
        res.extend([character] * count)
    return "".join(res)

assert encode("") == ""
assert decode("") == ""
assert encode("A") == "1A"
assert decode("1A") == "A"
assert encode("AAAAAAAB") == "7A1B"
assert decode("7A1B") == "AAAAAAAB"
assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"
