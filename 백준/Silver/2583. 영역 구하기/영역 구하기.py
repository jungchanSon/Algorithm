import sys
input = sys.stdin.readline

M, N, K = map(int, input().rsplit())
arr = []
board = [[0 for _ in range(N)] for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().rsplit())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1
ans = []
for i in range(M):
    for j in range(N):
        if not board[i][j]:
            q = [(i, j)]
            temp = 1
            board[i][j] = 1
            while q:
                cy, cx = q.pop(0)
                
                for k in range(4):
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    
                    if not board[ny][nx]:
                        q.append((ny, nx))
                        board[ny][nx] = 1
                        temp += 1
            ans.append(temp)
ans.sort()
print(len(ans))
print(*ans)