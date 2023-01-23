# import sys
# import math
# input = sys.stdin.readline

# n = int(input())
# arr = []
# dp = [[0 for _ in range(n)] for _ in range(n)]

# for _ in range(n):
#     arr.append(input().rstrip().split())

# for i in range(1, n):
#     for j in range(i-1, -1 , -1):
#         min_ = math.inf
#         for k in range(i-j):
            
#             ss = 1
#             s = 1
#             if i-j == 1:
#                 ss *= int(arr[j][0]) 
#                 ss *= int(arr[i][0])
#                 ss *= int(arr[i][1])
#                 min_ = min(min_, dp[i-k][i] + dp[i][j-k-1] + ss )
                
#             else :
#                 l = arr[:n-k-1] 
#                 r = arr[n-k-1:]
#                 if i > j:
#                     s *= int(l[0][0])
#                     s *= int(l[-1][1])
#                     s *= int(r[-1][1])
#                 else :
#                     s *= int(l[0][0])
#                     s *= int(r[0][0]) 
#                     s *= int(r[-1][1])
#                 min_ = min(min_, dp[i-k][i] + dp[j][i-k-1] + s )
                    
#         dp[j][i] = min_
        
# print(dp[0][n-1])



import sys
import math
input = sys.stdin.readline

n = int(input())
arr = []
dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    arr.append(input().rstrip().split())
    
# dp[x, y] = dp[x, k] + dp[k+1, y] +r(x) + c(k) + c(y)

dp = [[0 for _ in range(n)] for _ in range(n)]
def rec(x, y):
    
    if dp[x][y] : return dp[x][y]
    if y-x <= 0 : return 0
    
    m = math.inf 
    for k in range(x, y):
        m = min(m, rec(x,k) + rec(k+1, y) + int(arr[x][0])*int(arr[y][1])*int(arr[k][1]) )

    dp[x][y] = m
    return dp[x][y] 

print(rec(0, n-1))