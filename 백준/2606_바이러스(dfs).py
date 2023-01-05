import sys
input = sys.stdin.readline

com = int(input())
n = int(input())
edges = [[] for _ in range(com+1)]
visited = [False for _ in range(com+1)]

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

def dfs(node):
    global cnt
    
    if visited[node]:
        return
    visited[node] = True
    for i in edges[node]:
        dfs(i)

dfs(1)

print(sum(visited) - 1)