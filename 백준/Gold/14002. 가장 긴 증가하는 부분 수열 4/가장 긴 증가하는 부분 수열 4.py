import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rsplit()))
dp = [[1, -1] for _ in range(n)]
dp2 = {}
for i in range(1, n):
    cur = 0
    index = 0
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            cur = max(cur, dp[j][0])
            if cur == dp[j][0]:
                index = j
    if cur :
        dp[i][0] += cur
        dp[i][1] = index

ms, mi = max(dp)
print(ms)
ans = [arr[dp.index(max(dp))]]
while mi != -1:
    ans.insert(0, arr[mi])
    mi = dp[mi][1]

print(*ans)