#!/usr/bin/env python3

class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
    def right_most_child_with_parent(self):
        parent, curr = None, self
        while curr.right:
            parent = curr
            curr = curr.right
        return parent, curr


def second_largest(root):
    if not root:
        return None
    prev, curr = root.right_most_child_with_parent()
    if curr.left:
        _, curr = curr.left.right_most_child_with_parent()
        return curr.value
    return prev.value if prev else prev
"""
         7
        /
       4
      / \
     3   5 
"""
tree = Node(7, Node(4, Node(3), Node(5)))
assert second_largest(tree) == 5

"""
       5
      /  \
     4    7
         / \
        6  9
          /
         8
"""
tree = Node(5, Node(4), Node(7, Node(6), Node(9, Node(8))))
assert second_largest(tree) == 8

"""
    5
"""
tree = Node(5)
assert second_largest(tree) == None

"""
    5
     \
      7
       \
        10
       /
      9
     /
    8 
"""
tree = Node(5, right=Node(7, right=Node(10, left=Node(9, left=Node(8)))))
assert second_largest(tree) == 9