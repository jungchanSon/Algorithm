import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input().rstrip())
    dp = [0 for _ in range(n+1)]
    
    if n <= 2:
        print(n)
    elif n <= 3:
        print(4)
    
    if n <= 3:
        continue
    
    dp[1] = 1
    dp[2] = 2 
    dp[3] = 4
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])