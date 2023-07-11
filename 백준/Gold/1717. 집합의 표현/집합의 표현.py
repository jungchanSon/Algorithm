import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n, m = map(int, input().rsplit())
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
    
for _ in range(m):
    c, a, b = map(int, input().rsplit())
    
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")