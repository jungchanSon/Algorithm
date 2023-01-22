import sys
import heapq 

input = sys.stdin.readline
maxheap = []

N = int(input().rstrip())
for i in range(N):
    num = int(input())
    if num:
        heapq.heappush(maxheap, -num)
    else :
        if len(maxheap) == 0:
            print( 0)
        else:
            print( -1 * heapq.heappop(maxheap))