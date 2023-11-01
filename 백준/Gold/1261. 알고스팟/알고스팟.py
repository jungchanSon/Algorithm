import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rsplit())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()
q.append([0,0])
tempq = deque()
visited[0][0] = True
cnt = 0
while q:
    cx, cy = q.popleft()
    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        
        if visited[ny][nx]:
            continue
        if board[ny][nx] > 0 :
            tempq.append([nx, ny])
            visited[ny][nx] = True
        else :  
            visited[ny][nx] = True
            board[ny][nx] = cnt
            q.append([nx, ny])
            
    if not q:
        q = tempq.copy()
        tempq = deque()
        cnt += 1 

print(board[n-1][m-1])