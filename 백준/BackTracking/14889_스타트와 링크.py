import sys

input = sys.stdin.readline

n = int(input().rstrip())

board = []

for _ in range(n):
    data = list(map(int, input().rstrip().split()))
    board.append(data)


result_team = []
team = [0 for _ in range(n)]
team[0] = 1
otherTeamPoint = 0
answer = []



def bt(l, d, p) :
    global otherTeamPoint
    if sum(team) == n//2:
        otp = 0
        for i in range(n):
            for j in range(i, n):
                if i not in l and j not in l:
                    if i != j:
                        otp += board[i][j]+board[j][i]
                        
        answer.append(abs(otp-p))
        return
    for i in range(d+1, n):
        # po =  p + board[d][i] + board[i][d]
        po = 0
        for et in l : 
            po += board[et][i]+board[i][et]
        team[i] = 1
        l.append(i)
        bt(l, i, p+po)
        team[i] = 0
        l.remove(i)
        
bt([0], 0, 0)

# print(min(answer))
print(min(answer))
