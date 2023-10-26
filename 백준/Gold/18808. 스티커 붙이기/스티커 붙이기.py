import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m, k = map(int, input().rsplit())
board = [[0 for _ in range(m)] for _ in range(n)]

#    # # 
#    . #   . . #
#    . #   # # #  
def ro(old: list):
    old_n, old_m = len(old), len(old[0])
    new = [[0 for _ in range(old_n)] for _ in range(old_m)]
    
    for i in range(old_n):
        for j in range(old_m):
            new[j][old_n-i-1] = old[i][j]
    new_n, new_m = len(new), len(new[0])
    return new, new_n, new_m
for _ in range(k):
    nn, mm = map(int,input().rsplit())
    sticker = [list(map(int, input().rsplit())) for _ in range(nn)]
    for i in range(4):
        if i != 0:
            sticker, nn, mm = ro(sticker)
        df = False
        for i in range(n-nn+1):
            ff = False
            for j in range(m-mm+1):
                f = True
                for ii in range(nn):
                    fff = False
                    for jj in range(mm):
                        if sticker[ii][jj] == 1 and board[i+ii][j+jj] == 1:
                            f = False
                            fff = True
                            break
                    if fff:
                        break
                if f:
                    for y in range(i, i+nn):
                        for x in range(j, j+mm):
                            if sticker[y-i][x-j] == 1:
                                board[y][x] = 1
                    ff = True
                    df = True
                    break
            if ff:
                break
        if df:
            break
        

ans = 0
for i in board:
    ans += i.count(1)
print(ans)