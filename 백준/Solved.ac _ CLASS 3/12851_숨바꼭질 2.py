import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
visited = [-1 for _ in range(100001)]

def bfs():
    q = deque()
    q.append((N, 0))
    m = 1
    c = 0
    while q:
        current, cnt = q.popleft()
        if visited[current] != -1 and current == K:
            if cnt < visited[current] : 
                visited[current] = cnt
                m = 1
            elif cnt == visited[current]:
                m += 1
        else : 
            visited[current] = cnt
        
        if current - 1 >= 0 and visited[current-1] == -1:
            q.append((current-1, cnt+1))
        if current + 1 <= 100000 and visited[current+1] == -1:
            q.append((current+1, cnt+1))
        if current and current*2 <= 100000 and visited[current*2] == -1:
            q.append((current*2, cnt+1))
    return m
    
m = bfs()
print(visited[K])
print(m)