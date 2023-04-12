import sys
import copy
input = sys.stdin.readline

N = int(input())
board = [ list(map(int, input().rstrip().split())) for _ in range(N)]
l = [1,2,3,4]
v = [False for _ in range(6)]

def up(b):
    for i in range(len(b)):
        temp_l = []
        for j in range(len(b[0])):
            if b[j][i]:
                temp_l.append(b[j][i])
        for k in range(len(temp_l)-1):
            if temp_l[k] == temp_l[k+1]:
                temp_l[k] *= 2
                temp_l.pop(k+1)
            
def down():
    
def bt(b, d):
    if d == 5:
        pass
    
    bt(up(b), d + 1)
    bt(down(b), d +1)
    bt(left(b), d+1)
    bt(right(b), d+1)
    
    
bt(copy.deepcopy(board), 0)