import sys
import math
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
item_num = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n+1)]
distance = [math.inf for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().rstrip().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
    
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
    
ans_list = []
for start in range(1, n+1):
    sum_item = 0

    distance = [math.inf for _ in range(n+1)]
    dijkstra(start)
    
    for i in range(1, n+1):
        if distance[i] <= m:
            sum_item += item_num[i-1]
    ans_list.append(sum_item)
    
print(max(ans_list))