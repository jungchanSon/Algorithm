import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr.sort()

for i in range(len(arr)):
    
    arr[i]
    
def bt(i, depth, l):
    if depth == M:
        print(*l)
        return
    
    for i in range(len(arr)):
        if visited[i] == False :
            visited[i] = True
            bt(i, depth+1, l+[arr[i]])
            visited[i] = False

for i in range(N):
    visited = [False for _ in range(N)]
    visited[i] = True
    bt(i, 1, [arr[i]])