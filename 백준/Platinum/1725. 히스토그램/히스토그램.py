from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
data =[int(input()) for _ in range(n)] 
stack = []
cur = 0
ans = 0
cur_h = 0

for i in range(n):
    h = data[i]
    
    while stack and data[stack[-1]] > h:
        index = stack.pop()    
        
        w = i 
        if stack:
            w = (i - stack[-1] -1)
        ans = max(ans, data[index]* w)
        w += 1 

    stack.append(i)            

while stack:
    i = stack.pop()
    h = data[i]
    w = n
    if stack :
        w = n -stack[-1] -1
    ans = max(ans, h*w)
print(ans)