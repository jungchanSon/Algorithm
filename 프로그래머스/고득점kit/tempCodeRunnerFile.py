from collections import deque
import heapq

def solution(scoville, K):
    answer = 0
    cur_scoville = 0
    scoville = heapq.heapify(scoville)
    while scoville:
        check_scoville = True
        for i in scoville:
            if i < K:
                check_scoville = False
        
        if check_scoville:
            return answer
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        cur_scoville= a + b * 2
        heapq.heappush(scoville, cur_scoville)
        answer += 1
    return answer


data = [[[1, 2, 3, 9, 10, 12], 7]]

for s, k in data:
    print(solution(s, k))