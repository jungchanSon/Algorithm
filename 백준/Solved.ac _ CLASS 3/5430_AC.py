import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    temp = input().rstrip()
    if len(temp) == 2:
        s = []
    else :
        s = deque(list(map(int, temp[1:-1].split(","))))
    check = True

    reverse = False
    for i in range(len(p)):
        if p[i] == "R":
            reverse = not reverse
        elif p[i] == "D":
            if s:
                if reverse:
                    s.pop()
                else:
                    s.popleft()
            else:
                print("error")
                check = False
                break
    if check:
        if reverse:
            s.reverse()
        if len(s):
            print("[",end="")
            for i in range(len(s)):
                if i != len(s) - 1:
                    print(s[i], end=",")
                else :
                    print(s[i], end="]\n")
        else : 
            print("[]")