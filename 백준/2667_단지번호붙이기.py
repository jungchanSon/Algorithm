import sys
input = sys.stdin.readline

n = int(input())
houses = []
ans = []
cnt = 0
for _ in range(n):
    line = list(map(int, list(input().rstrip())))
    houses.append(line)

def sol(i, j) :
    global cnt
    if houses[i][j] == 0:
        return
    
    houses[i][j] = 0 
    cnt +=1
    
    if i < n-1:
        if houses[i+1][j] == 1: #하
            sol(i+1, j)
    if i != 0:
        if houses[i-1][j] == 1: #상
            sol(i-1, j)
    if j != 0:
        if houses[i][j-1] == 1: #좌
            sol(i, j-1)
    if j < n-1: 
        if houses[i][j+1] == 1: #우
            sol(i, j+1)
        
for i in range(len(houses)):
    for j in range(len(houses[i])):
        if houses[i][j] == 1:
            sol(i, j)
            ans.append(cnt)
            cnt = 0
            
ans.sort()
print(len(ans))
for i in ans:
    print(i)
"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""