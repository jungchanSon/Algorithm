import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().rsplit())) for _ in range(n)]

def t(board: list):
    # merge
    for i in range(n):
        for j in range(n):
            if board[j][i] == 0:
                continue
            for k in range(j+1, n):
                if board[k][i] == 0:
                    continue
                if board[j][i] == board[k][i]:
                    board[j][i] += board[k][i]
                    board[k][i] = 0
                    break
                else:
                    break

    for i in range(n):
        for j in range(n):
            if board[j][i] == 0:
                for k in range(j+1, n):
                    if board[k][i] != 0:
                        board[j][i] = board[k][i]
                        board[k][i] = 0
                        break
                        
    return board
def b(board: list):
    # merge
    for i in range(n):
        for j in range(n-1, -1, -1):
            if board[j][i] == 0:
                continue
            for k in range(j-1, -1, -1):
                if board[k][i] == 0:
                    continue
                if board[j][i] == board[k][i]:
                    board[j][i] += board[k][i]
                    board[k][i] = 0
                    break
                else:
                    break

    for i in range(n):
        for j in range(n-1, -1, -1):
            if board[j][i] == 0:
                for k in range(j-1, -1, -1):
                    if board[k][i] != 0:
                        board[j][i] = board[k][i]
                        board[k][i] = 0
                        break
    return board
                        

def l(board: list):
    # merge
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue
            for k in range(j+1, n):
                if board[i][k] == 0:
                    continue
                if board[i][j] == board[i][k]:
                    board[i][j] += board[i][k]
                    board[i][k] = 0
                    break
                else:
                    break

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                for k in range(j+1, n):
                    if board[i][k] != 0:
                        board[i][j] = board[i][k]
                        board[i][k] = 0
                        break
    return board

def r(board: list):
    # merge
    for i in range(n):
        for j in range(n-1, -1, -1):
            if board[i][j] == 0:
                continue
            for k in range(j-1, -1, -1):
                if board[i][k] == 0:
                    continue
                if board[i][j] == board[i][k]:
                    board[i][j] += board[i][k]
                    board[i][k] = 0
                    break
                else:
                    break

    for i in range(n):
        for j in range(n-1, -1, -1):
            if board[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if board[i][k] != 0:
                        board[i][j] = board[i][k]
                        board[i][k] = 0
                        break
                        
    return board
    
ans = 0 
def dfs(board: list, depth : int):
    global ans
    if depth == 5:
        for i in board:
            ans = max(ans, max(i))
        return

    temp_board = copy.deepcopy(board)
    res_board = t(temp_board)
    dfs(res_board, depth+1)
    
    temp_board = copy.deepcopy(board)
    res_board = b(temp_board)
    dfs(res_board, depth+1)
    
    temp_board = copy.deepcopy(board)
    res_board = l(temp_board)
    dfs(res_board, depth+1)
    
    temp_board = copy.deepcopy(board)
    res_board = r(temp_board)
    dfs(res_board, depth+1)
    
    
dfs(board, 0)

print(ans)