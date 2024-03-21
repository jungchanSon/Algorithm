import sys
from math import inf
import heapq
input = sys.stdin.readline

N, D = map(int, input().rsplit())
graph = [[] for _ in range(10_001)]
distance = [inf for _ in range(10_001)]
arr = []
path = []
for i in range(D+1):
    graph[i].append((i+1, 1))
for _ in range(N):
    s, e, d = map(int, input().rsplit())
    # if e >= d:
    #     continue
    graph[s].append([e, d])
    arr.append(s)    

q = []
def dijstra(start):
    q = []
    heapq.heappush(q, (0 , start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijstra(0)
print(distance[D])