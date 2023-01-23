import sys
input = sys.stdin.readline
import math
N = int(input())

for _ in range(N):
    K = int(input())
    dp = [[0 for _ in range(K)] for _ in range(K)]
    
    FILES = list(map(int, input().rstrip().split()))
    
    for i in range(1, K):
        for j in range(i-1, -1, -1):
            small = math.inf
            for d in range(i-j):
                small = min(small, dp[j][i-d-1]+dp[i-d][i])
            dp[j][i] = small + sum(FILES[j:i+1])
   
    print(dp[0][K-1])
    
        
""" 
    A   B   C                   D
A   0   AB  min(AB, BC)+ABC     min(AC, BD) + ABCD
B       0   BC                  min(BC, CD) + ABCD
C           0                   CD  
D                               0
"""