#!/usr/bin/env python3

def power_set(in_set):
    if not in_set:
        return [set()]
    items = list(in_set)
    result = []

    size = len(items)
    n = 1 << size
    for i in range(n):
        curr = set()
        for j in range(size):
            if 1 << j & i:
                curr.add(items[j])
        result.append(curr)
    return result

assert power_set({}) == [set()]
assert power_set({1}) == [set(), {1}]
assert power_set({1, 2, 3}) == [set(), {1}, {2}, {1,2}, {3}, {1,3}, {2,3}, {1,2,3}]
