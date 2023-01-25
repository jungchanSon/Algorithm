import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    i = list(input().rstrip())
    arr.append(list(map(int, i)))

def recursion(array, length):
    s = 0
    for i in array:
        s += sum(i)
    if s == 0:
        return "0"
    elif s == length**2:
        return "1"
    lt = []
    for i in range(length//2):
        lt.append(array[i][:length//2])
    rt = []
    for i in range(length//2):
        rt.append(array[i][length//2:length])
    lb = []
    for i in range(length//2, length):
        lb.append(array[i][:length//2])
    rb = []
    for i in range(length//2, length):
        rb.append(array[i][length//2:length])
    
    r = ""
    r+= "("
    r += recursion(lt, length//2)
    r += recursion(rt, length//2)
    r += recursion(lb, length//2)
    r += recursion(rb, length//2)
    r +=")"
    return r

print(recursion(arr, N))