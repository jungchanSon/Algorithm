def solution(people:list , limit:int):
    answer = 0
    arr = []
    
    people.sort() #10, 20, 30, 60, 70 80 100
    l = 0
    r = len(people) - 1
    while l<=r:
        if people[l] + people[r] <= limit:
            l += 1 
            r -= 1
            answer += 1
        else:
           r -= 1 
           answer += 1 
    return answer