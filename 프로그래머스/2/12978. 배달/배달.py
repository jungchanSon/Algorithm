from math import inf
import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]
    distance = [inf for _ in range(N+1)]
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))
    start = 1
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    print(distance)
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    return answer