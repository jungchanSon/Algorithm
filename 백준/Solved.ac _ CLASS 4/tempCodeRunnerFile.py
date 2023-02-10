import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))

dp = [1 for _ in range(N)]

dp[0] = 1

for i in range(1, N):
    maxN = 0
    for j in range(i):
        if arr[j] < arr[i]:
            maxN = max(dp[j], maxN)
    dp[i] = maxN + 1
print(dp[N-1])