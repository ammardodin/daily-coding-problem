#!/usr/bin/env python3
from heapq import heappop, heappush

# O(N^2logN)
def running_median(sequence):
    def median(start, end):
        length = end - start + 1
        mid = length // 2
        sorted_seq = sorted(sequence[start:end+1])
        if length & 1:
            return sorted_seq[mid]
        return (sorted_seq[mid-1] + sorted_seq[mid])/2
    
    def running_median_indices():
        start = 0
        end = start
        while end < len(sequence):
            yield (start,end)
            end = end + 1
    
    medians = [0] * len(sequence)
    for i, indices in enumerate(running_median_indices()):
        start, end = indices
        medians[i] = median(start, end)
    return medians


assert running_median([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]

# O(NlogN)
"""
low is a max heap representing values less than effective median
high is a min heap representing values greater than effective median
"""
def running_median_opt(sequence):
    low = []
    high = []
    medians = []
    for element in sequence:
        heappush(low, -element)
        heappush(high, -heappop(low))
        diff = len(low) - len(high)
        if diff < 0:
            heappush(low, -heappop(high))
        
        if len(low) > len(high):
            medians.append(-low[0])
        else:
            medians.append((-low[0]+high[0])/2)
    return medians

assert running_median_opt([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]