import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def find(a: int):
    if a == parent[a]: return a
    parent[a] = find(parent[a])
    
    return parent[a] 

def union(a: int, b: int):
    a = find(a)
    b = find(b)
    
    if a == b : return
    if a < b : parent[b] = a
    else: parent[a] = b
    
for i in range(1, n+1):
    data = list(map(int, input().rsplit()))
    
    for j in range(1, n+1):
        if data[j-1] == 1:
            union(i, j)
        
    
plan = list(map(int, input().rsplit()))
first = find(plan[0])
result = True
for i in plan[1:]:
    if first != find(i):
        result = False
if result == True:
    print("YES")
else:
    print("NO")