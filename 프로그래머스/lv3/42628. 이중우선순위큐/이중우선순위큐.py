#이중우선순위큐
import heapq
from collections import deque

def solution(operations):
    answer = []
    operations = deque(operations)
    max_heap = []
    min_heap = []
    while operations:
        cur_op, cur_n = operations.popleft().split()
        cur_n = int(cur_n)
        if cur_op == "I":
            heapq.heappush(min_heap, cur_n)
            heapq.heappush(max_heap, -cur_n)

        if cur_op == "D" and min_heap:
            if cur_n == 1: 
                n = heapq.heappop(max_heap)
                min_heap.remove(-n)
                heapq.heapify(min_heap) 
            elif cur_n == -1:
                n = heapq.heappop(min_heap)
                max_heap.remove(-n)
                heapq.heapify(min_heap)
    if not min_heap or not max_heap:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
data = [["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	]

