import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

p = [i for i in range(n+1)]

def find(n):
    if p[n] == n :
        return n
    
    p[n] = find(p[n])
    
def union(l):
    temp = []
    for i in l:
        temp.append(find(i))
    
    m = min(temp)
    for i in temp:
        if i != m :
            p[i] = m
        
        
    
    
for i in range(n):
    data = list(map(int, input().rstrip().split()))

    if data[0] == 1:
        union(data[1:])
    

st = list(map(int, input().rstrip().split()))

a = p[st[0]]
for i in range(len(st[1:])):
    