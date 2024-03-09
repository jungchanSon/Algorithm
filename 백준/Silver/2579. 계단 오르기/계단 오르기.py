import sys
input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]

if n == 1:
    print(stair[0])
    quit()
if n == 2:
    print(stair[0]+stair[1])
    quit()

dp = [[0,0] for _ in range(n+1)]
dp[1][0] = stair[0]
dp[2][0] = stair[1]
dp[2][1] = stair[1]+dp[1][0]
    
for i in range(3, n+1):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stair[i-1]
    dp[i][1] = dp[i-1][0] + stair[i-1]

print(max(dp[n]))