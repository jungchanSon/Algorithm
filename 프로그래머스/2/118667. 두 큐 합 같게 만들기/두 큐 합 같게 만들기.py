from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)
    maxlen = 4*len(queue1)
    while s1 != s2:
        answer += 1
        if s1 > s2:
            a = q1.popleft()
            s1 -= a
            s2 += a
            q2.append(a)
            
        elif s2 > s1:
            a = q2.popleft()
            s2 -= a
            s1 += a
            q1.append(a)
            
        if answer > maxlen:
            return -1 
        
    return answer