import sys
import heapq
from math import inf

input = sys.stdin.readline

N, M, K, X = map(int, input().rsplit())
graph = [[] for _ in range(N+1)]
distance = [inf for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)


def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijstra(X)
ans = []
for i in range(len(distance)):
    if distance[i] == K:
        ans.append(i)
        
if ans:
    for i in ans:
        print(i)
else:
    print(-1)
    
