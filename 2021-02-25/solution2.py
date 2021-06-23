#!/usr/bin/env python3

# O(N) time and constant space
def max_consecutive_ones_k(arr, k):
    longest = left = right = count_zeros = 0
    while right < len(arr):
        if arr[right] == 0:
            count_zeros += 1
        while count_zeros > k:
            if arr[left] == 0:
                count_zeros -= 1
            left += 1
        longest = max(longest, right - left + 1)
        right += 1
    return longest

assert max_consecutive_ones_k([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
assert max_consecutive_ones_k([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
