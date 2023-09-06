import sys
import collections
input = sys.stdin.readline

n, k = map(int, input().rsplit())
dp = [[10**6, -1] for _ in range(max(k*2+1, n+1))]
visited = [False for _ in range(max(k*2+1, n+1))]
q = collections.deque()

q.append([n, 0, -1])
dp[n][0] = 0

while q:
    c, p, pp = q.popleft()
    if visited[c]: 
        continue

    dp[c][1] = pp
    visited[c] = True
    
    nx1 = c-1
    nx2 = c+1
    nx3 = c*2
    
    if nx1 >= 0 and nx1 <= k*2:
        dp[nx1][0] = min(p+1, dp[nx1][0])
    q.append([nx1, p+1, c])
    
    if nx2 >= 0 and nx2 <= k*2:
        dp[nx2][0] = min(p+1, dp[nx2][0])
  
        q.append([nx2, p+1, c])
    
    if nx3 >= 0 and nx3 <= k*2:
        dp[nx3][0] = min(p+1, dp[nx3][0])

        q.append([nx3, p+1, c])

print(dp[k][0])

cur = dp[k][1]
ans = [k]
while cur != -1:
    ans.append(cur)
    cur = dp[cur][1]
print(*ans[::-1])
