import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

data = []
for _ in range(q):
    temp = input().rstrip().split()
    temp[1:3] = list(map(int, temp[1:3]))
    data.append(temp)
    
set_data = list(set(list(S)))
set_data.sort()

dp = [[0 for _ in range(len(S)+1)] for _ in range(len(set_data))]
for i in range(len(S)):
    index = set_data.index(S[i])
    dp[index][i+1] = max(dp[index]) +1

# for i in dp:
#     print(i)
# print(dp)

for i in data:
    alpa = i[0]
    start = i[1]
    end = i[2]
    if alpa in set_data:
        index = set_data.index(alpa)
        a = max(dp[index][:start+1])
        b = max(dp[index][start+1:end+2])
        print(b-a)
    else :
        print(0)

"""
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
"""