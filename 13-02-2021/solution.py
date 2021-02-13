#! /usr/bin/env python3

def any_two_sum_to_k(nums, k):
    seen = set()
    for n in nums:
        if k - n in seen:
            return True
        seen.add(n)
    return False

assert any_two_sum_to_k([], 1) is False
assert any_two_sum_to_k([-1, -2], -3) is True
assert any_two_sum_to_k([1, 2], 3) is True
assert any_two_sum_to_k([1, -1, 0], 0) is True
assert any_two_sum_to_k([1, 1], 3) is False
