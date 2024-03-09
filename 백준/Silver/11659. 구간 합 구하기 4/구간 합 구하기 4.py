import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = list(map(int, input().rsplit()))
req = []
for _ in range(n):
    req.append(list(map(int, input().rsplit())))

if m == 1:
    print(arr[0])
    quit()

for i in range(1, m):
    arr[i] = arr[i] + arr[i-1]
arr = [0] + arr
for s, e in req:
    print(arr[e] - arr[s-1])