import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
heap = []

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B) 
    in_degree[B] += 1
    

for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        heapq.heappush(heap, i )
while heap:
    current = heapq.heappop(heap)

    print(current, end=" ")
    
    for i in graph[current]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(heap, i)
            
    