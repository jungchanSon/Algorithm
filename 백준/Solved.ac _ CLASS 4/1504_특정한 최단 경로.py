import sys
import math
import heapq
input = sys.stdin.readline

N, E = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
distance = [math.inf for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

a, b = map(int, input().rstrip().split())
must = [a, b]

def dijkstra(start):
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

result = [0 for _ in range(N+1)]
distance = [math.inf for _ in range(N+1)]
dijkstra(1)
result[1] = (distance)

distance = [math.inf for _ in range(N+1)]
dijkstra(N)
result[N] = (distance)

distance = [math.inf for _ in range(N+1)]
dijkstra(must[0])
result[must[0]]=(distance)

distance = [math.inf for _ in range(N+1)]
dijkstra(must[1])
result[must[1]] = (distance)

n1 = result[1][must[0]] + result[must[0]][must[1]] + result[must[1]][N]
n2 = result[1][must[1]] + result[must[1]][must[0]] + result[must[0]][N]
if n1 == math.inf or n2 == math.inf:
    print(-1)
else:
    print(min(n1, n2))
