import heapq
import sys
import copy
input = sys.stdin.readline

inf = 1e9

v, e = map(int, input().rsplit())
graph = [[inf for _ in range(v+1)] for _ in range(v+1)] 

for i in range(1, v+1):
    graph[i][i] = 0
    
    
for _ in range(e):
    a,b,c = map(int, input().rsplit())
    graph[a][b] = c
        
distance = [inf for _ in range(v+1)]
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = inf
for x in range(1, v):
    for y in range(x+1, v+1):
        ans = min(ans, graph[x][y]+graph[y][x])
        
if ans < inf:
    print(ans)
else:
    print(-1)