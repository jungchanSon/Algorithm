from math import inf

def solution(board):
    answer = -1
    for i in range(len(board)):
        board[i] = list(board[i])
    pos = [0, 0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                pos = [i, j, 0]
    visited = [[inf for _ in range(len(board[0]))] for _ in range(len(board))]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = [pos]
    
    while q:
        cy, cx, d = q.pop(0)
        if board[cy][cx] == "G":
            answer = visited[cy][cx]
        for i in range(4):
            ny = cy
            nx = cx
            while 1:
                if ny+dy[i] < 0 or ny+dy[i] >= len(board) or nx+dx[i] < 0 or nx+dx[i] >= len(board[0]):
                    break
                if board[ny+dy[i]][nx+dx[i]] == "D":
                    break
                ny += dy[i]
                nx += dx[i]
            if visited[ny][nx] > d+1:
                visited[ny][nx] = d+1
                q.append([ny , nx, d+1])
    return answer