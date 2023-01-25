import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
    
white = 0
black = 0
def recursion(array, length):
    global white, black
    
    s = 0
    for i in array:
        s += sum(i)
    if s == 0:
        white += 1
        return
    elif s == length**2:
        black += 1
        return
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
        
    recursion(lt, length//2)
    recursion(rt, length//2)
    recursion(lb, length//2)
    recursion(rb, length//2)
    
recursion(arr, n)
print(white)
print(black)