import heapq
import sys
import copy
input = sys.stdin.readline
inf = 1e9

n = int(input())
a, b = map(int, input().rsplit())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    c, p = map(int, input().rsplit())
    graph[c].append(p)
    graph[p].append(c)

visited = [False for _ in range(n+1)]
q = [(a, 0)]
check = True
while q: 
    c, l = q.pop(0)
    if c == b:
        print(l)
        check =False
    for k in graph[c]:
        if visited[k]:
            continue
        q.append((k, l+1))
        visited[k] = True

if check:
    print(-1)