n = int(input().rstrip())

dp = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(1<<10):
            if j == 0 :
                dp[i][j][k | (1<<0)] += dp[i-1][1][k] 
                dp[i][j][k | (1<<0)] %= 1000000000
            elif j == 9:
                dp[i][j][k | (1<<9)] += dp[i-1][8][k]
                dp[i][j][k | (1<<9)] %= 1000000000
            else:
                dp[i][j][k | (1<<j)] += (dp[i-1][j-1][k] + dp[i-1][j+1][k])
                dp[i][j][k | (1<<j)] %= 1000000000
ans = 0
for i in range(10):
    ans += dp[n][i][(1<<10) -1] 
    ans %= 1000000000
print(ans)

"""
0 -> 10
n = 1
1, 2, 3, 4, 5, 6, 7, 8, 9

n = 2 x = 2
12, 10, 21, 23

89876543210
98765432101
12345678789
"""