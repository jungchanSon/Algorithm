import sys
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
    if n == 1:
        return True
    
    for i in arr[n]:
        if dfs(i):
            ans[n] = i
            return True
for i in range(2, N+1):
    visited = [False for _ in range(N+1)]
    dfs(i)
print(*(ans[2:]), sep="\n")