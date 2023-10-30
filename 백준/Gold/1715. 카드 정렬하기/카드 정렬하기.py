import sys
import bisect
import heapq

input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    a = int(input())
    heapq.heappush(h, a)
if len(h) == 1:
    print(0)
    quit()

ans = 0
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    res = a+b
    ans += res
    heapq.heappush(h, res)
    
print(ans)
