import sys
input = sys.stdin.readline

N = int(input().rstrip())

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1) 
if N == 0:
    print(0)
else :
    number = str(factorial(N))
    cnt = 0
    for i in range(len(number) -1, -1 , -1):
        if "0" == number[i]:
            cnt += 1
        else :
            break
    print(cnt)