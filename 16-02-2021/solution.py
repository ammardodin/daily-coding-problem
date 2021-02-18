#!/usr/bin/env python3

# The missing value is always in range 1...len(nums)+1
# linear space and time
def find_first_missing(nums):
    seen = [False] * len(nums)

    for n in nums:
        if n >= 1 and n <= len(nums):
            seen[n-1] = True
    
    for i in range(len(nums)):
        if not seen[i]:
            return i + 1
    
    return len(nums) + 1


def find_first_missing_opt(nums):
    # get rid of negatives and values outside the expected range for the missing value
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = len(nums) + 1
    
    # use the array itself as a hash for the seen numbers
    for n in nums:
        n = abs(n)
        if n <= len(nums) and nums[n-1] > 0:
            nums[n-1] *= -1
    
    # loop through range 1...len(nums) and see if we've seen all of it
    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1
    
    # if we've seen all of 1...len(nums), that means len(nums) + 1 is next missing value
    return len(nums) + 1

assert find_first_missing([1,2,0]) == 3
assert find_first_missing([3,4,-1,1]) == 2
assert find_first_missing([7,8,9,11,12]) == 1
 
assert find_first_missing_opt([1,2,0]) == 3
assert find_first_missing_opt([3,4,-1,1]) == 2
assert find_first_missing_opt([7,8,9,11,12]) == 1