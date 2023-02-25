import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().rstrip().split())
    times = list(map(int, input().rstrip().split()))
    graph = [0 for _ in range(N+1)]
    need_prev_build = [[] for _ in range(N+1)]
    next_building = [[] for _ in range(N+1)]
    
    for i in range(K):
        s, e = map(int, input().rstrip().split())
        need_prev_build[e].append(s)
        next_building[s].append(e)
    target = int(input())

    q = deque()
    
    for i in range(1, len(need_prev_build)):
        if not need_prev_build[i]:
            graph[i] = times[i-1]
            q.append(i)
    
    visited = [False for _ in range(N+1)]
    while q:
        current = q.popleft()
        if visited[current] : continue
        visited[current] = True

        for nextBuild in next_building[current]:
            prev_build_success = True
            for needBuild in need_prev_build[nextBuild]:
                if graph[needBuild] == 0:
                    prev_build_success = False
                    break
            if prev_build_success :
                q.append(nextBuild)
            graph[nextBuild] = max(graph[nextBuild], graph[current]+times[nextBuild-1])
    print("-------")
    for i in graph:
        print(i)
    print("--------")
    print(graph[target])