import sys
from collections import deque
input = sys.stdin.readline

l, c = map(int,input().rsplit())
arr = list(input().rsplit())

arr.sort()

def check(s): 
    a, b = 0, 0
    for i in s:
        if i in ['a','e','i','o','u']: 
            a += 1
        else: 
            b += 1 
    if a >= 1 and b >= 2: 
        return True
    else:
        return False
def dfs(current, cur_s): 
    global c, l
    
    if len(cur_s) == l: 
        if check(cur_s): 
            print(cur_s)
        return
    
    for i in range(current+1, c):
        dfs( i, cur_s + arr[i])
        
for i in range(0, c-l+1):
    visited = [False for _ in range(c)]
    dfs(i, arr[i])