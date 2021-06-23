#!/usr/bin/env python3

from collections import OrderedDict

def make_palindrome(candidate):
    freq = OrderedDict()
    for c in candidate:
        freq[c] = freq.get(c, 0) + 1
    num_odd = 0
    odd_char = ''
    for c, f in freq.items():
        if f & 1:
            num_odd = num_odd + 1
            odd_char = c
    if num_odd > 1:
        return ""
    
    left = []
    right = []
    for c, f in freq.items():
        half = f // 2
        left = left + [c] * half
        right = [c] * half + right
    
    if num_odd:
        return "".join(left + [odd_char] + right)
    
    return "".join(left + right)

assert make_palindrome("") == ""
assert make_palindrome("a") == "a"
assert make_palindrome("aab") == "aba"
assert make_palindrome("aaa") == "aaa"
assert(make_palindrome("bbaa")) == "baab"
assert(make_palindrome("aaaabbc")) == "aabcbaa"
assert(make_palindrome("bab")) == "bab"
