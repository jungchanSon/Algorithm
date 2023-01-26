import sys 
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, B = map(int, input().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

result = [[ 0 for _ in range(N)] for _ in range(N)]

def recursion(array, depth):
    if depth >= B: 
        global result
        result = array
        return

    temp = [[ 0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s = 0
            for z in range(N):
                s += array[i][z] * arr[z][j]
                s %= 1000
            temp[i][j] = s 
    recursion(temp, depth+1)


if B == 1:
    for i in arr:
        print(" ".join(list(map(str, i))))
else :
    B -= 1
    recursion(arr, 0)
    for i in result:
        print(" ".join(list(map(str, i))))
        
