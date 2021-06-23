#!/usr/bin/env python3

class Empty(Exception):
    pass

class MaxStack():
    __empty_msg = 'stack is empty'

    def __init__(self) -> None:
        self.stack = []
        self.max_stack = []
    
    def push(self, element) -> None:
        self.stack.append(element)
        if not self.max_stack or element > self.max_stack[-1]:
            self.max_stack.append(element)
    
    def pop(self) -> object:
        if not self.stack:
            raise Empty(self.__empty_msg)
        top = self.stack.pop()
        if top == self.max_stack[-1]:
            self.max_stack.pop()
        return top
    
    def max(self) -> object:
        if not self.stack:
            raise Empty(self.__empty_msg)
        return self.max_stack[-1]

max_stack = MaxStack()
max_stack.push(1)
assert max_stack.max() == 1
max_stack.push(-3)
assert max_stack.max() == 1
assert max_stack.pop() == -3
assert max_stack.pop() == 1
try:
    max_stack.pop()
except Empty:
    pass
except Exception:
    assert True == False