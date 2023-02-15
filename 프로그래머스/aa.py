from collections import deque

def solution(board, aloc, bloc):
    answer = -1
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    n = len(board)
    m = len(board[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    print(n)
    print(m)
    
    # q = deque()
    # q.append((aloc, bloc))
    
    # while q:
    #     a, b = q.popleft()
        
    #     for i in range(4):
    #         Any = a[0] + dy[i]
    #         Anx = a[1] + dx[i]
    #         for j in range(4):
    #             Bny = b[0] + dy[j]
    #             Bnx = b[1] + dx[j]    
                
    #             if Any >= 0 and Any < n and Anx >=0 and Anx <m:
    #                 if Bny >=0 and Bny < n and Bnx >=0 and Bnx <m:
    #                     if board[Any][Anx] == 1 and board[Bny][Bnx] == 1:
    #                         if Anx != Bnx and Any != Bny:
    #                             board[Any][Anx] = 0
    #                             board[Bny][Bnx] = 0
    #                             print(Any, Anx, Bny, Bnx)
    #                             q.append(([Any, Anx], [Bny, Bnx]))
    #                             answer+=1
    ans = []
    board[aloc[0]][aloc[1]] = 0
    board[bloc[0]][bloc[1]] = 0
    def dfs(a, b, cnt, turn):
        ans.append(cnt)
        
        moveA = False
        moveB = False
        if turn:
            for i in range(4):
                moveA = False
                ax = a[1] + dx[i]
                ay = a[0] + dy[i]
                if ay >= 0 and ay < n and ax >=0 and ax <m:
                    if board[ay][ax] == 1 :
                        if ax != b[1] and ay != b[0]:
                            moveA = True
                            board[ay][ax] = 0
                            dfs([ay, ax], b, cnt +1, not turn)
                            board[ay][ax] = 1
        else:
            for i in range(4):
                moveB = False
                bx = b[1] + dx[i]
                by = b[0] + dy[i]
                if by >= 0 and by < n and bx >=0 and bx < m:
                    if board[by][bx] == 1 :
                        if bx != a[1] and by != a[0]:
                            moveB = True
                            board[by][bx] = 0
                            dfs(a, [by, bx], cnt +1, not turn)
                            board[by][bx] = 1
            # for j in range(4):
            #     bx = b[1] + dx[j]
            #     by = b[0] + dy[j]
            #     if ay >= 0 and ay < n and ax >=0 and ax <m:
            #         canMoveA = True
            #         if by >=0 and by < n and bx >=0 and bx <m:
            #             canMoveB = True
            #             if board[ay][ax] == 1 and board[by][bx] == 1:
            #                 if ax != bx and by != ay:
            #                     board[ay][ax] = 0
            #                     board[by][bx] = 0
            #                     dfs([ay, ax], [by, bx], cnt)
            #                     board[ay][ax] = 1
            #                     board[by][bx] = 1
   
    dfs(aloc, bloc, 0, True)
    print(ans)
    answer = max(ans)
    return answer


t1 = [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]]
t2 = [[[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]	]
t3 = [[[1, 1, 1, 1, 1]], [0, 0], [0, 4]]
t4 = [[[1]], [0, 0], [0, 0]]

print(solution(t1[0],t1[1],t1[2]))
print(solution(t2[0],t2[1],t2[2]))
print(solution(t3[0],t3[1],t3[2]))
print(solution(t4[0],t4[1],t4[2]))