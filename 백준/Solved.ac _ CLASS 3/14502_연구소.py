import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(copied_board):
    num_zero = 0
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if copied_board[i][j] == 2:
                q.append((i, j))
                
    while q:
        cy, cx = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if copied_board[ny][nx] == 1:
                continue
            
            if not visited[ny][nx]:     
                visited[ny][nx] = True
                copied_board[ny][nx] = 2
                q.append((ny, nx))
        
    for line in copied_board:
        num_zero += line.count(0)
    return num_zero

ans = 0
for i1 in range(N):
    for j1 in range(M):
        if board[i1][j1] == 0:
            board[i1][j1] = 1
            cnt += 1
            for i2 in range(i1, N):
                if i2 == i1:
                    j2_start = j1+1
                else:
                    j2_start = 0
                for j2 in range(j2_start, M):
                    if board[i2][j2] == 0:
                        board[i2][j2] = 1
                        cnt +=1
                        for i3 in range(i2, N):
                            if i3 == i2:
                                j3_start = j2+1
                            else:
                                j3_start = 0
                            for j3 in range(j3_start, M):
                                if board[i3][j3] == 0:
                                    board[i3][j3] = 1
                                    cnt += 1
                                    temp = bfs(copy.deepcopy(board))
                                    ans = max(ans, temp)
                                    board[i3][j3] = 0
                        board[i2][j2] = 0
            board[i1][j1] = 0
            
                                
print(ans)     
"""
1. 벽을 세움 64*63*62
2. 바이러스 증식 64
3. 남은 칸 계산 8
4. 모든 칸에 대해 탐색

"""