#!/usr/bin/env python3

"""
Brute force O(N^3) time and O(N) space
"""
from collections import defaultdict


def substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(n):
            yield s[i:j]

def num_unique(s):
    return len(set(s))

def longest_with_k_distinct_brute(s, k):
    longest = 0
    for substr in substrings(s):
        if num_unique(substr) == k:
            longest = max(longest, len(substr))
    return longest

assert longest_with_k_distinct_brute("abcba", 2) == 3
assert longest_with_k_distinct_brute("", 2) == 0
assert longest_with_k_distinct_brute("aaaaaaaa", 2) == 0
assert longest_with_k_distinct_brute("abcbbbbbbbca", 2) == 10

"""
Sliding window O(N) space and time
"""
def longest_with_k_distinct(s, k):
    if not s:
        return 0
    longest = 0
    start = end = 0

    window = set()
    freq = defaultdict(int)
    left = right = 0

    while right < len(s):
        window.add(s[right])
        freq[s[right]] += 1

        while len(window) > k:
            freq[s[left]] -= 1
            if freq[s[left]] <= 0:
                window.remove(s[left])
            left = left + 1
        
        if right - left > end - start:
            start = left
            end = right
        
        right += 1
    
    return end - start + 1

assert longest_with_k_distinct("abcba", 2) == 3
assert longest_with_k_distinct("", 2) == 0
assert longest_with_k_distinct("abcbbbbbbbca", 2) == 10