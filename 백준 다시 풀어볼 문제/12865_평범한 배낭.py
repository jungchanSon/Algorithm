import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
items = []

for _ in range(n):
    items.append(list(map(int, input().split())))

dp = [[0 for _ in range(100001)] for _ in range(101) ]
def dfs(i, w):
    if dp[i][w] : 
        return dp[i][w]
    if i == n:
        return 0
    
    v1 = 0
    if w+items[i][0] <= k :
        v1 = items[i][1] + dfs(i+1, w+items[i][0]) # 넣
    v2 = dfs(i+1, w) #안넣
    dp[i][w] = max(v1, v2)
    return dp[i][w]

a = dfs(0, 0)
print(a)