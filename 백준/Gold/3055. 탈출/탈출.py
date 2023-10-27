import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().rsplit())
board = [list(input().rstrip()) for _ in range(r)]
water_pos = deque()
start = deque()
end = []
visited = [[False for _ in range(c)] for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(r):
    for j in range(c):
        if board[i][j] == "*":
            water_pos.append([i, j])
        if board[i][j] == "S":
            visited[i][j] = True
            start.append([i, j, 0])
        if board[i][j] == "D":
            end.append([i, j])


while water_pos or start:
    temp = deque()
    while water_pos:
        wy, wx = water_pos.popleft()
        for i in range(4):
            nwx, nwy = wx+dx[i], wy+dy[i]
            if nwx < 0 or nwx >= c or nwy < 0 or nwy >= r:
                continue
            if board[nwy][nwx] == "*" or board[nwy][nwx] == "X" or board[nwy][nwx] == "D":
                continue
            board[nwy][nwx] = "*"
            temp.append([nwy, nwx])
    water_pos = temp
    
    temp = deque()
    while start:
        sy, sx, cnt= start.popleft()
        for i in range(4):
            nsx, nsy = sx+dx[i], sy+dy[i]
            if nsx < 0 or nsx >= c or nsy < 0 or nsy >= r:
                continue
            if board[nsy][nsx] == "*" or board[nsy][nsx] == "X":
                continue
            if board[nsy][nsx] == "D":
                print(cnt+1)
                quit()
            if not visited[nsy][nsx]: 
                visited[nsy][nsx] = True
                temp.append([nsy, nsx, cnt+1])
                # print('----------------')
                # print(sx, sy, nsx, nsy)
                # for i in board:
                #     print(*i)
                # print('----------------')
    start = temp
            
            

print("KAKTUS")