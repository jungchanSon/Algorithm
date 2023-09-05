import sys
input = sys.stdin.readline

board = [list(map(int, input().rsplit())) for _ in range(9)]

def check_board(y, x):
    
    tmp = set([i for i in range(1, 10)])
    arr = set()
    
    for i in range(9):
        arr.add(board[y][i])
        arr.add(board[i][x])
        
    for i in range((y//3)*3, (y//3 + 1)*3):
        for j in range((x//3)*3, (x//3+1)*3):
            arr.add(board[i][j])
            
    return list(tmp - arr)    

def check_full():
    for i in board:
        if 0 in i:
            return False
    return True

def bt(d):
    if check_full(): 
        for i in board:
            print(*i)
        quit()
    
    i, j = empty[d]
    arr = check_board(i, j)
    for k in arr:
        board[i][j] = k
        bt(d+1)
        board[i][j] = 0
 
empty = []
for i in range(9): 
    for j in range(9):
        if not board[i][j]: 
            empty.append([i, j])     
empty_num = len(empty) 
bt(0)

"""
0 0 0 0 0 0 0 0 9
0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 1

1 1 1 1 1 1 1 1 9
1 1 1 1 1 1 1 1 8
1 1 1 1 1 1 1 1 7
1 1 1 1 1 1 1 1 6
1 1 1 1 1 1 1 1 5
1 1 1 1 1 1 1 1 4
1 1 1 1 1 1 1 1 3
1 1 1 1 1 1 1 1 2
1 1 1 1 1 1 1 1 1
"""