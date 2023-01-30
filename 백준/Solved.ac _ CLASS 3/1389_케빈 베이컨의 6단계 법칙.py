import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [[] for _ in range(N+1)]
result = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs():
    sums = 0

    while q :
        a, p = q.pop(0)
        
        if visited[a]:
            continue
        visited[a] = True
        sums += p
        
        for i in arr[a]:
            q.append((i, p+1))
            
    return sums

for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    
    q = [(i, 0)]
    result[i] = bfs()
    
print(result.index(min(result[1:])))