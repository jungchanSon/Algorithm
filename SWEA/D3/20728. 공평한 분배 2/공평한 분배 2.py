import math
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().rsplit())
    candy = list(map(int, input().rsplit()))
    candy.sort()
    l = 0
    r = K-1
    if K == N:
        print("#"+str(test_case), candy[-1] - candy[0])
        continue
    
    ans = math.inf
    for _ in range(N-r):
        ans = min(ans, candy[r] - candy[l])
        l += 1
        r += 1
        
    print("#"+str(test_case), ans)