import sys
input = sys.stdin.readline 

data1 = input().rstrip()
data2 = input().rstrip()

dp = [0 for _ in range(max(len(data1), len(data2)))]
dp2 = ["" for _ in range(max(len(data1), len(data2)))]

if len(data1) > len(data2):
    long_data = data1
    short_data = data2
else:
    long_data = data2
    short_data = data1
# print("long :", long_data)
# print("short :", short_data)
# ans = []
for i in range(len(short_data)):
    temp = []
    for j in range(len(long_data)):
        if short_data[i] == long_data[j]:
            if j == 0:
                temp.append([j, 0, ""])
            else:
                temp2 = 0
                index = 0
                for k in range(j):
                    if dp[k] >= temp2:
                        temp2 = dp[k]
                        index = k
                cnt = dp[index]
                value = dp2[index]
                temp.append([j, cnt, value])
    for p, c, v in temp:
        dp[p] = c+ 1
        dp2[p] = v + short_data[i]
# print(dp)
# print(dp2)

temp = 0
pos = 0
for i in range(len(dp)):
    if dp[i] > temp:
        temp = dp[i]
        pos = i
print(dp[pos])
print(dp2[pos])
"""
ACAYKP
CAPCAK
"""