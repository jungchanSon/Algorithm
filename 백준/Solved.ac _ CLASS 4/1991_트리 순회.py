import sys
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(N):
    p, l, r = input().rstrip().split()
    arr[ord(p)-65].append(ord(l)-65)
    arr[ord(p)-65].append(ord(r)-65)

ans = []
ans1 = []
ans2 = []
def dfs(n):
    if n == -19 :
        return
    if n >= N:
        ans.append(chr(n+65))
        ans1.append(chr(n+65))
        return
    if visited[n]: 
        return
    else :
        visited[n] = True

    l = arr[n][0]
    r = arr[n][1]
    ans.append(chr(n+65))
    dfs(l)
    ans1.append(chr(n+65))
    
    dfs(r)
    
for i in range(N):
    if not visited[i]:
        dfs(i)
        
        
visited2 = [False for _ in range(N+1)]
def dfs2(n):
    if n == -19 :
        return
    if n >= N:
        ans2.append(chr(n+65))
        return
    if visited2[n]: 
        return
    else :
        visited2[n] = True
    l = arr[n][0]
    r = arr[n][1]
    
    dfs2(l)
    dfs2(r)
    ans2.append(chr(n+65))
    
for i in range(0, N):
    if not visited2[i]:
        dfs2(0)
        
print("".join(ans))
print("".join(ans1))
print("".join(ans2))

