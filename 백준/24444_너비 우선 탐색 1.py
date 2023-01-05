import sys
sys.setrecursionlimit(1000000) 

input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())

edges = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
queue = []
cnt = 1
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(len(edges)):
    edges[i].sort()
    
def bfs(node):
    global cnt
    
    queue.append(node)
    visited[node] = cnt
    cnt += 1 
    
    while queue:
        popedNode = queue.pop(0)
        for i in edges[popedNode]:
            if visited[i] == 0 :
                visited[i] = cnt
                cnt += 1
                queue.append(i)

bfs(r)

for i in visited[1:]:
    print(i)
"""
5 5 1
1 4
1 2
2 3
2 4
3 4    
"""