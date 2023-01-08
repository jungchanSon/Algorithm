import sys
input = sys.stdin.readline

testCount = int(input().rstrip())

def bfs() :
    
    while q:
        current = q.pop(0)
        cx, cy = current
        if current == end:
            break
        #상
        if cy-2 >= 0:
            #좌
            if cx-1 >= 0:
                if visited[cx-1][cy-2] == 0:
                    visited[cx-1][cy-2] = visited[cx][cy] + 1
                    q.append([cx-1, cy-2])
            #우
            if cx+1 < boardSize:
                if visited[cx+1][cy-2] == 0:
                    visited[cx+1][cy-2] = visited[cx][cy] + 1
                    q.append([cx+1, cy-2])

        #하
        if cy+2 < boardSize:
            #좌
            if cx-1 >= 0:
                if visited[cx-1][cy+2] == 0:
                    visited[cx-1][cy+2] = visited[cx][cy] + 1
                    q.append([cx-1, cy+2])
            #우
            if cx+1 < boardSize:
                if visited[cx+1][cy+2] == 0:
                    visited[cx+1][cy+2] = visited[cx][cy] + 1
                    q.append([cx+1, cy+2])

        #좌
        if cx-2 >= 0:
            #상
            if cy-1 >= 0:
                if visited[cx-2][cy-1] == 0:
                    visited[cx-2][cy-1] = visited[cx][cy] + 1
                    q.append([cx-2, cy-1])
            #하
            if cy+1 < boardSize:
                if visited[cx-2][cy+1] == 0:
                    visited[cx-2][cy+1] = visited[cx][cy] + 1
                    q.append([cx-2, cy+1])
        #우
        if cx+2 < boardSize:
            #상
            if cy-1 >= 0:
                if visited[cx+2][cy-1] == 0:
                    visited[cx+2][cy-1] = visited[cx][cy] + 1
                    q.append([cx+2, cy-1])
            #하
            if cy+1 < boardSize:
                if visited[cx+2][cy+1] == 0:
                    visited[cx+2][cy+1] = visited[cx][cy] + 1
                    q.append([cx+2, cy+1])
    
for _ in range(testCount):
    boardSize = int(input().rstrip())
    start = list(map(int, input().rstrip().split()))
    end = list(map(int, input().rstrip().split()))

    q = [start]
    cnt = 0
    visited = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
    visited[start[0]][start[1]] = 1
    bfs()
    
    print(visited[end[0]][end[1]] - 1)
"""
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
"""