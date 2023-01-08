import sys
input = sys.stdin.readline

def bfs() :
    while q :
        current = q.pop(0)
        cx, cy = current[0]
        
        if current not in path:
            path.append(current)
        
        #상
        if cy > 0:
            if maze[cy-1][cx] == 1:
                maze[cy-1][cx] = 0
                q.append([[cx, cy-1], current[0]])

        #하
        if cy < y-1:
            if maze[cy+1][cx] == 1:
                maze[cy+1][cx] = 0
                q.append([[cx, cy+1], current[0]])
                
        #좌
        if cx > 0:
            if maze[cy][cx-1] == 1:
                maze[cy][cx-1] = 0
                q.append([[cx-1, cy], current[0]])
                
        #우
        if cx < x-1:
            if maze[cy][cx+1] == 1:
                maze[cy][cx+1] = 0
                q.append([[cx+1, cy], current[0]])
        
        
y, x = list(map(int, input().rstrip().split()))
maze = []
q = []
visited = [[0 for _ in range(x)] for _ in range(y)]
path = []

for _ in range(y):
    line = list(map(int, input().rstrip()))
    maze.append(line)

q.append([[0,0]])

bfs()
path_ans = []

cur = 0
# 목표지 찾고, 이후 이동은 삭제
while cur == 0 :
    temp = path.pop()
    if temp[0] == [x-1, y-1]:
        cur = temp
        path_ans.append(cur[0])

# 현재(목표) 직전의 경로들을 찾아 리스트
while path:
    prev = path.pop()
    if cur[1] == prev[0]:
        path_ans.append(cur[1])
        cur = prev
        
# print(path_ans)
print(len(path_ans))
"""
4 6
101111
101010
101011
111011
"""