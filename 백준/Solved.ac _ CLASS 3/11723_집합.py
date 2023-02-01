import sys
input = sys.stdin.readline

M = int(input())
s = set()
for _ in range(M):
    temp = input().rstrip()
    if temp == "all":
        op = "all"
    elif temp == "empty":
        op = "empty"
    else :
        op, n = temp.split()
        n = int(n)
    if op == "add":
        s.add(n)
    elif op == "remove":
        s -= {n}
    elif op == "check":
        if n in s:
            print(1)
        else : 
            print(0)
    elif op == "toggle":
        if n in s:
            s -= {n}
        else :
            s.add(n)
    elif op == "all":
        s = {i for i in range(1, 21)}
    elif op == "empty":
        s = set()
    
