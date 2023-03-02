import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
in_degree = [0 for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
q = deque()

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    arr[a].append(b)
    in_degree[b] += 1
    
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)
# print(q)
# for i in arr:
#     print(i)
ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    next_node = arr[cur]
    for i in next_node:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)

print(*ans)
        
#위상 정렬