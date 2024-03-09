import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(n)]

if n == 1:
    print(1)
    quit()
elif n == 2:
    print(2)
    quit()

dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2 ]) % 10007 

print(dp[n-1])