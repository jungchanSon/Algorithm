import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
B = list(map(int, input().rstrip().split()))

m = abs(N - 100)

for i in range(1000001):
    t = str(i)
    
    for j in range(len(t)):
        if int(t[j]) in B:
            break;
        elif j == len(t)-1:
            m = min(m, abs(N-int(t))+len(t))

print(m)
"""
같다 -> 가까운 수
크다 -> 작은 수
작다 -> 큰 수
1. 같은 수
2. 큰수, 작은 수
"""

# 참고 : https://seongonion.tistory.com/99