#!/usr/bin/env python3

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def left(a, b):
        return a
    return pair(left)

def cdr(pair):
    def right(a, b):
        return b
    return pair(right)

assert car(cons(1,2)) == 1
assert cdr(cons(5, 2)) == 2
