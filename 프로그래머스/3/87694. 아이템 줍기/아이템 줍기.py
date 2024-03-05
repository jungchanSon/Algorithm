def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    n = 51 * 2 
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    for rec in rectangle:
        fill(rec, board)
    
    dx = [0, 1 ,0 , -1] 
    dy = [-1, 0, 1, 0]
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            if board[i][j] != 0:
                continue
            if board[i-1][j-1] == -1 or board[i-1][j] == -1 or board[i-1][j+1] ==-1 or board[i][j+1] == -1 or board[i+1][j+1] == -1 or board[i+1][j] ==-1 or board[i+1][j-1] ==-1 or board[i][j-1] == -1:
                board[i][j] = 1 
    board[characterY][characterX] = 2
    
    q = [(characterX, characterY)]
    while q:
        cx, cy = q.pop(0)
    
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[ny][nx] != 1 :
                continue
            board[ny][nx] = board[cy][cx] +1
            q.append((nx, ny))
    
    # for i in board:
    #     print(*i)
        
    answer = board[itemY][itemX]//2 - 1
    return answer

def fill(l, b):
        x1, y1, x2, y2 = l
        x1 *= 2
        x2 *= 2
        y1 *= 2
        y2 *= 2
        
        for i in range(y1+1, y2):
            for j in range(x1+1, x2):
                b[i][j] = -1