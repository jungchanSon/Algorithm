import sys
import math
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
visited = [[False for _ in range(N)] for _ in range(N)]
shark = 0
for i in range(N):
    data = list(map(int, input().rstrip().split()))
    arr.append(data)
    if 9 in data:
        shark = (data.index(9), i)
        

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sharkSize = 2
sharkEating = 0
saveTime = 0
print(shark)
arr[shark[1]][shark[0]] = 0
temp = []

minX, minY, minTime = 0, 0, 0

def bfs():
    global minX, minY, minTime
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
            
            if arr[cy][cx] < sharkSize:
                if minTime == time:
                    if cy < minY:
                        minY = cy
                    elif cy == minY and cx < minX:
                        minX = cx
                else :
                    minX = cx
                    minY = cy
                    minTime = time
            
            q.append((nx,ny, time+1))

print(saveTime)

for i in visited:
    print(i)

q = deque()
q.append((shark[0], shark[1], 1))
cnt = 0
while True:
    if cnt > len(arr) ** 2:
        break
    bfs()
    saveTime += minTime # -1
    arr[minY][minX] = 0
    
    sharkEating += 1
    
    if sharkEating == sharkSize : 
        sharkSize += 1
        sharkEating = 0
        
    q.append((minX, minY, saveTime))
    cnt += 1 
    
print(saveTime)