import sys
import math
input = sys.stdin.readline

N = 6
M =  [[1,2,2], [1,4,1], [1,3,5], [2,3,3], [2,4,2],
				[3,4,3], [3,5,1], [4,5,1], [5,6,2], [3,6,5]]

start = int(input())
gragph = [[] for i in range(N+1)]
visited = [False] * (N+1)
distance = [math.inf] * (N+1)

for i in M:
    gragph[i[0]].append((i[1], i[2]))

def get_smallest_node():
    min_value = math.inf
    index = 0
    
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for j in gragph[start]:
        distance[j[0]] = j[1]
    
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in gragph[now]:
            cost = distance[now] + j[1] 
            if cost < distance[j[0]]:
                distance[j[0]] = cost


def dijkstra2(start):
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
 
dijkstra(start)

for i in range(1, N+1):
    if distance[i] == math.inf:
        print("inf")
    else:
        print(distance[i])
        
# https://www.youtube.com/watch?v=acqm9mM1P6o