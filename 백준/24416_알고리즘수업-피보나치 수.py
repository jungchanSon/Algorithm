import sys

input = sys.stdin.readline

n = int(input().rstrip())

recursionCnt = 0
def recursion(n):
    global recursionCnt
    recursionCnt += 1 
    
    if n == 1 or n == 2 :
        recursionCnt -= 1
        return 1
    
    else:
        return (recursion(n-1) + recursion(n-2))

dpCnt = 0
def dp(n):
    global dpCnt
    
    f = [0 for _ in range(n+1)]
    
    f[1] = 1
    f[2] = 1 
    
    for i in range(3, n+1):
        dpCnt += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

recursion(n)


print(recursionCnt + 1, n-2 )


