from collections import deque

def solution(board):
    answer = 0
    q = deque()
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    q.append([(0,0),(0,1)])
    visited = [[(0, 0) for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in visited:
        print(i)
    print()
    for i in board:
        print(i)
    print()
    
    while q:
        a, b = q.popleft()
        print(a,b)
        
        if visited[a[0]][a[1]][0]:
            print(0)
            continue
        
        for i in range(4):
            na = (a[0]+dy[i], a[1]+dx[i])
            nb = (b[0]+dy[i], b[1]+dx[i])
            if na[0] <0 or na[0] >= len(board) or na[1] < 0 or na[1] >= len(board[0]):
                print(1)
                continue
            if nb[0] <0 or nb[0] >= len(board) or nb[1] < 0 or nb[1] >= len(board[0]):
                print(2)
                continue
            if board[na[0]][na[1]] or board[nb[0]][nb[1]]:
                print(3)
                continue
            visited[na[0]][na[1]][0] = True
            q.append((na, nb))
    print(q)
    for i in visited:
        print(i)
    print()
    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
solution(board)