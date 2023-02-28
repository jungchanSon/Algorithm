import sys
import copy
input = sys.stdin.readline

N = int(input())
board = []
up_right = [0 for _ in range(2*N - 1)]
up_left = [0 for _ in range(2*N - 1)]
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

ans = 0

def bt(diagonal, cnt):
    global ans
    
    if diagonal == 2*N - 1:
        ans = max(ans, cnt)
        return
    
    flag = False
    search_range = N - abs((diagonal - (N-1)))
    
    for i in range(search_range):
        if diagonal < N:
            x = i
            y = diagonal - i
        else:
            x = diagonal - N + i + 1
            y = N - i - 1
            
        if board[y][x] and up_right[diagonal] == 0 and up_left[N - 1 - (y - x)] == 0:
            flag = True
            up_right[diagonal] = 1
            up_left[N - 1 - (y - x)] = 1
            
            bt(diagonal + 1, cnt + 1)
            
            up_right[diagonal] = 0
            up_left[N - 1 - (y - x)] = 0
            
    if not flag:
        bt(diagonal + 1, cnt)
            
bt(0, 0)
print(ans)
"""
# 참고 https://codingnotes.tistory.com/90 #

모든 방향의 대각선을 고려할 필요가 없음
우상 대각선 / 우하 대각선 중 하나만 고려하면, 모든 케이스 체크 가능
-> 대각선의 갯수로 탈출 조건 정의
th 번째의 대각선의 갯수 = n - |th - (n-1)|

"""


