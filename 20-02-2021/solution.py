#!/usr/bin/env python3

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return (self is not None
                and self.left == self.right == None)

def count_unival_subtrees(root):
    if not root:
        return 0
    if root.is_leaf():
        return 1
    left_count = count_unival_subtrees(root.left)
    right_count = count_unival_subtrees(root.right)
    total = left_count + right_count
    if root.val == root.left.val == root.right.val:
        total += 1
    return total

assert count_unival_subtrees(None) == 0
assert count_unival_subtrees(Node(1)) == 1
assert count_unival_subtrees(Node(0)) == 1
assert count_unival_subtrees(Node(1, Node(1), Node(1))) == 3
assert count_unival_subtrees(Node(1, Node(0), Node(1))) == 2
assert(count_unival_subtrees(Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))))) == 5
