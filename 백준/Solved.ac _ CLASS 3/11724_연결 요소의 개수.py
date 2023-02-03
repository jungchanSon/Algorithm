import sys
input = sys.stdin.readline 

N, M = map(int, input().rstrip().split())

nodes = [[] for _ in range(N+1) ]
visited = [False for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    nodes[a].append(b)
    nodes[b].append(a)
    
def dfs(n):
    if visited[n]: 
        return
    
    visited[n] = True
    
    for item in nodes[n]:
        dfs(item)
    
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        # print(i, visited)
        cnt += 1

print(cnt)