import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    w = dict()
    n = int(input())
    
    for _ in range(n):
        name, t = input().rstrip().split()
        if t in w.keys() :
            w[t].append(name)
        else:
            w[t] = []
            w[t].append(name)
    
    l = []
    for i in w.keys():
        l.append(len(w[i]))
        
    if len(w.keys()) == 1 : 
        print(n)
    else :
        s = 1
        for i in l:
            s *= (i+1)
        print(s-1)