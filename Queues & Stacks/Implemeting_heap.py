# https://docs.python.org/3/library/heapq.html

# heap uses the formula below to reach each node since heap can be applied using arr in python: heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]

import heapq

# python comes with heapq module in to heapity any arr
a = [23, 115, 63, 38, 542, 79, 0, 455]
heapq.heapify(a)
# pushing into heap
heapq.heappush(a, 8880)	
print(a)
# poping from heap:
heapq.heappop(a)
print(a)