import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = []
dp = [[-1 for _ in range(n)] for _ in range(m)]
for _ in range(m):
    arr.append(list(map(int, input().rstrip().split())))
dp[0][0] = 1
def rec(x, y, w):
    if dp[y][x] != -1 : return dp[y][x]
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    path = 0
    if x-1 >= 0 and arr[y][x-1] > w :
        path += rec(x-1, y, arr[y][x-1])
    if x+1 < n and arr[y][x+1] > w :
        path += rec(x+1, y, arr[y][x+1])
    if y-1 >= 0 and arr[y-1][x] > w :
        path += rec(x, y-1, arr[y-1][x] )
    if y+1 < m and arr[y+1][x] > w :
        path += rec(x, y+1, arr[y+1][x])
    
    dp[y][x] = path
    return dp[y][x]
# start = time.time()

print(rec(n-1, m-1, arr[m-1][n-1]))

# end = time.time() 
# print(end-start)
"""
dp[n][m] = dp[n-1][m] + dp[n+1][m] + dp[n][m-1] + dp[n][m+1]
 
"""

"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
"""