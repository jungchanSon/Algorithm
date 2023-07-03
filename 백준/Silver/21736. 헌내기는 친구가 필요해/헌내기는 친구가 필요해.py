n, m = map(int ,input().rsplit())

board = [list(input()) for _ in range(n)]
cur_x = 0
cur_y = 0
q = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            q.append([i, j])      
            break
    if board[i][j] == 'I':
            break

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans= 0
while q:
    cur_y, cur_x = q.pop()
    
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx < 0 or nx >= m:
            continue
        if ny < 0 or ny >= n:
            continue
        
        if board[ny][nx] != 'X':
            if board[ny][nx] == 'P':
                ans += 1
            q.append([ny, nx])
            board[ny][nx] = 'X'

if ans:
    print(ans)
else:
    print("TT")