from collections import deque

def solution(n, edge):

    graph = [[] for _ in range(n+1)]
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    # for i in graph:
        # print(i)
    
    q = deque()
    q.append((1, 0))
    
    visited = [False for i in range(n+1)]

    while q:    
        current, distance = q.popleft()
        if visited[current]:
            continue
        if distance:
            visited[current] = distance
        
        else:
            visited[current] = True    
        for i in graph[current]:
            q.append((i, distance+1))

    max_num = max(visited)
    cnt = 0
    for i in visited:
        if i == max_num:
            cnt += 1
            
    return cnt


n = 6
v = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, v)