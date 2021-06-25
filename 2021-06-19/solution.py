#!/usr/bin/env python3
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def find(root, caller, value):
    if not root or root == caller:
        return None
    
    if value == root.value:
        return root
    elif value > root.value:
        return find(root.right, value)
    
    return find(root.left, value)

def two_sum_search(root, target):
    if not root:
        return (None, None)

    q = deque([root])
    while q:
        curr = q.popleft()
        complement = find(root, curr, target-curr.value)
        if complement:
            return curr, complement
        q.extendleft([root.left, root.right])
    return None, None

def two_sum_arrify(root, target):

    values = []
    def in_order(root):
        if not root:
            return
        in_order(root.left)
        values.append(root)
        in_order(root.right)
    in_order(root)
    
    left, right = 0, len(values) - 1
    while left < right:
        s = values[left].value + values[right].value
        if s == target:
            return values[left],values[right]
        elif s > target:
            right -= 1
        else:
            left += 1

    return None,None
            