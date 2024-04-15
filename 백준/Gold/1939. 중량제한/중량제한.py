import sys

input = sys.stdin.readline

n, m = map(int, input().rsplit())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rsplit())
    graph[a].append((b,c))    
    graph[b].append((a,c))

start, end = map(int, input().rsplit())


from collections import deque

def bfs(w):
    visited = [False for _ in range(n+1)]
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for t, tw in graph[cur]:
            if not visited[t] and tw >= w:
                visited[t] = True
                q.append(t)
    if visited[end] :
        return True
    else: 
        return False

l, r = 0, 1000000000
ans = 0
while l <= r :
    mid = (l+r) //2
    if bfs(mid):
        ans = mid
        l = mid+1
    else :
        r = mid-1
print(ans)