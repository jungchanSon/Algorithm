def solution(alp, cop, problems):
    answer = 1e6
    
    alp_max = max(problems, key = lambda x : x[0])[0]
    cop_max = max(problems, key = lambda x : x[1])[1]
    
    print(alp_max, cop_max )
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    
    dp = [[1e6 for _ in range(180)] for _ in range(180)]
    dp[alp][cop] = 0
    
    for i in range(alp, alp_max+1):
        for j in range(cop, cop_max+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue
                alp_nxt = min(alp_max, i+alp_rwd)
                cop_nxt = min(cop_max, j+cop_rwd)
                dp[alp_nxt][cop_nxt] = min(dp[alp_nxt][cop_nxt], dp[i][j]+cost)
                
    return dp[alp_max][cop_max]
#                 dp[i+alp_rwd][j+cop_rwd] = min(dp[i+alp_rwd][j+cop_rwd], dp[i][j] + cost)
#     for i in range(alp_max, 180):
#         for j in range(cop_max, 180):
#             answer = min(answer, dp[i][j])
    
#     return answer