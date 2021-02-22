#!/usr/bin/env python3

"""
Let sum be an array such that sum[i] is max non-adjacent sum of a[0]...a[i]
sum[0] = arr[0]
sum[1] = max(sum[0], arr[1])
sum[2] = max(sum[0] + arr[2], sum[1])
...
sum[i] = max(sum[i-2] + arr[i], sum[i-1])
"""
def max_non_adjacent_sum(arr, i):
    if not arr:
        return 0
    elif i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    return max(max_non_adjacent_sum(arr, i - 2) + arr[i], max_non_adjacent_sum(arr, i - 1))

def max_non_adjacent_sum_dp(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n <= 2:
        return max(arr)
    s = [0] * len(arr)
    s[0] = arr[0]
    s[1] = max(s[0], arr[1])
    for i in range(2, len(arr)):
        s[i] = max(s[i-2] + arr[i], s[i-1])
    return s[-1]

assert max_non_adjacent_sum([], 0) == 0
assert max_non_adjacent_sum([1], 0) == 1
assert max_non_adjacent_sum([1, 2], 1) == 2
assert max_non_adjacent_sum([-5, -6, -7], 2) == -5
assert max_non_adjacent_sum([2, 4, 6, 2, 5], 4) == 13
assert max_non_adjacent_sum([5,1,1,5], 3) == 10

assert max_non_adjacent_sum_dp([]) == 0
assert max_non_adjacent_sum_dp([1]) == 1
assert max_non_adjacent_sum_dp([1, 2]) == 2
assert max_non_adjacent_sum_dp([-5, -6, -7]) == -5
assert max_non_adjacent_sum_dp([2, 4, 6, 2, 5]) == 13
assert max_non_adjacent_sum_dp([5,1,1,5]) == 10
