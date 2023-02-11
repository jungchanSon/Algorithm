import math

n = int(input())
m = int(input())

graph = [[math.inf for _ in range(n+1)] for _ in range(n+1) ]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b :
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == math.inf:
            print("INF")
        else:
            print(graph[a][b])

# https://www.youtube.com/watch?v=hw-SvAR3Zqg&t=551s