import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))
    
maxn = 0
for i in range(N): # l
    for j in range(M-3):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3])
for i in range(N-3): # ㅡ
    for j in range(M):
        maxn = max(maxn, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j])

#ㅏ
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+1][j+1])

#ㅓ
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1])
#ㅗ
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2])
#ㅜ
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1])
#ㅁ
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1])
#z1
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1])
#z2
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j])

#z3
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j+2])
#z4
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j+1]+arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1])

#ㄴ1
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2])
#ㄴ2
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+2][j])
#ㄴ3
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+2])
#ㄴ4
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1])
#ㄴ1
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2])
#ㄴ2
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1])
#ㄴ3
for i in range(N-1):
    for j in range(M-2):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j])
#ㄴ4
for i in range(N-2):
    for j in range(M-1):
        maxn = max(maxn, arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1])

print(maxn)