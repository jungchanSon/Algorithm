import sys
import math
from collections import deque 

input = sys.stdin.readline
R, C, T = map(int, input().rstrip().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().rstrip().split())))


air_cleaner_pos = []
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            air_cleaner_pos.append((i, j))
board2 = [[0 for _ in range(C)] for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def one_time(prev_board, target_board):
    for i in range(R):
        for j in range(C):
            if prev_board[i][j] == -1:
                target_board[i][j] = -1
                continue
            if prev_board[i][j]:
                unit = math.floor(prev_board[i][j] / 5)
                cnt = 0
                for d in range(4):
                    nx = j + dx[d]
                    ny = i + dy[d]
                    if nx < 0 or ny < 0 or nx >= C or ny >= R:
                        continue
                    if prev_board[ny][nx] == -1:
                        continue
                    cnt += 1
                    target_board[ny][nx] += unit
                target_board[i][j] += math.ceil(prev_board[i][j] - unit*cnt)

    prev = 0
    temp = target_board[air_cleaner_pos[0][0]]
    temp = deque(temp[1:])
    prev = temp.pop()
    temp.appendleft( 0)
    temp.appendleft(-1)
    target_board[air_cleaner_pos[0][0]] = list(temp)
    next_num = 0
    for i in range(air_cleaner_pos[0][0]-1, -1, -1):
        next_num = target_board[i][C-1]
        target_board[i][C-1] = prev
        prev = next_num

    temp = deque(target_board[0])
    a = temp.pop()
    temp.append(prev)
    temp.append(a)
    prev = temp.popleft()
    target_board[0] = list(temp) 
    

    for i in range(1, air_cleaner_pos[0][0]):
        next_num = target_board[i][0]
        target_board[i][0] = prev
        prev = next_num  

    # print()
    # for j in target_board:
    #     print(j)
    # print()

    prev = 0
    temp2 = target_board[air_cleaner_pos[1][0]]
    temp2 = deque(temp2[1:])
    prev = temp2.pop()
    temp2.appendleft( 0)
    temp2.appendleft(-1)
    target_board[air_cleaner_pos[1][0]] = list(temp2)

    next_num = 0
    for i in range(air_cleaner_pos[1][0]+1, R):
        next_num = target_board[i][C-1]
        target_board[i][C-1] = prev
        prev = next_num

    temp2 = deque(target_board[R-1])
    a = temp2.pop()
    temp2.append(prev)
    temp2.append(a)
    prev = temp2.popleft()
    target_board[R-1] = list(temp2)

    for i in range(R-2 , air_cleaner_pos[1][0], -1):
        next_num = target_board[i][0]
        target_board[i][0] = prev
        prev = next_num  


ans = 0
aa = 0
bb = 0

for i in range(T):
    if i % 2 == 0:
        board2 = [[0 for _ in range(C)] for _ in range(R)]        
        one_time(board, board2)
        if i == T-1:
            for j in board2:
                ans += sum(j)
                
            # for z in board2:
            #     print(z)
    else :
        board = [[0 for _ in range(C)] for _ in range(R)]
        one_time(board2, board)
        if i == T-1:
            for j in board:
                ans += sum(j)
            
            # for z in board:
            #     print(z)
print(ans+2)