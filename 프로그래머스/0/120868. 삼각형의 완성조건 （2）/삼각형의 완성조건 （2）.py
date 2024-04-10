def solution(sides):
    ma = max(sides)
    mi = min(sides)
    
    #1. m-a < x <= m
    #2. m < x < a+b
    #1.
    ans = ma - (ma-mi+1)
    print(ans)
    ans += ma+mi - ma
    print(ans)
    
    
    answer = 0
    return ans