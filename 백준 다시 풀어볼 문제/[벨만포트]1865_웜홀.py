import sys
import math
import heapq
input = sys.stdin.readline

T = int(input())

def bf(start):
    dist[start] = 0
    
    for i in range(N):
        for j in range(M+W):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            
            if dist[cur] != math.inf and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == N - 1:
                    return True
                
    return False


for i in range(T):
    N, M, W = map(int, input().rstrip().split())
    graph = [[] for _ in range(N+1)]
    dist = [math.inf for _ in range(N+1)]
    edges = []
    
    for _ in range(M):
        S, E, T = map(int, input().rstrip().split())
        graph[S].append((E, T))
        edges.append((S, E, T))
    for _ in range(W):
        S, E, T = map(int, input().rstrip().split())
        graph[S].append((E, -T))
        edges.append((S, E, -T))
    
    negative_cycle = bf(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")
