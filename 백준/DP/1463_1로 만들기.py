import sys
import math
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]

#dp[n] = dp[]
if n == 1 :
    print(0)
elif n == 2: 
    print(1)
elif n == 3:
    print(1)
else :
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, n+1):
        a = 0
        b = 0
        if i % 3 == 0:
            a = dp[i // 3] + 1
        if i % 2 == 0:
            b = dp[ i // 2] + 1
            
        c = dp[i - 1] + 1

        if a and b :
            dp[i] = min(a,b,c)
        elif a :
            dp[i] = min(a,c)
        elif b : 
            dp[i] = min(b,c)
        else :
            dp[i] = c
            
    print(dp[n])
"""
1   0
2   1
3   1
4   2
5   3
6   2
7   3
"""