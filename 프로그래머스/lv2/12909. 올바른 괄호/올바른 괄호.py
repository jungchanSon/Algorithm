from collections import deque

def solution(s):
    
    stack = []
    s = deque(s)
    stack.append(s.popleft());
    if stack[-1] == ")":
        return False
    
    while s:
        cur = s.popleft()
        if cur == ")":
            if len(stack) == 0 :
                return False
            elif stack[-1] == "(":
                stack.pop()
                continue
            
        stack.append(cur)
    
    if stack:
        return False
    else : 
        return True
