#!/usr/bin/env python3

def sort_rgb(sequence):
    def bubble_up(candidate, wall):
        swap_pos, curr = wall, wall
        while curr < len(sequence):
            if sequence[curr] == candidate:
                sequence[curr], sequence[swap_pos] = sequence[swap_pos], sequence[curr]
                swap_pos = swap_pos + 1
            curr = curr + 1
        return swap_pos

    start = 0
    for c in ['R', 'G', 'B']:
        start = bubble_up(c, start)
    return sequence


assert sort_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
assert sort_rgb([]) == []
assert sort_rgb(['G', 'B', 'R', 'G']) == ['R', 'G', 'G', 'B']
assert sort_rgb(['B', 'B', 'G']) == ['G', 'B', 'B']