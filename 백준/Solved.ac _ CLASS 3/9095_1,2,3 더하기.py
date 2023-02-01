import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2) 
        continue
    elif n == 3:
        print(4)
        continue
    dp = [0 for _ in range(n+1)]
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])
"""
dp[n] = dp[n-1]+dp[n-2]+dp[n-3]
1 1 
1

2 2 
1 1
2

3 4
1 1 1
1 2
2 1
3

4 7
1 1 1 1
1 1 2
1 2 1
2 1 1
2 2 
3 1 
1 3 

5 13 
1 1 1 1 1
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1
2 2 1 
2 1 2 
1 2 2
3 1 1 
1 3 1 
1 1 3 
2 3 
3 2 
"""