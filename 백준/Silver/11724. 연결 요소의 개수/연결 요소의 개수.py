import sys
import bisect
import heapq
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rsplit())
graph = [ [] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().rsplit())
    graph[s].append(e)
    graph[e].append(s)
    
ans = 0

for i in range(1, n+1):
    if visited[i]:
        continue
    ans +=1
    q = deque([i])
    visited[i] = True
    
    while q:
        cur = q.pop()
        for j in graph[cur]:
            if visited[j]:
                continue
            visited[j] = True
            q.append(j)
            
print(ans)