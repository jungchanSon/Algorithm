import sys
import math
import heapq
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
K = int(input())
distance = [math.inf for _ in range(V+1)]
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
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
                
djikstra(K)
for i in distance[1:]:
    print(i)