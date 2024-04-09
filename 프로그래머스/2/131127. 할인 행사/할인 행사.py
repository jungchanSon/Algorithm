def solution(want, number, discount):
    answer = 0
    
    DATE = sum(number)
    N = len(discount) 
    
    for i in range(0, N-DATE+1):
        temp = discount[i:i+DATE]
        
        for j in range(len(want)):
            w = want[j]
            wn = number[j]
            
            if temp.count(w) != wn:
                break
            if j == len(want)-1:
                answer += 1
            
        
        
    return answer