import sys
import math
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())
arr = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().rstrip().split())
    arr[start].append((end, time))

#이부분이 시간초과 나는듯 -> heap으로
def get_smallest_node():
    
    min_value = math.inf
    index = 0
    
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # for j in arr[start]:
    #     distance[j[0]] = j[1]

    # for _ in range(N-1):
    #     now = get_smallest_node()
    #     visited[now] = True
        
        # for j in arr[now]:
        #     cost = distance[now] + j[1]
        #     if cost < distance[j[0]]:
        #         distance[j[0]] = cost

result = [0 for _ in range(N+1)]
temp = []

for i in range(1, N+1):
    distance = [math.inf for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    
    dijkstra(i)

    result[i] = distance

for i in range(1, N+1):
    temp.append(result[i][X]+result[X][i])

print(max(temp))
# 참고: https://steadily-worked.tistory.com/661