import sys

input = sys.stdin.readline

def w(a, b, c) :
    
    for i in range(1, 21):
        for j in range(1, 21):
            for w in range(1, 21):
                if i < j < w:
                    wList[i][j][w] = wList[i][j][w-1] + wList[i][j-1][w-1] - wList[i][j-1][w]
                else : 
                    wList[i][j][w] = + wList[i-1][j][w] + wList[i-1][j-1][w] + wList[i-1][j][w-1] - wList[i-1][j-1][w-1]
wList = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
w(20, 20, 20)
while 1:
    a, b, c = list(map(int, input().rstrip().split()))
    
    if a == b == c == -1 :
        break
    
    
    
    if a <= 0 or b <= 0 or c <= 0:
        print("w("+str(a)+", "+str(b)+", "+ str(c)+ ") = "+ str(1))
    elif a > 20 or b > 20 or c > 20:
        print("w("+str(a)+", "+str(b)+", "+ str(c)+ ") = "+ str(wList[20][20][20]))
    else:
        print("w("+str(a)+", "+str(b)+", "+ str(c)+ ") = "+ str(wList[a][b][c]))
    