import sys

input = sys.stdin.readline

n = int(input())
data=[list(map(int, input().split())) for _ in range(n)]

# dp[n] = max(dp[n-1], dp[n])

dp = [ [0 for _ in range(n)] for _ in range(n)]
dp[0][0] = data[0][0]

for i in range(1, n):
    for j in range(0, len(data[i])):
        
        if j == 0:
            dp[i][j] = dp[n-1][j]
        elif j == len(data[i])-1:
            dp[i][j] = dp[n-1][j-1]
            
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]

print(max(dp[n-1]))

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""