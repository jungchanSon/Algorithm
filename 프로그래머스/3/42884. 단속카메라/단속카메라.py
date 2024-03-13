def solution(routes):
    answer = 0
    routes.sort(key = lambda x: (x[0], x[1]))
    for i in routes:
        print(i)
    
    std = routes.pop(0)[1]
    answer += 1
    while routes:
        s, e = routes.pop(0)
        if std < s:
            std = e        
            answer += 1
        std = min(std, e)
    return answer