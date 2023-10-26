import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

def recursion(a,b):
    if b == 1 :
        return a % C 
    temp = recursion(a, b//2)
    
    if b % 2 == 0:
        return (temp * temp) % C     
    else :
        return (temp * temp * a) % C
print(recursion(A, B))

"""
참고 :https://www.acmicpc.net/board/view/39615
      https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%EA%B3%B1%EC%85%88-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
an =  an/2  *  an/2  (n %2 == 0)
an =  a(n-1)/2 *  a(n-1)/2 x a (n%2 != 0)
"""