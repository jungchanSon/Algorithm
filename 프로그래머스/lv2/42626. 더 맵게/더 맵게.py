from collections import deque
import heapq

def solution(scoville, K):
    answer = 0
    cur_scoville = 0
    heapq.heapify(scoville)
    
    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            return answer
        
        if scoville:
            b = heapq.heappop(scoville)
        else :
            return -1
        cur_scoville= a + b * 2
        heapq.heappush(scoville, cur_scoville)
        answer += 1
        
    return answer
