import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000) 

y, x = list(map(int, input().rstrip().split()))
board = []
for _ in range(y):
    line = list(map(int, input().rstrip()))
    board.append(line)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] 
visited = [[[0 for _ in range(2)] for _ in range(x)] for _ in range(y)]
ans = []
q = deque()
def bfs():
    while q:
        current = q.popleft()
        cx, cy, cw = current
        if cx == x-1 and cy == y-1 :
            print(visited[cy][cx][cw] + 1)
            return
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= 0 and nx < x and ny >=0 and ny < y:
                if board[ny][nx] == 1 and cw == 0:
                    q.append([nx, ny, 1])
                    visited[ny][nx][1] = visited[cy][cx][0] + 1
                elif board[ny][nx] == 0 :
                    if visited[ny][nx][cw] == 0:
                        visited[ny][nx][cw] = visited[cy][cx][cw] + 1
                        q.append([nx, ny, cw])

    print(-1)
    
q.append([0,0, 0])
bfs()