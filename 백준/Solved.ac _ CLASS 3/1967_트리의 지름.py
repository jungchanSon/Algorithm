import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
gragh = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(n-1):
    p, c, w = map(int, input().rstrip().split())
    gragh[p].append((c,w ))
    gragh[c].append((p,w ))

# for i in gragh:
#     print(i)

s = (0, 0)
def dfs(start, w):
    global s, n1
    
    if visited[start]:
        return
    visited[start] = True

    if w > s[1]:
        s = (start, w)
    for next_node, weight in gragh[start]:
        dfs(next_node, weight+w)
        
dfs(1, 0)
visited = [0 for _ in range(n+1)]
dfs(s[0], 0)
print(s[1])