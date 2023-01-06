import sys
input = sys.stdin.readline

ans = []

def solution(i, j):
    global cnt
    if field[i][j] == 0 :
        return
    
    field[i][j] = 0
    
    #상
    if i != 0:
        if field[i-1][j] == 1:
            solution(i-1, j)
    #좌
    if j != 0:
        if field[i][j-1] == 1:
            solution(i, j-1)
    #우
    if j < m-1:
        if field[i][j+1] == 1:
            solution(i, j+1)
    #하
    if i < n-1:
        if field[i+1][j] == 1:
            solution(i+1, j)

caseN = int(input().rstrip())


# caseN만큼 반복
for _ in range(caseN):
    cnt = 0
    m, n, k = map(int, input().rstrip().split()) # m=가로, n=세로, k=배추수

    field = [[0 for _ in range(m)] for _ in range(n)]

#field에 배추 심기
    for _ in range(k):
        y, x = list(map(int, input().rstrip().split()))
        field[x][y] = 1
        
# field에서 필요한 수 체크
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                solution(i, j)
                cnt += 1
    ans.append(cnt)
           
           
for i in ans:
    print(i)
        

"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""