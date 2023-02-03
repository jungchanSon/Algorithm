import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    line = list(map(int, input().rstrip().split()))
    arr.append(line)
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in arr:
    print(i)
    
"""
나중에 다시 한번 풀어보기
플로이드 워셜.
"""