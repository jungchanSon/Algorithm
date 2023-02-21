import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
visited = [False for _ in range(N)]
arr.sort()


def bt(i, depth, l):
    if depth == M:
        print(*l)
        return
    
    for j in range(len(arr)):
        if visited[j] == False:
            visited[j] = True
            bt(j, depth+1, l+[arr[j]])
            visited[j] = False

for i in range(N):
    visited = [False for _ in range(N)]
    visited[i] = True
    bt(i, 1, [arr[i]])
    
