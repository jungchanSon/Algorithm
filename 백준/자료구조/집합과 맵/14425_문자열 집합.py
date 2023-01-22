import sys
input = sys.stdin.readline

n, m = map(int, input().split())

strList = []
strdict = {}
for _ in range(n):
    strdict[input().rstrip()] = True

cnt = 0
checkList = []
for _ in range(m):
    a = input().rstrip()
    if strdict.get(a):
        cnt +=1

print(cnt)