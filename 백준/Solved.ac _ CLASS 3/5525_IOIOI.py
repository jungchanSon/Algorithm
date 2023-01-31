# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# M = int(input())
# # S = deque(list(input().rstrip()))
# S = input().rstrip()

# unit = N*2 +1
# cnt = 0

# collect = "IO"*N +"I"

#슬라이싱은 시간초과
# while 1 :
#     if len(S) < unit:
#         break
#     if S[0] == "O":
#         S.popleft()
#         continue
#     t = "".join(list(S)[:unit])
#     if t == collect :
#         S.popleft()
#         cnt += 1
#     S.popleft()
    
# print(cnt)

# cursor = 0
# while cursor < M-1 :
#     if S[cursor:cursor + unit] == collect:
#         cursor+= 2
#         cnt+=1
#     else :
#         cursor +=1 
# print(cnt)


import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
# S = deque(list(input().rstrip()))
S = input()

unit = N*2 +1
cnt = 0
collect = "IO"*N + "I"
cursor = 0
count = 0
while cursor < M-1:
    # if S[cursor:cursor + unit] == collect:
    if S[cursor:cursor + 3] == "IOI":
        cursor += 2
        count += 1
        if count == N:
            cnt +=1
            count -=1
    else :
        count = 0
        cursor +=1 
print(cnt)

# 참고: https://aia1235.tistory.com/30

# 참고: https://aia1235.tistory.com/30

