import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
board = []
check_alpha = [False for _ in range(30)]
for i in range(R):
    board.append(list(input().rstrip()))
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 1

def dfs(pos, cnt):
    global ans
    cy, cx = pos
    
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if nx < 0 or nx >=C or ny < 0 or ny >= R:
            continue
        
        next_alpha = board[ny][nx]
        if not visited[ny][nx] and not check_alpha[ord(next_alpha)-65] :
            visited[ny][nx] = True
            check_alpha[ord(next_alpha)-65] = True
            ans = max(ans, cnt+1)
            dfs((ny, nx), cnt + 1)
            check_alpha[ord(next_alpha)-65] = False
            visited[ny][nx] = False

        
visited = [[False for _ in range(C)] for _ in range(R)]
check_alpha[ord(board[0][0])-65] = True
dfs((0,0), 1)
print(ans)