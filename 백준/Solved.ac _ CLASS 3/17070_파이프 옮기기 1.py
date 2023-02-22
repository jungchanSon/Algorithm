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

#dfs
# 가로/세로/대각 == shape 0/shape 1/shape 2 
ans2 = 0
def dfs(position, shape):
    global ans2
    cy = position[0]
    cx = position[1]
    if cx == N-1 and cy == N-1:
        ans2 +=1
        return
    
    if shape == 0:
        if cx+1 < N and board[cy][cx+1] != 1:
            dfs((position[0], position[1]+1), 0)
        if cx+1 < N and cy+1 < N and board[cy+1][cx+1] != 1 and board[cy+1][cx] != 1 and board[cy][cx+1] != 1:
            dfs((position[0]+1, position[1]+1), 2)
    elif shape == 1:
        if cy+1 < N and board[cy+1][cx] != 1:
            dfs((cy+1, cx), 1)
        if cy+1 < N and cx+1 < N and board[cy+1][cx+1] != 1 and board[cy+1][cx] != 1 and board[cy][cx+1] != 1:
            dfs((cy+1, cx+1), 2)
    elif shape == 2:
        if cx+1< N and board[cy][cx+1] != 1:
            dfs((cy, cx+1), 0)
        if cy+1 < N and board[cy+1][cx] != 1:
            dfs((cy+1, cx), 1)
        if cy+1 < N and cx+1 <N and board[cy+1][cx+1] != 1 and board[cy+1][cx] != 1 and board[cy][cx+1] != 1:
            dfs((cy+1, cx+1), 2)
dfs((0, 1), 0)
print(ans2)