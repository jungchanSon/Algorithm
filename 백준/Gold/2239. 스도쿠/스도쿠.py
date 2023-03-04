import sys
import copy
input = sys.stdin.readline
board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
empty_space = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty_space.append((i, j))

def check_row(cur, value):
    y, x = cur
    
    if value not in board[y]:
        return True
    else: 
        return False

def check_column(cur, value):
    y, x = cur
    
    for i in range(9):
        if board[i][x] == value:
            return False
    return True 

def check_area(cur, value):
    y, x = cur
    
    area_x = x // 3
    area_y = y // 3
    
    for i in range(area_y * 3, area_y * 3 + 3):
        for j in range(area_x * 3, area_x * 3 + 3):
            if board[i][j] == value:
                return False
    return True
ans = [] 
def dfs(depth):
    # global ans
    if depth >= len(empty_space):
        # ans = copy.deepcopy(board)
        for i in board:
            print(*i, sep="")
        quit()
    cy, cx = empty_space[depth]
    pos = empty_space[depth]
    for i in range(1, 10):
        if not check_column(pos, i) or not check_row(pos, i) or not check_area(pos, i):
            continue
        board[cy][cx] = i
        dfs(depth+1)
        board[cy][cx] = 0
        # print("    ", pos, i)
ans = dfs(0)
