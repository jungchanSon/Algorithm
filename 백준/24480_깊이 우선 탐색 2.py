import sys
sys.setrecursionlimit(1000000) 
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
edges = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 1
for i in range(m):
    a, b = map(int, input().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)
    
for i in range(len(edges)):
    edges[i].sort(reverse=True)

def dfs(node):
    global cnt
    
    if visited[node] != 0:
        return

    visited[node] = cnt
    cnt += 1
    
    for i in edges[node]:
        dfs(i)
    
dfs(r)
for ans in visited[1:]:
    print(ans)
"""
5 5 1
1 4
1 2
2 3
2 4
3 4
"""