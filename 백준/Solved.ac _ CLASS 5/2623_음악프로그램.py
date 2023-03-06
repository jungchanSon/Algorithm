import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(M+1)]
in_degree = [0 for _ in range(N+1)]

for i in range(1, M+1):
    data = list(map(int, input().rstrip().split()))

    for j in range(2, data[0]+1):
        in_degree[data[j]] += 1
        
    graph[i] = data[1:]

q = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)
        
ans = []
index_arr = [0 for _ in range(M+1)]
while q:
    check = True
    current = q.popleft()
    ans.append(current)
    for i in range(1, M+1):
        index = index_arr[i]
        if graph[i][index] == current:
            if index+1 < len(graph[i]):
                in_degree[graph[i][index+1]] -= 1
                if in_degree[graph[i][index+1]] == 0:
                    q.append(graph[i][index+1])
                index_arr[i] += 1

if len(ans) != N:
    print(0)
else:
    print(*ans, sep="\n")