import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []

max_n = 0
min_n = 101

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(n):
    data = list(map(int,input().rsplit()))
    max_n = max(max_n, max(data))
    min_n = min(min_n, min(data))
    board.append(data)
    
ans = 0
for k in range(min_n-1, max_n+1):
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    check_list = []
    cur_ans = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] > k:
                temp_board[i][j] = 1
                check_list.append([i, j])

    q = deque()
    for i in range(n): 
        for j in range(n):
            if temp_board[i][j] == 0: 
                continue
            q.append([i, j])
            cur_ans += 1 
            while q: 
                cy, cx = q.popleft()
                temp_board[cy][cx] = 0
                
                for d in range(4): 
                    nx = cx + dx[d]
                    ny = cy + dy[d]

                    if nx < 0 or nx >= n: 
                        continue
                    if ny < 0 or ny >= n: 
                        continue
                    if temp_board[ny][nx] == 0: 
                        continue
                    temp_board[ny][nx] = 0
                    q.append([ny, nx])
    
    ans = max(ans, cur_ans)
print(ans)