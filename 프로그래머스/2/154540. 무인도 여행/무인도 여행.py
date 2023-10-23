def solution(maps):
    answer = []
    board = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for line in maps:
        board.append(list(line))
    
    def bfs(y, x):
        q = [(y, x)]
        score = 0
        while q:
            cy, cx = q.pop(0)
            if not board[cy][cx].isnumeric():
                continue
            score += int(board[cy][cx])
            board[cy][cx] = 'X'
            
            for i in range(4):
                nx = dx[i] + cx
                ny = dy[i] + cy
                
                if nx < 0 or nx>=len(board[0]):
                    continue
                if ny < 0 or ny>=len(board):
                    continue
                
                if board[ny][nx].isnumeric():
                    q.append((ny, nx))
        return score
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j].isnumeric():
                score = bfs(i, j)
                if score:
                    answer.append(score)
    if not answer:
        answer.append(-1) 
    answer.sort()
    return answer