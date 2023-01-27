import sys
input = sys.stdin.readline


T = int(input())

dp = [0 for _ in range(41)]

dp[0] = 0
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]


for _ in range(T):
    n = int(input())

    if n == 0:
        print(1, 0)
    else :
        print(dp[n-1], dp[n])