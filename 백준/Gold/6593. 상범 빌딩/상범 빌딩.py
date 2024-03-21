import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while 1:
    q = []
    goal = []
    L, R, C = map(int, input().rsplit())
    if L == 0 and R == 0 and C == 0:
        break
    buildings = []
    for _ in range(L):
        b = [list(input().rstrip()) for _ in range(R)]
        input()
        buildings.append(b)
    
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if buildings[i][j][k] == "S":
                    q.append((k, j, i, 0))
                if buildings[i][j][k] == "E":
                    goal = [k, j, i]
    
    while q:
        cx, cy, cz, depth = q.pop(0)
        
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i] 
            nz = cz + dz[i]
            
            if nx < 0 or nx >= C or ny < 0 or ny >= R or nz < 0 or nz >= L:
                continue
            
            if buildings[nz][ny][nx] == '.' or buildings[nz][ny][nx] == 'E' :
                buildings[nz][ny][nx] = depth+ 1
                q.append((nx, ny, nz, depth+1))
    ans = buildings[goal[2]][goal[1]][goal[0]]  
    if ans == "E":
        print("Trapped!")
    else:
        print("Escaped in "+str(ans)+" minute(s).")