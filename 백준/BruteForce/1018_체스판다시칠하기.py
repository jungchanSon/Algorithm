import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
test = []

for _ in range(n):
    test.append(list(input().rstrip()))

board1 = [ [] for _ in range(8)]
board2 = [[] for _ in range(8)]

check = True
for i in range(8):
    if check:
        board1[0].append('W')
        check = not check
    else :
        board1[0].append('B')
        check = not check
for i in range(1, 8):
    for j in range(8):
        if board1[i-1][j] == 'W':
            board1[i].append('B')
        else: 
            board1[i].append('W')

check = True
for i in range(8):
    if check:
        board2[0].append('B')
        check = not check
    else :
        board2[0].append('W')
        check = not check
        
for i in range(1, 8):
    for j in range(8):
        if board2[i-1][j] == 'W':
            board2[i].append('B')
        else: 
            board2[i].append('W')


ans = []
for di in range(n-7):
    for dj in range(m-7):
        b1 = 0
        b2 = 0
        for i in range(di, 8+di):
            for j in range(dj, 8+dj):
                if test[i][j] != board1[i-di][j-dj]:
                    b1 += 1
                
                if test[i][j] != board2[i-di][j-dj]:
                    b2 += 1
        ans.append(b1)
        ans.append(b2)
print(min(ans))