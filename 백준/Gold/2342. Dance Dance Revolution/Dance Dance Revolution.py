import sys
input = sys.stdin.readline

input_data = list(map(int, input().rstrip().split()))
input_data.pop()
# dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(100000)] 
dp = [[[400001 for _ in range(5)] for _ in range(5)] for _ in range(len(input_data)+1)] 

def cal(c, n):
    if c == 0 and n != 0:
        return 2
    if c == n:
        return 1
    if abs(c - n) == 2:
        return 4
    else : 
        return 3
# dp[n] = min(dp[n-1], dp[n-1])
# for i in range(len(input_data)):
#     l = dp[1]
#     r = dp[2]
    
#     p, l, r = dp[i-1][0]
#     c1 = cal(dp[i-1][0][1], input_data[i])
#     c2 = cal(dp[i-1][1][1], input_data[i])
#     if c1 < c2:
#         dp[i][0] = [p+c1, input_data[i], r]
#     else: 
#         dp[i][0] = [p+c2, input_data[i], dp[i-1][1][2]]

#     p, l, r = dp[i-1][0]
#     c1 = cal(dp[i-1][0][2], input_data[i]) 
#     c2 = cal(dp[i-1][1][2], input_data[i])    
#     if c1 < c2:
#         dp[i][1] = [p+c1, l,  input_data[i]]
#     else: 
#         dp[i][1] = [p+c2, dp[i-1][1][1],  input_data[i]]
#     print(dp[i])
# 실패 : 1 3 2 4 1 3 2 4 0 
# 참고 : https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-2342-Dance-Dance-Revolution

dp[-1][0][0] = 0 #처음엔 왼발 오른발 -> 0

if len(input_data) == 0: 
    print(0)
    exit() 
for i in range(len(input_data)):
    #왼발
    for r in range(5):
        for k in  range(5):
            dp[i][input_data[i]][r] = min(dp[i][input_data[i]][r], dp[i-1][k][r] + cal(k, input_data[i]))
    #오른발
    for l in  range(5):
        for k in  range(5):
            dp[i][l][input_data[i]] = min(dp[i][l][input_data[i]], dp[i-1][l][k] + cal(k, input_data[i]))
ans = 400001
for i in dp[len(input_data)-1]:
    ans = min(ans, min(i))
    
print(ans)
# 동일 : 1
# 중앙 : 2
# 인접 : 3
# 반대 : 4 