import sys
from collections import Counter
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
len_a = len(bin(A)) -2
len_b = len(bin(B)) -2 
bin_a = bin(A)[2:]
bin_b = bin(B)[2:]

dp = [0 for _ in range(len_b)]
dp[0] = 1

for i in range(1, len(dp)):
    dp[i] = dp[i-1] * 2 + (1<<i)
print(dp)

print(bin(B)[2:])
ans = 0
for i in range(len_b):
    temp = len_b - i
    if bin_b[i] == "1":
        print(temp)
        ans += dp[temp-2]
        ans += 2**(temp-2)
    if i == len_b-1 and bin_b[i] == 1:
        ans += 1
print(ans)
for i in range(len_a):
    temp = len_a - i
    if bin_a[i] == "1":
        ans -= dp[temp-2]
    if bin_a[i] == "1" and i == len_a -1:
        ans -= 1
print(ans)
"""
2 12 10
10
1000
1001
1010
1011
1 
1  1

2   3
10  11  2 1 1 4 
4   5   6   7
100 101 110 111 4 4 4 12
8       9       10      11      12      13      14      15
1000    1001    1010    1011    1100    1101    1110    1111 8 12 12 32
12 5 2 1 
16      17
10000   10001
"""