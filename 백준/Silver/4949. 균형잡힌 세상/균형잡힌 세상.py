import sys
input = sys.stdin.readline

while True:
    q = []
    line = input().rstrip()
    check = True
    if line == ".": 
        break
    for i in line:
        if i == "(" or i == "[":
            q.append(i)
        elif i == ")":
            if not q or q[-1] != "(":
                check = False
                break 
            q.pop()
        elif i == "]":
            if not q or q[-1] != "[" : 
                check = False
                break
            q.pop()
    if q:
        print('no')
    else: 
        if check:
            print('yes')
        else:
            print('no')