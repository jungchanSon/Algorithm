import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# for i in board:
#     print(i)
    
#dp
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    if board[0][i] != 1:
        dp[0][i][0] = 1
    else : break


for i in range(1, N):
    for j in range(2, N):
        if board[i][j] != 1 and board[i][j-1] != 1:
            dp[i][j][0] = dp[i][j-1][2] + dp[i][j-1][0]
        if board[i][j] != 1 and board[i-1][j] != 1:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if board[i][j] != 1 and board[i-1][j-1] != 1 and board[i-1][j] != 1 and  board[i][j-1] != 1:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
# for i in dp:
#     print(i)
"""
dp[n][n] = dp[n-1][n-1] + dp[n-1][n] + dp[n][n-1]

"""

print(dp[N-1][N-1][0]+dp[N-1][N-1][1]+dp[N-1][N-1][2])