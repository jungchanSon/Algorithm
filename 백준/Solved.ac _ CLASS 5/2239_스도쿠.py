import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip().split())) for _ in range(9)]

def dfs(y, x):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                

dfs(0, 0)