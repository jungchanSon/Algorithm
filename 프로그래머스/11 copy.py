from collections import deque

def solution(s):

    q = deque(s)
   
    if len(s) == 1 :
        return 0
    
    answer = 0
    
    collect = []
    
    big = deque()
    middle = deque()
    small = deque()
    
    for _ in range(len(s)):
        check = False
        for i in q:
            if i == "[":
                big.append(i)
            elif i == "{":
                middle.append(i)
            elif i == "(":
                small.append(i)
            elif i == "]":
                if big:
                    big.popleft()
                else:
                    check = True
                    break
            elif i == "}":
                if middle:
                    middle.popleft()
                else:
                    check = True
                    break
            elif i == ")":
                if small:
                    small.popleft()
                else:
                    check = True
                    break
                
        if not check:
            if small or middle or big:
                return 0 
            else :
                answer+=1
        collect.append(q.copy())
        temp = q.popleft()
        q.append(temp)
    
    return answer


print(solution( "[](){}"))
print(solution( "}]()[{"))
print(solution("[)(]" ))
print(solution( "}}}"))
print(solution( "{"))
print(solution( "}"))
print(solution( "{}"))
print(solution( "()"))
print(solution( "(())()"))