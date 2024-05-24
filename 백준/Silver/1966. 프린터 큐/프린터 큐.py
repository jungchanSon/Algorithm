import heapq
import sys
import copy
input = sys.stdin.readline
inf = 1e9

T = int(input())
for _ in range(T):
    N, M = map(int,input().rsplit())
    imp = list(map(int, input().rsplit()))
    imp = [ (i, imp[i]) for i in range(len(imp))]
    ans = 1
    while imp:
        mx = max(imp, key=lambda x : x [1])[1]
        ci, cv = imp.pop(0)
        if cv == mx:
            if M == ci:
                print(ans)
                break
            else:
                ans += 1
        else:
            imp.append((ci, cv))
        