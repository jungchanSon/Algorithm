import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))


bigDp = [ 0 for _ in range(n)]
smallDp = [ 0 for _ in range(n)]

for i in range(1, n):
    temp = []
    for j in range(i-1, -1, -1):                
        if data[i] > data[j] :
            temp.append(bigDp[j])
    if temp :
        bigDp[i] = max(temp) + 1
    else :
        bigDp[i] = 0
            
for i in range(n-2, -1, -1):
    temp = []
    for j in range(i, n, 1):
        if data[i] > data[j] :
            temp.append(smallDp[j])
    if temp:
        smallDp[i] = max(temp) + 1
    else :
        smallDp[i] = 0

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = smallDp[i] + bigDp[i]

if max(result) == 0:
    print(1)
else : 
    print(max(result)+ 1)
