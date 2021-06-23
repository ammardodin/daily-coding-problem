#!/usr/bin/env python3


class OrderIDLog():
    def __init__(self, n) -> None:
        self.max_size = n
        self.buffer = [0] * n
        self.last = 0
    
    def record(self, order_id) -> None:
        self.buffer[self.last] = order_id
        self.last = (self.last + 1) % self.max_size
    
    def get_last(self, i) -> int:
        return self.buffer[(self.last - i + self.max_size) % self.max_size]

log = OrderIDLog(3)
log.record(1)
assert log.get_last(1) == 1
log.record(2)
assert log.get_last(1) == 2
assert log.get_last(2) == 1
log.record(3)
assert log.get_last(1) == 3
assert log.get_last(2) == 2
assert log.get_last(3) == 1
log.record(5)
assert log.get_last(1) == 5
assert log.get_last(2) == 3
assert log.get_last(3) == 2