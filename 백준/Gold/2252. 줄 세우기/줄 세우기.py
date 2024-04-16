import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rsplit())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
q = deque()

for _ in range(m):
    a, b = map(int, input().rsplit())
    graph[a].append(b)
    indegree[b] += 1

ans = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans.append(i)
while q:
    cur = q.popleft()
    
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            ans.append(i)

print(*ans)