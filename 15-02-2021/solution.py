#!/usr/bin/env python3

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    sentinel = "null"
    delimiter = " "
    values = []

    def encode(root):
        if not root:
            values.append(sentinel)
            return
        values.append(root.val)
        encode(root.left)
        encode(root.right)
    
    encode(root)

    return delimiter.join(values)

def deserialize(serialized):
    sentinel = "null"
    delimiter = " "
    values = iter(serialized.split(delimiter))

    def decode(values):
        val = next(values)
        if val == sentinel:
            return None
        root = Node(val)
        root.left = decode(values)
        root.right = decode(values)
        return root
    
    return decode(values)

node = Node('root', Node('left', Node('left.left')), Node('right', Node("foo"), Node("bar")))

serialized = serialize(node)
deserialized = deserialize(serialized)
assert serialized == serialize(deserialized)