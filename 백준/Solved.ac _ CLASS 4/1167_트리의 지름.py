import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(N):
    data = list(map(int, input().rstrip().split()))
    node = data[0]
    for i in range(1, len(data)-1, 2):
        arr[node].append((data[i],data[i+1]))

def dfs(n, d):
    global maxDistance
    if visited[n]:
        return d
    else :
        visited[n] = True
    if d > a[1]:
        a[0] = n
        a[1] = d

    maxDistance = max(maxDistance, d)
    
    for i in arr[n]:
        nextNode, distance = i
        if not visited[nextNode]:
            dfs(nextNode, d+distance)
    

maxDistance = 0

a = [0, 0]
visited = [False for _ in range(N+1)]
dfs(1, 0)
visited = [False for _ in range(N+1)]
maxDistance = 0
dfs(a[0], 0)
print(maxDistance)

"""
시간초과 해결

트리의 최대 지름 구하는 공식
1. 임의의 노드 A에서 가장 먼 노드 B
2. B에서 가장 먼 노드 A까지의 거리가 트리의 최대 지름.
"""