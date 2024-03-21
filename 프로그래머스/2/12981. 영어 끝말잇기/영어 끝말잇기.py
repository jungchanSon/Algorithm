from collections import deque
import math
def solution(n, words):
    answer = [0, 0]
    dq = deque(words)
    temp = []
    temp.append(dq.popleft())
    cnt = 1
    while dq:
        poped = dq.popleft()
        
        if poped[0] != temp[-1][-1] or poped in temp:
            answer = [(cnt%n)+1, math.ceil((cnt+1)/n)]
            break
            
        temp.append(poped)
        last = poped[-1]
        cnt += 1

    return answer
"""
1, 2 ,3 , 1, 2, 3
""" 