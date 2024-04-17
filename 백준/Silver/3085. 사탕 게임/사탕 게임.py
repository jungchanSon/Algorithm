import sys
import copy
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
ans = 0

def check(b, i, j):
    t = b[i][j]
    ta1 = 0
    ta2 = 0
    for k in range(i-1, -1, -1):
        if b[k][j] == t:
            ta1 += 1
        else: break 
    for k in range(i, n):
        if b[k][j] == t:
            ta1 += 1
        else: break
        
    for k in range(j-1, -1, -1):
        if b[i][k] == t:
            ta2 += 1
        else: break
    for k in range(j, n):
        if b[i][k] == t:
            ta2 += 1
        else: break
    return max(ta1, ta2)

#행
for i in range(n):
    for j in range(n-1):
        ans = max(ans, check(board, i, j))
for i in range(n):
    for j in range(n-1):
        if board[i][j] == board[i][j+1]:
            continue
        tb = copy.deepcopy(board)
        temp = tb[i][j]
        tb[i][j] = tb[i][j+1]
        tb[i][j+1] = temp
        ans = max(ans, check(tb, i, j))
        ans = max(ans, check(tb, i, j+1))
# 열
for i in range(n):
    for j in range(n-1):
        if board[j][i] == board[j+1][i]:
            continue
        tb = copy.deepcopy(board)
        temp = tb[j][i]
        tb[j][i] = tb[j+1][i]
        tb[j+1][i] = temp

        ans = max(ans, check(tb, j, i))
        ans = max(ans, check(tb, j+1, i))
print(ans)
        