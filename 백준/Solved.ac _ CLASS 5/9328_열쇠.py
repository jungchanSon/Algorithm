import sys
import copy
from collections import deque
input = sys.stdin.readline
T = int(input())

def use_key(key, board):
    check_use = False
    while key:
        cur_key = key.pop()
        upper_case_key = chr(ord(cur_key)-32)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == upper_case_key:
                    board[i][j] = "."
                    check_use = True
    
    return check_use

def collect_key(key, board, start_pos):
    check_collect = False
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    while start_pos:
        cx, cy = start_pos.popleft()
        if visited[cy][cx] :
            continue
        visited[cy][cx] = True
        
        if ord(board[cy][cx]) >= ord("a") and ord(board[cy][cx]) <= ord("z"):
            key.append(board[cy][cx])
            board[cy][cx] = "."
            check_collect = True
                
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board):
                continue

            if board[ny][nx] == "." or board[ny][nx] == "$" or (ord(board[ny][nx]) >= ord("a") and ord(board[ny][nx]) <= ord("z")):
                start_pos.append([nx, ny])
                
    return check_collect

def check_document(board, start_pos):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    ans = 0
    while start_pos:
        cx, cy = start_pos.popleft()
        if visited[cy][cx]:
            continue
        if board[cy][cx] == "$":
            ans += 1
        visited[cy][cx] = True
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board):
                continue
            if board[ny][nx] == "." or board[ny][nx] == "$":
                start_pos.append([nx, ny])
                
    return ans
answer = []
for _ in range(T):
    board = []
    H, W = map(int, input().rstrip().split())
    for _ in range(H):
        board.append(list(input().rstrip()))
    
    key = list(input().rstrip())
    start_q = deque()
    
            
    if key[0] != "0":
        while True:
            for i in range(W):
                if board[0][i] == "$" or board[0][i] == "." or (ord(board[0][i]) >= ord("a") and ord(board[0][i]) <= ord("z")):
                    start_q.append([i, 0])
                if board[H-1][i] == "$" or board[H-1][i] == "." or (ord(board[H-1][i]) >= ord("a") and ord(board[H-1][i]) <= ord("z")):
                    start_q.append([i, H-1])
            for i in range(1, H-1):
                if board[i][0] =="$" or board[i][0] == "." or (ord(board[i][0]) >= ord("a") and ord(board[i][0]) <= ord("z")):
                    start_q.append([0, i])
                if board[i][W-1] =="$" or board[i][W-1] == "." or (ord(board[i][W-1]) >= ord("a") and ord(board[i][W-1]) <= ord("z")):
                    start_q.append([W-1, i ])
            check_use = use_key(key, board)
            check_collect = collect_key(key, board, copy.deepcopy(start_q))
            if not check_collect and not check_use:
                break
    else:
        while True:
            for i in range(W):
                if board[0][i] == "$" or board[0][i] == "." or (ord(board[0][i]) >= ord("a") and ord(board[0][i]) <= ord("z")):
                    start_q.append([i, 0])
                if board[H-1][i] == "$" or board[H-1][i] == "." or (ord(board[H-1][i]) >= ord("a") and ord(board[H-1][i]) <= ord("z")):
                    start_q.append([i, H-1])
            for i in range(1, H-1):
                if board[i][0] == "$" or board[i][0] == "." or (ord(board[i][0]) >= ord("a") and ord(board[i][0]) <= ord("z")):
                    start_q.append([0, i])
                if board[i][W-1] == "$" or board[i][W-1] == "." or (ord(board[i][W-1]) >= ord("a") and ord(board[i][W-1]) <= ord("z")):
                    start_q.append([W-1, i ])
                    
            check_collect = collect_key(key, board, copy.deepcopy(start_q))
            check_use = use_key(key, board)
            if not check_use and not check_collect:
                break
    answer.append(check_document(board, copy.deepcopy(start_q)))

for i in answer:
    print(i)
"""
6
3 100
****************************************************************************************************
A$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*a
****************************************************************************************************
0
4 5
*A***
*$*a.
**$**
**A**
0
3 4
****
*$A*
****
a
5 5
***b*
***A*
***$*
.a***
*****
0
2 2
$$
$$
0
3 54
******************************************************
AbCdEfGhIjKlMnOpQrStUvWxYz*$ZyXwVuTsRqPoNmLkJiHgFeDcBa
******************************************************
0
"""