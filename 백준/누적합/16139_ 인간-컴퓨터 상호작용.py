import sys
input = sys.stdin.readline
S = input().rstrip()
q = int(input().rstrip())
dp = [[0 for _ in range(len(S)+1)] for _ in range(26)]

for i in range(len(S)):
    for j in range(26):
        if ord(S[i]) - 97 == j:
            dp[j][i+1] = dp[j][i] + 1
        else :
            dp[j][i+1] = dp[j][i] 
data = []
for _ in range(q):
    data = input().rstrip().split()
    
    index = ord(data[0]) - 97
    start = int(data[1])
    end = int( data[2])
    
    a = dp[index][start]
    b = dp[index][end+1]
    print(b-a)

"""
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
"""