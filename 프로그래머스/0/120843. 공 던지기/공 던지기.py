def solution(numbers, k):
    answer = 0
    tmp= 2*(k-1)
    answer = numbers[tmp%len(numbers)]
    return answer