from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
        
    visited = [0 for _ in range(n+1)]
    
    q = deque()
    q.append((1, 0))
    
    while q:
        cn, dist = q.popleft()
        for nn in graph[cn]:
            if visited[nn] == 0: 
                visited[nn] = dist+1
                q.append((nn, dist+1))
    
    m = max(visited[2:])
    for i in visited[2:]:
        if m == i:
            answer += 1
    return answer