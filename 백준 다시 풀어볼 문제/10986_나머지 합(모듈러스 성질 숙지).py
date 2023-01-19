import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
data = list(map(int, input().rstrip().split()))

cnt = [0 for _ in range(m)]

total = 0
for i in range(n):
    total = (total + data[i]) % 3 
    cnt[total] += 1
    
s = cnt[0]
for i in range(len(cnt)):
    s += cnt[i] * (cnt[i]-1)//2

print(s)