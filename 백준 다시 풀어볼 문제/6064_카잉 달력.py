import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().rstrip().split())

    currentX = 1
    currentY = 1
    cnt = 0
    maxn = M*N
    while 1:
        if (cnt *M + x )% N == y:
            print(cnt *M + x )
            break
        elif cnt * M + x > maxn:
            print(-1)
            break
        cnt += 1

"""
참고 https://www.youtube.com/watch?v=YLsntT3F_AE
"""