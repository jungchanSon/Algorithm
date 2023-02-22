import sys
from itertools import combinations
from collections import deque
import math

input = sys.stdin.readline

N , M = map(int, input().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# for i in board:
#     print(i)

chicken_house = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken_house.append((i, j)) 
        elif board[i][j] == 1:
            house.append((i, j))
            
# print(chicken_house)
chick_house_combi = list(combinations(chicken_house, M))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 시간 초과
# def bfs(p, b):
#     q = deque()
#     q.append(p)
    
#     while q:
#         cy, cx, cnt = q.popleft()
#         for chick_position in b:
#             if cy == chick_position[0] and cx == chick_position[1]:
#                 return cnt
#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]
            
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue           
            
#             q.append((ny, nx, cnt+1))

ans = math.inf 
    
for combi in chick_house_combi:
    temp = 0
    for h in house:
        y, x = h
        min_num = math.inf
        for chick_p in combi:
            dist = abs(y-chick_p[0]) + abs(x-chick_p[1])
            min_num = min(min_num, dist)
        temp += min_num
    ans = min(ans, temp)
print(ans)