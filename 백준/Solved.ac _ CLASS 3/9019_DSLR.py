import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    n = int(n) * 2 % 10000 
    return n 
def S(n):
    n = (int(n) - 1) % 10000
    return n
def L(n):
    return (10*int(n) + (int(n)//1000))%10000
def R(n):
    return (int(n)//10 + (int(n) % 10)*1000) % 10000

T = int(input())
    

for _ in range(T):
    visited = [0 for _ in range(10001)]

    a, b = input().rstrip().split()
    b = int(b)

    q = deque()
    q.append((a, ""))

    while q:
        t, op = q.popleft()
        visited[int(t)] = True
        if int(t) == b:
            print(op)
            break
        
        d = D(t) 
        if d < 10000:
            if not visited[d] :
                q.append((d, op+"D"))
                visited[d] = True
        
        s = S(t)
        if s < 10000:
            if not visited[s] :
                q.append((s, op+"S"))
                visited[s] = True
        l = L(t)
        if l < 10000:
            if not visited[l] :
                q.append((l, op+"L"))
                visited[l] = True
        r = R(t)
        if r < 10000:
            if not visited[r]:
                q.append((r, op+"R"))
                visited[r] = True