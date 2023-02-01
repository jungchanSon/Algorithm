import sys
input = sys.stdin.readline

N = int(input())
Ps = list(map(int, input().rstrip().split()))
Ps.sort()

if len(Ps) > 1:
    for i in range(1, len(Ps)):
        Ps[i] += Ps[i-1]
    print(sum(Ps))
elif len(Ps) <= 1:
    print(Ps[0])