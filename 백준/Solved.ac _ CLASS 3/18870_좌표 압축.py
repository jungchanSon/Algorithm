import sys
import math
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().rstrip().split()))

arr = list(set(X))
arr.sort()

dic = dict()
for i in range(len(arr)):
    dic[arr[i]] = i
    
ans = [0 for _ in range(N)]

for i in range(N):
    n = dic[X[i]]
    ans[i] = n 
print(*ans)