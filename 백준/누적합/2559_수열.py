import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
Nums = list(map(int, input().split()))
Seq = [0 for _ in range(len(Nums)+1)]

for i in range(1, len(Seq)):
    Seq[i] = Nums[i-1] + Seq[i-1]

ans = []

for i in range(N-M+1):
    ans.append(Seq[i+M]-Seq[i])
print(max(ans))