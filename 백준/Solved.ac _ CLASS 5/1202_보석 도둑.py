import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
items = []
ans = 0

for _ in range(N):
    m, v = map(int, input().rstrip().split())
    heapq.heappush(items, (m, v))
    
bag = []
for _ in range(K):
    heapq.heappush(bag, int(input()))

temp = []
while bag:
    current_weight = heapq.heappop(bag)
    while items:
        m, v = heapq.heappop(items)
        if m > current_weight:
            heapq.heappush(items, (m, v))
            break
        
        heapq.heappush(temp, -v)
    if temp:
        ans += -heapq.heappop(temp)

print(ans)