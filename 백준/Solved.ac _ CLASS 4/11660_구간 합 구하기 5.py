import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr1 = []
arr2 = []

for _ in range(N):
    arr1.append(list(map(int, input().rstrip().split())))
for _ in range(M):
    arr2.append(list(map(int, input().rstrip().split())))


dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(len(arr1[0])):
    dp[0][i] = sum(arr1[0][:i+1])
for i in range(1, N):
    for j in range(0, N):
        dp[i][j] = dp[i-1][j]
        for k in range(j+1):
            dp[i][j] += arr1[i][k]

for data in arr2:
    x1, y1, x2, y2 = data
    if x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1:
        print(dp[x2-1][y2-1]-dp[x2-1][y1-2])
    elif y1 == 1:
        print(dp[x2-1][y2-1]-dp[x1-2][y2-1])
    else :
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2] - dp[x1-2][y2-1] + dp[x1-2][y1-2])