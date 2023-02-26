import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().rstrip().split())
    times = list(map(int, input().rstrip().split()))
    graph = [[] for _ in range(N+1)]
    total_times = [0 for _ in range(N+1)]
    #테스트들을 모두 통과, 제출 시 4% 오답
    # graph = [0 for _ in range(N+1)]
    # need_prev_build = [[] for _ in range(N+1)]
    # next_building = [[] for _ in range(N+1)]
    # visited = [False for _ in range(N+1)]
    # q = deque()
    
    # for i in range(K):
    #     s, e = map(int, input().rstrip().split())
    #     need_prev_build[e].append(s)
    #     next_building[s].append(e)
    
    # for i in range(1, len(need_prev_build)):
    #     if not need_prev_build[i]:
    #         graph[i] = times[i-1]
    #         q.append(i)
    # while q:
    #     current = q.popleft()
    #     if visited[current] : continue
    #     visited[current] = True

    #     for nextBuild in next_building[current]:
    #         prev_build_success = True
    #         for needBuild in need_prev_build[nextBuild]:
    #             if graph[needBuild] == 0:
    #                 prev_build_success = False
    #                 break
    #         if prev_build_success :
    #             q.append(nextBuild)
    #         graph[nextBuild] = max(graph[nextBuild], graph[current]+times[nextBuild-1])
    # target = int(input())
    # print(graph[target])

    #위상정렬 이용
    inDegree = [0 for _ in range(N+1)]
    
    q = deque()
    for i in range(K):
        s, e = map(int, input().rstrip().split())
        graph[s].append(e)
        inDegree[e] += 1
    
    for i in range(1, N+1):
        if inDegree[i] == 0:
            total_times[i] = times[i-1]
            q.append(i)
    
    for i in range(1, N+1):
        current = q.popleft()
        
        for j in range(len(graph[current])):
            temp = graph[current][j]
            inDegree[temp] -= 1
            total_times[temp] = max(total_times[temp], total_times[current]+times[temp-1])
            if inDegree[temp] == 0:
                q.append(temp)

    target = int(input())
    print(total_times[target])