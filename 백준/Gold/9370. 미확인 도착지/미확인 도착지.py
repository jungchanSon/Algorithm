import math
import heapq
import sys
import copy
input = sys.stdin.readline

T = int(input())
def dij(start: int):
    q = []
    heapq.heappush(q, (0, start))
    distance[start ] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
for _ in range(T):
    n,m,t = map(int, input().rsplit())
    s,g,h = map(int, input().rsplit())
    graph = [[] for _ in range(n+1)]
    target = []
    distance = [100000000  for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int, input().rsplit())
        graph[a].append((b,d))
        graph[b].append((a,d))
 
    target = [int(input()) for _ in range(t)]
    dij(s)
    r = copy.deepcopy(distance)
    distance = [100000000  for _ in range(n+1)]
    dij(g)
    rg = copy.deepcopy(distance)
    distance = [100000000  for _ in range(n+1)]
    dij(h)
    rh = copy.deepcopy(distance)
    ans = []
    for i in target:
        v1 = r[g]+rg[h]+rh[i]
        v2 = r[h]+rh[g]+rg[i]
        v = min(v1, v2)
        if r[i] == v:
            ans.append(i)
            
    ans.sort()
    print(*ans)
    