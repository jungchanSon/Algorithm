import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
N, M = map(int, input().rstrip().split())
board = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

while 1:
    q = deque()
    q.append((0,0))

    check = False
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for i in board:
        if sum(i) != 0:
            check =True
            break
        
    if not check:
        break
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if board[ny][nx]:
                if visited[ny][nx] == True or visited[ny][nx] == False:
                    visited[ny][nx] = 2
                else :
                    visited[ny][nx] +=1
                    
                if visited[ny][nx] >= 3:
                    board[ny][nx] = 0
                    check = True
                    continue
                
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))
                
    if not check:
        break
    
    cnt += 1 
    
print(cnt)