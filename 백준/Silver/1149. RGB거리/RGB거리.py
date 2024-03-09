import sys
input = sys.stdin.readline

n = int(input().rstrip())
house = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0] = house[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]

print(min(dp[n-1]))