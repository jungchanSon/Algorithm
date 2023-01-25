import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

temp = []
def recursion(a, b):
    if b == 1:
        return 1
    if b % 2 == 0:
        return ( recursion(a**(b/2), b+1))%C * (recursion(a**(b/2), b+1) ) % C
        
    else : 
        return (recursion(a **((b-1)/2), b+1))%C * (recursion(a **((b-1)/2), b+1) * a) % C
        
if B == 1:
    print(A % C)
else :
    print(recursion(A, B))
"""
참고 :https://www.acmicpc.net/board/view/39615

an =  an/2  *  an/2  (n %2 == 0)
an =  a(n-1)/2 *  a(n-1)/2 x a (n%2 != 0)
"""