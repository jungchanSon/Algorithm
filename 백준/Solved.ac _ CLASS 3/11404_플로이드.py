import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())
gragh = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().rstrip().split())
    if gragh[start][end]:
        gragh[start][end] = min(gragh[start][end], cost)
    else:
        gragh[start][end] = cost
    
# for i in range(1, n+1):
#     gragh[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            gragh[i][j] = min(gragh[i][j], gragh[i][k]+gragh[k][j])
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or gragh[i][j] == math.inf:
            gragh[i][j] = 0

for i in gragh[1:]:
    print(*i[1:])