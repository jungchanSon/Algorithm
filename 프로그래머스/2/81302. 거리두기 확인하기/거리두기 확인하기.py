from collections import deque;

def solution(places):
    answer = [1 for _ in range(len(places))]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    def calc(t1:list, t2:list):
        return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])
    
    for idx in range(len(places)):
        place = places[idx]
        n, m = 5, 5
        for i in range(n):
            for j in range(m):
                if place[i][j] == "P" and answer[idx] == 1:
                    visited = [[False for _ in range(m)] for _ in range(n)]
                    q = deque([(i, j)])
                    visited[i][j] = True
                    by, bx = i, j
                    while q:
                        cy, cx = q.popleft()
                        
                        for d in range(4):
                            nx = cx + dx[d]
                            ny = cy + dy[d]
                            if calc([by,bx], [ny, nx]) > 2 :
                                continue
                            if nx < 0 or nx >= m:
                                continue
                            if ny < 0 or ny >= n:
                                continue
                            if place[ny][nx] == "X":
                                continue
                            if visited[ny][nx]:
                                continue
                            if place[ny][nx] == "P":
                                answer[idx] = 0
                                break
                            visited[ny][nx] = True
                            q.append([ny, nx])
                        
                    
    return answer