n, m = map(int, input().rsplit())
board = [list(map(int, input().rsplit())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            cx, cy = j, i
            q.append([cx, cy, 1])
            
while q:
    cx, cy, dist = q.pop(0)
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if board[ny][nx] != 1 :
            visited[ny][nx] = 0
            continue
        if visited[ny][nx] != -1:
            continue
        visited[ny][nx] = dist
        q.append([nx, ny, dist+1])

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            visited[i][j] = 0

for i in visited:
    print(*i, end="\n")