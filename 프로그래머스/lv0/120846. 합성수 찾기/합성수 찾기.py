def solution(n):
    answer = 0
    
    dp = [0 for _ in range(101)]
    dp[4] = 1
    for i in range(5, 101):
        if is_composite_num(i):
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
            
    return dp[n]
def is_composite_num(n : int):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False