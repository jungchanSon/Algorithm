import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
def bf(current, cnt):
    if current > B:
        return 0
    if current == B:
        return cnt
    temp = 0
    temp = bf(current*2 , cnt+1)
    temp = max(temp, bf(int(str(current) + "1"), cnt +1))
    
    return temp
ans = bf(A, 1)

if ans:
    print(ans)
else:
    print(-1)