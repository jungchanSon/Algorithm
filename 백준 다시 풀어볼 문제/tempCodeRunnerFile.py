import sys

input = sys.stdin.readline

n , m = list(map(int, input().rstrip().split()))
data = list(map(int, input().rstrip().split()))

cnt = [0 for _ in range(m)]
sum = 0
for i in range(n):
    sum = (sum + data[i]) % 3 
    cnt[sum] += 1
s = 0
for i in range(len(cnt)):
    s += cnt[i] * (cnt[i]-1)/2
s += cnt[0]

print(int(s))

#모듈러스 성질