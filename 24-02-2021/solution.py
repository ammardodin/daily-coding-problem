#!/usr/bin/env python3

"""
We can get to the nth step from either the (n-2)th step or the (n-1)th step.
If we know the number of ways to get to the (n-2)th and (n-1)th steps, their
sum would be the number of ways we can get to the nth step.

The recurrence is given by T(n) = T(n-1) + T(n-2) + O(1)
""" 

# O(2^n) time + O(n) space
def num_ways(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return num_ways(n-1) + num_ways(n-2)

# O(N) time and space
def num_ways_dp(n):
    if n == 0 or n == 1 or n == 2:
        return n
    ways = [0] * (n+1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i-1] + ways[i-2]
    return ways[n]

# O(N) time and constant space
def num_ways_opt(n):
    if n == 0 or n == 1 or n == 2:
        return n
    a, b = 1, 2
    for i in range(3, n + 1):
        a,b = b, a + b
    return b

assert num_ways(0) == 0
assert num_ways(1) == 1
assert num_ways(2) == 2
assert num_ways(3) == 3
assert num_ways(4) == 5
assert num_ways(5) == 8

assert num_ways_dp(0) == 0
assert num_ways_dp(1) == 1
assert num_ways_dp(2) == 2
assert num_ways_dp(3) == 3
assert num_ways_dp(4) == 5
assert num_ways_dp(5) == 8


assert num_ways_opt(0) == 0
assert num_ways_opt(1) == 1
assert num_ways_opt(2) == 2
assert num_ways_opt(3) == 3
assert num_ways_opt(4) == 5
assert num_ways_opt(5) == 8