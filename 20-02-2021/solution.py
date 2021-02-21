#!/usr/bin/env python3

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return (self is not None
                and self.left == self.right == None)
    
    def equal_to_left_and_right(self):
        if not self.left and not self.right:
            return True
        if self.left and self.right and self.val == self.right.val == self.left.val:
            return True
        if self.left:
            return self.val == self.left.val
        if self.right:
            return self.val == self.right.val

def count_unival_subtrees(root):
    def solve(root):
        if not root:
            return 0, True
        left_count, left_is_unival = solve(root.left)
        right_count, right_is_unival = solve(root.right)
        root_is_unival = left_is_unival and right_is_unival and root.equal_to_left_and_right()
        total = left_count + right_count
        if root_is_unival:
            return total + 1, True
        return total, False
    num_subtrees, _ = solve(root)
    return num_subtrees


assert count_unival_subtrees(None) == 0
assert count_unival_subtrees(Node(1)) == 1
assert count_unival_subtrees(Node(0)) == 1
assert count_unival_subtrees(Node(1, Node(1), Node(1))) == 3
assert count_unival_subtrees(Node(1, Node(0), Node(1))) == 2
assert count_unival_subtrees(Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))) == 5
assert count_unival_subtrees(Node(5, Node(1, Node(5), Node(5)), Node(5, None, Node(5)))) == 4
assert count_unival_subtrees(Node(1, Node(3, Node(4), Node(5)), Node(2, None, Node(6)))) == 3