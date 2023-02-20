import sys
import math
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [math.inf for _ in range(n+1)]

for i in range(m):
    s, e, c = map(int, input().rstrip().split())
    graph[s].append((e, c))

start, end = map(int, input().rstrip().split())
path = []

def dijkstra(start):
    global path
    
    q = []
    heapq.heappush(q, (0, start, [start]))
    distance[start] = 0
    
    while q:
        dist, now, arr= heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0], arr + [i[0]]))
        if now == end:
            path = arr
dijkstra(start)

print(distance[end])
print(len(path))
print(*path)