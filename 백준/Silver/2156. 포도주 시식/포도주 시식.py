import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])
    quit()
elif n == 2: 
    print(arr[0]+arr[1])
    quit()
elif n == 3: 
    print(max(arr[0]+arr[1], arr[1]+arr[2], arr[0]+arr[2]))
    quit()
dp = [0 for _ in range(n)]
dp[0] = arr[0]
dp[1] = dp[0] + arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], arr[0]+arr[1])
for i in range(3, n): 
    dp[i] = max(dp[i-2] + arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1])
print(dp[-1])