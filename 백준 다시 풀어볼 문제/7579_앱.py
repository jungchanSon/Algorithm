import sys
input = sys.stdin.readline

n , m = map(int, input().rstrip().split())
am = list(map(int, input().rstrip().split()))
c =  list(map(int, input().rstrip().split()))
dp = [[0 for _ in range(sum(c)+1)] for _ in range(n+1)]

# TODO : 재귀로 나중에 다시 고민해보기.

""" 
def recursion(memory, cost, depth):
    if dp[depth][cost]: 
        return dp[depth][cost]
    dp[depth][cost] =  memory
    if depth >= n :
        return 0

    n1 = recursion(memory+am[depth], cost+c[depth], depth+1)
    n2 = recursion(memory, cost, depth+1)

    dp[depth][cost] = max(n1, n2)
    return dp[depth][cost]
recursion(0, 0, 0)

"""

    
for i in range(1, len(dp)):
    for j in range(len(dp[0])):
        if j - c[i-1] >= 0:
            dp[i][j] = am[i-1]+dp[i-1][j-c[i-1]]
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        

# for i in dp:
#     print(i)
    
for i in range(len(dp[0])):
    if dp[n][i] >= m:
        print(i)
        break
    
#도움 : https://cocoon1787.tistory.com/319