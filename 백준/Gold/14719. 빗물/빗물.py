H, W = map(int, input().rsplit())
block_h = list(map(int, input().rsplit()))

board = [[False for _ in range(W)] for _ in range(H)]

for i in range(W):
    for j in range(block_h[i]):
        board[j][i] = True
board = board[::-1]       

ans = 0
for i in board:
    cur = False 
    temp_ans = 0
    for j in i:
        if cur == False and j == True:
            cur = True
        elif cur == True and j == False:
            temp_ans += 1
        elif cur == True and j == True:
            ans += temp_ans
            temp_ans = 0
        
print(ans)