import sys
import math
input = sys.stdin.readline

n = int(input())
arr = [i for i in range(n+1)]
for i in range(2, int(math.sqrt(n))+1 ):
    if arr[i] == 0:
        continue
    for j in range(i*i, n+1, i):
        arr[j] = 0
arr[0] = 0
arr[1] = 0

prime_list = []
for i in arr:
    if i:
        prime_list.append(i)

dp = [0 for _ in range(n+1)]
for i in range(len(prime_list)):
    sum_all = prime_list[i]
    dp[sum_all] += 1
    
    for j in range(i+1, len(prime_list)):
        sum_all += prime_list[j]
        if sum_all > n:
            break
        dp[sum_all] += 1
print(dp[-1])