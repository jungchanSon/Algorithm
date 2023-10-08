def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    temp = 0
    for i in range(0, len(score), m):
        if len(score) - i < m:
            break
        answer += min(score[i: i+m]) * m
    return answer