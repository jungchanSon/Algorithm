from collections import Counter
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(a:int, b:int):
    x = find(a)
    y = find(b)
    if x == y:
        return rank[y]
    parent[x] = y
    rank[y] += rank[x]
    return rank[y]

t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    temp = []
    parent = {}
    rank = {}
    for _ in range(n):
        a, b = input().rstrip().split() 
        if a not in parent:
            parent[a] = a
            rank[a] = 1
        if b not in parent:
            parent[b] = b
            rank[b] = 1
        print(union(a, b))
        