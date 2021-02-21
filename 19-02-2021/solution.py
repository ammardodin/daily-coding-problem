#!/usr/bin/env python3
from functools import cache

"""
Choose either a 1-len prefix or a 2-len prefix at each step
This explodes exponentially in the worst case, i.e. something like 11111111
so essentially degrades into a fibonacci sequence-like recursion
"""
def num_decodings(s):
    if not s:
        return 1
    
    choose_single, choose_double = 0, 0

    if 1 <= int(s[:1]) <= 9:
        choose_single = num_decodings(s[1:])
    
    if 10 <= int(s[:2]) <= 26:
        choose_double = num_decodings(s[2:])
    
    return choose_single + choose_double

"""
simply memoize the results to get a linear space + time solution
"""
@cache
def num_decodings_memoized(s):
    if not s:
        return 1
    
    choose_single, choose_double = 0, 0

    if 1 <= int(s[:1]) <= 9:
        choose_single = num_decodings(s[1:])
    
    if 10 <= int(s[:2]) <= 26:
        choose_double = num_decodings(s[2:])
    
    return choose_single + choose_double

"""
bottom up memoization
"""
def num_decodings_bottom_up(s):
    n = len(s)
    if n == 0:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
        if 1 <= int(s[i-1:i]) <= 9:
            dp[i] += dp[i-1]
    return dp[len(s)]

assert num_decodings("12") == 2
assert num_decodings("226") == 3
assert num_decodings("11111") == 8

assert num_decodings_memoized("12") == 2
assert num_decodings_memoized("226") == 3
assert num_decodings_memoized("11111") == 8

assert num_decodings_bottom_up("12") == 2
assert num_decodings_bottom_up("226") == 3
assert num_decodings_bottom_up("11111") == 8
