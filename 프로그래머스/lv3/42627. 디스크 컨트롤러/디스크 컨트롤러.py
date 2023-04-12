import heapq
import math
from collections import deque

def solution(jobs):
    L = len(jobs)
    jobs.sort()

    start = jobs[0][0]
    first = jobs.pop(0)
    cur_time = first[1]
    answer = first[1]

    for i in jobs:
        i[0] -= start
    cnt = 1
    while jobs:
        heap = []
        for time, work in jobs:
            if time < cur_time:
                heapq.heappush(heap, [work, time])
            else :
                break
            
        if heap:
            work, time = heapq.heappop(heap)
            print(0, cur_time,work, answer)
            cur_time += work
            answer += cur_time - time
            jobs.remove([time, work])
            cnt +=1 
        else:
            cur = jobs.pop(0)
            cur_time = cur[0] + cur[1]
            answer += cur[1]
            print(1, cur_time, answer)
            cnt += 1 
    answer //= L
    return int(answer);
