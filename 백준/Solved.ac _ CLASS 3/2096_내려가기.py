#메모리 초과
# import sys
# input = sys.stdin.readline

# N = int(input())
# board = []
# dp = [[[0,0], [0,0], [0,0]] for _ in range(N)]
# for _ in range(N):
#     board.append(list(map(int, input().rstrip().split())))

# if N == 1:
#     print(max(board[0][0], board[0][1], board[0][2]), min(board[0][0], board[0][1], board[0][2]))
#     quit()
    
# for i in range(3):
#     dp[0][i][0] = board[0][i]
#     dp[0][i][1] = board[0][i]
    
# for i in range(1, N):
#     dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][1]) + board[i][0]
#     dp[i][1][1] = max(dp[i-1][0][1], dp[i-1][1][1], dp[i-1][2][1]) + board[i][1]
#     dp[i][2][1] = max(dp[i-1][1][1], dp[i-1][2][1]) + board[i][2]
    
#     dp[i][0][0] = min(dp[i-1][0][0], dp[i-1][1][0]) + board[i][0]
#     dp[i][1][0] = min(dp[i-1][0][0], dp[i-1][1][0], dp[i-1][2][0]) + board[i][1]
#     dp[i][2][0] = min(dp[i-1][1][0], dp[i-1][2][0]) + board[i][2]
    
# print(max(dp[-1][0][1], dp[-1][1][1], dp[-1][2][1]), min(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0]))

import sys
input = sys.stdin.readline

N = int(input())
board = []

minList = [0, 0, 0]
maxList = [0, 0, 0]
for i in range(N):
    a, b, c = map(int, input().rstrip().split())
    if i == 0:
        minList[0] = a
        maxList[0] = a
        
        minList[1] = b
        maxList[1] = b
        
        minList[2] = c
        maxList[2] = c
    else:
        minA = min(minList[0],minList[1]) + a
        minB = min(minList[0],minList[1],minList[2]) + b
        minC = min(minList[1],minList[2]) + c
        
        maxA = max(maxList[0],maxList[1]) + a
        maxB = max(maxList[0],maxList[1],maxList[2]) + b
        maxC = max(maxList[1],maxList[2]) + c
        
        minList = [minA, minB, minC]
        maxList = [maxA, maxB, maxC]

print(max(maxList), min(minList))