import copy
h, w, n = map(int, input().rsplit())

board = [list(map(int, input().rsplit())) for _ in range(h)]

    
for _ in range(n):
    depth = 0
    temp_board = [[0 for _ in range(w)] for _ in range(h)]
    
    while depth < min(h//2, w//2):
        
        for i in range(depth, w-1-depth):
            temp_board[depth][i] = board[depth][i+1]
        for i in range(depth, h-1-depth):
            temp_board[i][w-depth-1] = board[i+1][w-depth-1]
        for i in range(w-1-depth, depth, -1):
            temp_board[h-1-depth][i] = board[h-1-depth][i-1]
        for i in range(h-1-depth, depth, -1):
            temp_board[i][depth] = board[i-1][depth]
        
        depth +=1
    board = temp_board.copy()
for i in board:
    print(*i)
        