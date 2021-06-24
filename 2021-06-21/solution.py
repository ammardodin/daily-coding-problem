#!/usr/bin/env python3


class ListNode:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

def serialize_list(head):
    itr = head
    digits = []
    while itr:
        digits.append(itr.value)
        itr = itr.next
    return ''.join(map(str, digits[::-1]))

def add(l1, l2):
    if not l1:
        return l2
    
    if not l2:
        return l1

    res = ListNode(-1)
    iter = res
    carry = 0
    while l1 or l2 or carry:
        a = l1.value if l1 else 0
        b = l2.value if l2 else 0
        s = a + b + carry
        digit = s % 10
        carry = 1 if s > 9 else 0
        iter.next = ListNode(digit)
        iter = iter.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
    
    return res.next

tests = [
    (ListNode(9,ListNode(9)),ListNode(5,ListNode(2)), '124'),
    (ListNode(9), None, '9'),
    (None, ListNode(9), '9'),
    (None, None, ''),
]

for tt in tests:
    assert serialize_list(add(tt[0],tt[1])) == tt[2]
