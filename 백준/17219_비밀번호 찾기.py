import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
site_ps = {}
for _ in range(N):
    s, p = input().rstrip().split()
    site_ps[s] = p
        
for _ in range(M):
    targetSite = input().rstrip()
    print(site_ps[targetSite])