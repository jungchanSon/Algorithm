import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
arrA = []

for _ in range(N):
    arrA.append(list(input().rstrip()))
    
arrB = copy.deepcopy(arrA)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

a = 0
b = 0
def dfsA(cx, cy, color):
    if arrA[cx][cy] != color:
        return
    if arrA[cx][cy]:
        arrA[cx][cy] = 0
    else :
        return
    for i in range(4):
        x = cx + dx[i]
        y = cy + dy[i]
        
        if x < 0 or x >= len(arrA[0]) or y < 0 or y >= len(arrA):
            continue
        dfsA(x, y, color)


def dfsB(cx, cy, color):
    if color == "B" and color != arrB[cx][cy]:  
        return
    elif (color == "G" or color == "R") and arrB[cx][cy] == "B":
        return
    if arrB[cx][cy]:
        arrB[cx][cy] = 0
    else :
        return
    for i in range(4):
        x = cx + dx[i]
        y = cy + dy[i]
        
        if x < 0 or x >= len(arrB[0]) or y < 0 or y >= len(arrB):
            continue
        
        dfsB(x, y, color)

for i in range(len(arrA)):        
    for j in range(len(arrA[0])):
        if arrA[i][j]:
            dfsA(i, j, arrA[i][j])
            a += 1
        if arrB[i][j]:
            dfsB(i, j, arrB[i][j])
            b += 1
print(a, b)