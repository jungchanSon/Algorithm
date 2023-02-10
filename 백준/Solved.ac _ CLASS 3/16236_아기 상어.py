import sys
import math
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
visited = [[False for _ in range(N)] for _ in range(N)]
shark = 0
for i in range(N):
    data = list(map(int, input().rstrip().split()))
    arr.append(data)
    if 9 in data:
        shark = (data.index(9), i)
        

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sharkSize = 2
sharkEating = 0
saveTime = 0
arr[shark[1]][shark[0]] = 0

check = False
minX = 22
minY = 22
minTime = 22
def bfs():
    global minX, minY, minTime, check

    while q:
        cx, cy, time = q.popleft()
        if visited[cy][cx]:
            continue
        else :
            visited[cy][cx] = time

        for i in range(4):
            nx = cx +dx[i]
            ny = cy +dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if arr[ny][nx] > sharkSize: 
                continue
            
            if arr[ny][nx] and time <= minTime and arr[ny][nx] < sharkSize:
                check = True
                if  ny < minY :
                    minY = ny
                    minX = nx
                    minTime = time
                elif ny == minY and nx < minX:
                    minY = ny
                    minX = nx
                    minTime = time
                    
            q.append((nx,ny, time+1))

q = deque()
q.append((shark[0], shark[1], 1))

while True:
    check = False
    visited = [[0 for _ in range(N)] for _ in range(N)]
    minX = 22
    minY = 22
    minTime = 22
  
    bfs()
    if not check:
        break
   
    saveTime += visited[minY][minX] -1
    arr[minY][minX] = 0
   
    sharkEating += 1
    
    if sharkEating == sharkSize : 
        sharkSize += 1
        sharkEating = 0
        
    q.append((minX, minY, 1))
    
print(saveTime)