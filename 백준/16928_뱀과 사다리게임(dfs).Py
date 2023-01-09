import sys
input = sys.stdin.readline

#n: 사다리, m:뱀
n, m = list(map(int, input().rstrip().split()))

ledge = []
snake = []

for _ in range(n):
    x, y = list(map(int, input().rstrip().split()))
    ledge.append([x, y])
    
for _ in range(m):
    x, y = list(map(int, input().rstrip().split()))
    snake.append([x, y])

ans = []
ledgeSnake = ledge+snake
visited = [0 for _ in range(101)]

def dfs(n, diceCnt):
    if n >100 :
        return
    if n == 100:
        if visited[n]:
            visited[n] = min(visited[n], diceCnt)
            return
        else: 
            visited[n] = diceCnt
            return
    
    if visited[n]:
        if diceCnt < visited[n]:
            visited[n] = diceCnt     
        else:
            return        
    else : 
        visited[n] = diceCnt
    

    for i in range(1, 7):
        f = False
        for j in ledgeSnake:
            if n+i == j[0]:
                f = True
                dfs(j[1], diceCnt+1)
        if f == False:
            dfs(n+i, diceCnt+1)

dfs(1, 0)

print(visited[100])