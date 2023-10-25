import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rsplit())
board = [list(input().rstrip()) for _ in range(n)]
vis = [[False for _ in range(m)] for _ in range(n)]
vis_f = [[False for _ in range(m)] for _ in range(n)]

check = True
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
jq = deque()
fq = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == "J":
            jq = deque([[i, j, 0]])
            vis[i][j] = 0
        if board[i][j] == "F":
            fq.append([i, j, 0])
            vis_f[i][j] = 0

while fq:
    cy, cx, t = fq.popleft()
    
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if nx < 0 or nx >= m:
            continue
        if ny < 0 or ny >= n:
            continue
        if board[ny][nx] == "#" or board[ny][nx] == "F":
            continue
        if vis_f[ny][nx]: 
            continue
        vis_f[ny][nx] = t+1
        fq.append([ny, nx, t+1])

while jq:
    cy, cx, t = jq.popleft()
    if cy == 0 or cy == n-1 or cx == 0 or cx == m-1:
        print(t+1)
        check = False
        break    
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= m:
            continue
        if ny < 0 or ny >= n:
            continue
        if board[ny][nx] == "#" or board[ny][nx] == "F":
            continue
        if vis[ny][nx]: 
            continue
        if not vis_f[ny][nx] or vis_f[ny][nx] > t+1:
            vis[ny][nx] = t+1
            jq.append([ny, nx, t+1])
if check:
    print("IMPOSSIBLE")
    