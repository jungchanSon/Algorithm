def solution(n):
    answer = ''

    while n:
        temp = n % 3
        if temp == 0:
            answer += str(4)
            n = n//3 -1
        else: 
            answer += str(temp)
            n = n//3
        
    answer = list(answer)
    answer.reverse()
    answer = "".join(answer)
    return answer

print(solution(100))