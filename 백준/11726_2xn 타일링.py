import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])
"""
1
1

2
2

3
3

4
5

5
8

6
13

7
21

8
34

9 
55
"""