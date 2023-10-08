def solution(d, budget):
    answer = 0
    
    d.sort()
    
    while d and d[0] <= budget:
        budget -= d.pop(0)
        answer += 1 
    print(budget, d)
    return answer