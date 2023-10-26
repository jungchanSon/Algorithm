import sys
from collections import deque
import copy
input = sys.stdin.readline

ans = 0
n, m = map(int, input().rsplit())
board = [list(map(int, input().rsplit())) for _ in range(n)]

arr = []
for i in range(n):
    for j in range(m):
        if board[i][j] >= 1 and board[i][j] <= 5:
            arr.append([i, j, board[i][j]])

def is_wall(b, a):
    if board[a][b] == 6:
        return True
    else:
        return False

def top(b, a, cb):
    for i in range(a, -1, -1):
        if is_wall(b, i):
            break
        else:
            cb[i][b] = "#"
            
def bottom(b, a, cb):
    for i in range(a, n):
        if is_wall(b, i):
            break
        else:
            cb[i][b] = "#"
    
def left(b, a, cb):
    for i in range(b, -1, -1):
        if is_wall(i, a):
            break
        else:
            cb[a][i] = "#"
    
def right(b, a, cb):
    for i in range(b, m):
        if is_wall(i, a):
            break
        else:
            cb[a][i] = "#"
ans = 1e9
def dfs(cur, board: list):
    global ans
    if cur == len(arr):
        temp = 0
        for i in board:
            temp += i.count(0)
        ans = min(ans, temp)
        return
    y, x, t = arr[cur]
    if t == 1:
        b = copy.deepcopy(board)
        top(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        bottom(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        left(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        right(x, y, b)
        dfs(cur+1, b)
        
    elif t == 2:
        b = copy.deepcopy(board)
        bottom(x, y, b)
        top(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        right(x, y, b)
        left(x, y, b)
        dfs(cur+1, b)
    elif t == 3:
        b = copy.deepcopy(board)
        top(x, y, b)
        right(x,y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        right(x,y, b)
        bottom(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        bottom(x, y, b)
        left(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        left(x, y, b)
        top(x,y, b)
        dfs(cur+1, b)
    elif t == 4:
        b = copy.deepcopy(board)
        left(x, y, b)
        top(x, y, b)
        right(x,y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        top(x, y, b)
        right(x,y, b)
        bottom(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        right(x,y, b)
        bottom(x, y, b)
        left(x, y, b)
        dfs(cur+1, b)
        b = copy.deepcopy(board)
        left(x, y, b)
        bottom(x, y, b)
        top(x,y, b)
        dfs(cur+1, b)
    else:
        b = copy.deepcopy(board)
        left(x,y, b)
        bottom(x,y, b)
        top(x,y, b)
        right(x, y, b)
        dfs(cur+1, b)
        
if arr:
    dfs(0, board)
else:
    ans = 0
    for i in board:
        ans += i.count(0)
print(ans)