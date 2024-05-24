import heapq
import sys
import copy
input = sys.stdin.readline
inf = 1e9

N = int(input())
dp = [0 for _ in range(N+3)]
arr = [list(map(int, input().rsplit())) for _ in range(N)]

arr = [0] + arr
ans = 0
for i in range(1, N+1):
    t, p= arr[i]
    
    if i+t <= N+1:
        dp[i+t] = max(dp[i+t], dp[i] + p)
        ans = max(ans, dp[i+t])
    dp[i+1] = max(dp[i+1], dp[i])
    ans = max(ans,dp[i+1])
print(ans)