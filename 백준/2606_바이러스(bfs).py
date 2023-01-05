import sys
input = sys.stdin.readline

com = int(input())
n = int(input())
edges = [[] for _ in range(com+1)]
visited = [False for _ in range(com+1)]
q = []

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

def bfs(node):
    q.append(node)
    
    while q:
        current = q.pop(0)
        for i in edges[current]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

bfs(1)
print(sum(visited) - 1)