import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
T = list(map(int, input().rstrip().split()))[1:]
arr = []
for _ in range(M):
    arr.append(list(map(int, input().rstrip().split()))[1:])


if T == 0:
    print(len(arr))
    quit()

for _ in range(M):
    for i in arr:
        for j in T:
            if j in i:
                T += i
                T = list(set(T))
cnt = 0
for i in arr:
    isComponent = False
    for j in T:
        if j in i:
            isComponent =True
            break
    if not isComponent:
        cnt +=1
print(cnt)