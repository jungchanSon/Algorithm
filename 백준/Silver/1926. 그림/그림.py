import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rsplit())) for _ in range(n)]

ans_1 = 0
ans_2 = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j]:
            q = deque([[i, j]])
            board[i][j] = 0
            temp = 0
            while q:
                cy, cx = q.popleft()
                temp += 1
                for k in range(4):
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or board[ny][nx] == 0:
                        continue
                    
                    board[ny][nx] = 0
                    q.append([ny, nx])
                    
            ans_1 += 1
            ans_2 = max(ans_2, temp)

print(ans_1)
print(ans_2)