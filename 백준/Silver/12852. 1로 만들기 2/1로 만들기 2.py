import sys
input = sys.stdin.readline
N = int(input())
dp = [1e9 for _ in range(N*3 +1)]

if N == 1:
    print(0)
    print(1)
else:
    dp[1] = 0
    for i in range(1, N+1):
        dp[i*2] = min(dp[i*2], dp[i] + 1)
        dp[i*3] = min(dp[i*3], dp[i] + 1)
        dp[i+1] = min(dp[i+1], dp[i] + 1)
    print(dp[N])
    while N >0:
        print(N, end=" ")
        if N % 2 == 0 and dp[N//2] == dp[N] - 1:
            N //= 2
        elif N % 3 == 0 and dp[N//3] == dp[N] - 1:
            N //= 3
        else:
            N -= 1
# dp[n] = min(dp[n//2] + 1, dp[n//3] + 1, dp[n-1] + 1)
