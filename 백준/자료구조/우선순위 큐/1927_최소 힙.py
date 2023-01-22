import sys
import heapq

input = sys.stdin.readline

N = int(input())

minHeap = []
for _ in range(N):
    num = int(input())
    
    if num:
        heapq.heappush(minHeap, num)
    else :    
        if len(minHeap) == 0 : 
            print(0)
        else:
            print(heapq.heappop(minHeap))