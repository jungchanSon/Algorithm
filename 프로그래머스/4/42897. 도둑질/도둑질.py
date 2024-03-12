def solution(money):
    answer = 0
    n = len(money )
    money.append(money[0])
    dp = [0 for _ in range(n-1)]
    dp[0] = money[0]
    dp[1] = max(money[1], money[0])
    for i in range(2, n-1): 
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    dp2 = [0 for _ in range(n-1)]
    dp2[0] = money[1]
    dp2[1] = max(money[1], money[2])
    for i in range(2, n-1):
        dp2[i] = max(dp2[i-1], dp2[i-2] +money[i+1])
   
    answer = max(dp[n-2], dp2[n-2])
    return answer