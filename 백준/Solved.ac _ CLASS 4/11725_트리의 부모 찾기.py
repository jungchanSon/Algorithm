import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

ans = [0 for _ in range(N+1)]
def dfs(n):
    if visited[n]:
        return
    else :
        visited[n] = True
        
    for i in arr[n]:
        if not ans[i]: 
            ans[i] = n
        dfs(i)
visited = [False for _ in range(N+1)]
dfs(1)
for i in ans[2:]:
    print(i)