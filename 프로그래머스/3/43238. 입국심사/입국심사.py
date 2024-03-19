def solution(n, times):
    answer = 0
    l, r = 1, 1_000_000_000 * 1_000_000_000
    
    while l <= r: 
        m = (l+r) // 2 
        temp = 0
        
        for i in times:
            temp += m // i
          
        
        if temp >= n:
            answer = m
            r = m - 1
        else:
            l = m + 1
        
    
    return answer

