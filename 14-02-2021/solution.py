#!/usr/bin/env python3

# linear space (result list) and quadratic time
def solution(nums):
    res = [0] * len(nums)
    for i in range(len(nums)):
        curr = 1
        for j in range(len(nums)):
            if i != j:
                curr *= nums[j]
        res[i] = curr
    return res

# linear space (result list) and time
def solution2(nums):
    numZeros = 0
    res = [0] * len(nums)
    total = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            numZeros += 1
            continue
        total *= nums[i]
    if numZeros > 1:
        return res
    for i in range(len(nums)):
        if numZeros == 1 and nums[i] == 0:
            res[i] = total
        elif numZeros == 0:
            res[i] = total // nums[i]
    return res

# without division
# linear space and time
# needs 2N auxiliary space aside from result list
def solution3(nums):
    n = len(nums)
    res = [0] * n
    right = list(nums)
    left = list(nums)

    for i in range(1, n):
        left[i] *= left[i-1]
    
    for i in range(n-2, 0, -1):
        right[i] *= right[i+1]
    
    for i in range(n):
        l = left[i-1] if i-1 > -1 else 1
        r = right[i+1] if i+1 < n else 1
        res[i] = l * r
    
    return res

# without division
# linear space and time
# needs 1N auxiliary space aside from 
def solution4(nums):
    n = len(nums)
    res = [0] * n
    right = list(nums)
    
    for i in range(n-2, 0, -1):
        right[i] *= right[i+1]
    
    leftRunningProduct = 1
    for i in range(n):
        r = right[i+1] if i+1 < n else 1
        res[i] = leftRunningProduct * r
        leftRunningProduct *= nums[i]
    
    return res


assert solution([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solution([1, 2, 3, 0]) == [0, 0, 0, 6]
assert solution([1, 0, 3, 0]) == [0, 0, 0, 0]
assert solution([3, 2, 1]) == [2, 3, 6]

assert solution2([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solution2([1, 2, 3, 0]) == [0, 0, 0, 6]
assert solution2([1, 0, 3, 0]) == [0, 0, 0, 0]
assert solution2([3, 2, 1]) == [2, 3, 6]

assert solution3([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solution3([1, 2, 3, 0]) == [0, 0, 0, 6]
assert solution3([1, 0, 3, 0]) == [0, 0, 0, 0]
assert solution3([3, 2, 1]) == [2, 3, 6]

assert solution4([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solution4([1, 2, 3, 0]) == [0, 0, 0, 6]
assert solution4([1, 0, 3, 0]) == [0, 0, 0, 0]
assert solution4([3, 2, 1]) == [2, 3, 6]
