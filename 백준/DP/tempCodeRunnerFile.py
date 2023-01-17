import sys
input = sys.stdin.readline

data1 = input()
data2 = input()
dp = [0 for _ in range(len(data1)-1)]
if len(data1) < len(data2):
    temp = data2
    data2 = data1
    data1 = temp
    
for d1 in range(len(data1)-1):
    for d2 in range(len(data2)-1):
        if data1[d1] == data2[d2]:
            if d2 == 0:
                dp[d2] = 1
            else:
                dp[d2]= max(dp[:d2])+1
print(max(dp))
""""
ACAYKP
CAPCAK
"""
