import sys
input = sys.stdin.readline

def sol1(n: int):
    ans = 0
    
    dp = [10*7 for _ in range(n+1)]
    dp[n] = 0
    
    # #sol.1 : for loop
    for i in range(n, 0, -1):
        temp = 10*7
        dp[i-1] = min(dp[i-1], dp[i]+1)
        if i % 2 == 0:
            dp[i//2] = min(dp[i//2], dp[i] + 1)
        if i % 3 == 0:
            dp[i//3] = min(dp[i//3], dp[i] + 1)
        
    print(dp[1])
    return dp[1]

sol1(int(input().rstrip()))