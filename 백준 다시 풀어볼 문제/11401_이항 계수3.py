import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, K = list(map(int, input().rstrip().split()))

def recursion(a, b):
    
    # if a == b or b == 0:
    #     return 1
    # result = (recursion(a-1, b-1) + recursion(a-1, b)) % 1000000007
    if b == 0:
        return 1
    if b == 1 :
        return a
    
    temp = recursion(a, b//2)
    
    if b % 2 == 0:
        return temp * temp % 1000000007
    else :
        return temp * temp * a % 1000000007

def factorial(a):

    temp = 1 
    for i in range (2, a+1):
        temp *= (temp*i) % 1000000007
    return temp

result = (factorial(N) * recursion( factorial(K) * factorial(N-K) % 1000000007, (1000000005) ))% 1000000007
print(result)
"""
도움 : https://st-lab.tistory.com/241

이항(a, b) = a! / { b! * (a-b)! } mod n
=> a!(mod n) / {b! * (a-b)! (mod n)} 불가능! ( mod 는 나누기의 분배법칙 불가 )

==> {b! * (a-b)! (mod n)} 의 역원을 구해서 곱셈의 분배법칙으로 변환
==> (페르마의 소정리) a (mod n)의 역원 == a^(n-2) (mod n)

===> 1/{b! * (a-b)!} mod n == {b! * (a-b)!}^(n-2) (mod n)

===> a! (mod 1000000007) * {b! * (a-b)! ^ (1000000007-2)} (mod 1000000007)
"""