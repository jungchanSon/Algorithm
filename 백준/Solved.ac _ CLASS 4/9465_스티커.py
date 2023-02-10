import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0,0] for _ in range(N)]
    arr1 = list(map(int, input().rstrip().split()))
    arr2 = list(map(int, input().rstrip().split()))
    
    flag = 0
    up = 0
    down = 0
    dp[0][0] = arr1[0]
    dp[0][1] = arr2[0]
    if N == 1:
        print(max(dp[0][0], dp[0][1]))
        continue
    dp[1][0] = dp[0][1]+arr1[1] 
    dp[1][1] = dp[0][0]+arr2[1]
    if N == 2:
        print(max(dp[1][0], dp[1][1]))
        continue
    for i in range(2, N):
        prevprev = max(dp[i-2][0], dp[i-2][1])
        
        dp[i][0] = max(prevprev+arr1[i], dp[i-1][1]+arr1[i])
        dp[i][1] = max(prevprev+arr2[i], dp[i-1][0]+arr2[i])
    
  
    print(max(dp[N-1][0], dp[N-1 ][1]))           
    
#점화식
"""
    dp[n] = max(dp[n-1], dp[n-2])
""" 