import sys
input = sys.stdin.readline

data1 = input()
data2 = input()
dp = [[0 for _ in range(len(data2))] for _ in range( len(data1))]

for i in range(1, len(data1)):
    for j in range(1, len(data2)):
        if data1[i-1] == data2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 

# for i in dp:
#     print(i)
    
print(dp[len(data1)-1][len(data2)-1])
""""
ACAYKP
CAPCAK
"""
