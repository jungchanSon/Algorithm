import sys

s = list(input())
n = int(input())
t = []

for i in range(n):
    a = input().rstrip().split()
    if a[0] == "L":
        if s:
            t.append(s.pop())
    elif a[0] == "D":
        if t:
            s.append(t.pop())    
    elif a[0] == "B":
        if s:
            s.pop()
    else:
        s.append(a[1])

print("".join(s+list(reversed(t))))