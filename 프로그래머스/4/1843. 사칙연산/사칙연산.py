import math

def solution(arr):
    answer = -1
    n = len(arr)
    m = math.ceil(len(arr)/2)
    min_dp = [[False for _ in range(n)] for _ in range(n)]
    max_dp = [[False for _ in range(n)] for _ in range(n)]

    
    for i in range(0, n, 2): 
        min_dp[i][i] = int(arr[i])
        max_dp[i][i] = int(arr[i])
    min_dp[0][n-1] = eval("".join(arr))
    max_dp[0][n-1] = eval("".join(arr))
    for _ in range(2):
        for c in range(0, n, 2):
            for i in range(0, n-c, 2):
                j = i + c
                for k in range(i+1, j, 2):

                    if arr[k] == '-':
                        if not max_dp[i][j]:
                            max_dp[i][j] = max_dp[i][k-1] - min_dp[k+1][j]
                        else:
                            max_dp[i][j] = max(max_dp[i][j], max_dp[i][k-1] - min_dp[k+1][j])
                        if not min_dp[i][j]:
                            min_dp[i][j] = min_dp[i][k-1] - max_dp[k+1][j]
                        else:
                            min_dp[i][j] = min(min_dp[i][j], min_dp[i][k-1] - max_dp[k+1][j])
                    else:  
                        if not max_dp[i][j]:
                            max_dp[i][j] = max_dp[i][k-1] + max_dp[k+1][j]
                        else:
                            max_dp[i][j] = max(max_dp[i][j], max_dp[i][k-1] + max_dp[k+1][j])
                        if not min_dp[i][j]:
                            min_dp[i][j] = min_dp[i][k-1] + min_dp[k+1][j]
                        else:
                            min_dp[i][j] = min(min_dp[i][j], min_dp[i][k-1] + min_dp[k+1][j])
    # for i in min_dp:
    #     print(i)
    # print()
    # for i in max_dp:
    #     print(i)
    return max_dp[0][n-1]

''' 
dp[n] = max(dp[n-1] , dp[n-2])
dp[n] = max(dp[n-2]) eval(dp[n-2:n]) , dp[n-1]+dp[n]
'''