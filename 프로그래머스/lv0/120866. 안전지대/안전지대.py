def solution(board):
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if j-1 >= 0 and board[i][j-1] == 0:
                    board[i][j-1] = 2
                if j+1 < m and board[i][j+1] == 0:
                    board[i][j+1] = 2
                if i-1 >= 0 and board[i-1][j] == 0:
                    board[i-1][j] = 2
                if i+1 < n and board[i+1][j] == 0:
                    board[i+1][j] = 2
                if i-1 >= 0 and j-1 >=0 and board[i-1][j-1] == 0:
                    board[i-1][j-1] = 2
                if i+1 < n and j-1 >= 0 and board[i+1][j-1] == 0:
                    board[i+1][j-1] = 2
                if i+1 < n and j+1 < m and board[i+1][j+1] == 0:
                    board[i+1][j+1] = 2
                if i-1 >= 0 and j+1 < m and board[i-1][j+1] == 0:
                    board[i-1][j+1] = 2
    ans = 0
    for i in board:
        ans += i.count(0)
    return ans