def round(N):
    if N - int(N) >= 0.5:
        return int(N)+1
    else:
        return int(N)
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
mark = round(N * 0.15)

arr = arr[mark:N-mark]
if len(arr) == 0:
    print(0)
else:
    print(round(sum(arr)/len(arr)))