import heapq
import sys
import copy
input = sys.stdin.readline
inf = 1e9

n = int(input())
dp = [0 for _ in range(91)]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
cnt = 1
for i in range(4, 91):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])