import sys
input = sys.stdin.readline

def bfs():
    global dayCnt
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while q:
        current = q.pop(0)
        dayCnt += 1
        temp = [] 
        for i in current:
            cx, cy = i
        
            for i in range(4):
                nextX= cx+dx[i]
                nextY= cy+dy[i]
                
                #밖으로 나갈 경우
                if nextX < 0 or nextX >= x or nextY < 0 or nextY >= y :
                    continue
                
                #벽을 만날 경우
                if tomatoBoard[nextY][nextX] == -1 :
                    continue
                
                if tomatoBoard[nextY][nextX] == 0:
                    tomatoBoard[nextY][nextX] = 1
                    temp.append([nextX,nextY])
                    # q.append([nextX, nextY])
        if len(temp) > 0 :
            q.append(temp)
                
def checkRipeTomato():
    temp = []
    for i in range(len(tomatoBoard)):
        for j in range(len(tomatoBoard[0])):
            if tomatoBoard[i][j] == 1:
                temp.append([j, i])
    q.append(temp)
    
x, y = list(map(int, input().rstrip().split()))

tomatoBoard = []
dayCnt = 0
visited = []
q = []

for _ in range(y):
    line = list(map(int, input().rstrip().split()))
    tomatoBoard.append(line)
    
#익은 토마토 인덱스 저장, q에 삽입
checkRipeTomato()
bfs()

#모두 익히지 못하면 -1 출력
for i in tomatoBoard:
    if 0 in i:
        print(-1)
        quit()
print(dayCnt -1)