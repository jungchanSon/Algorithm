import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
Nums = list(map(int, input().split()))
Seq = [0 for _ in range(len(Nums)+1)]

for i in range(1, len(Seq)):
    Seq[i] = Nums[i-1] + Seq[i-1]
    
for _ in range(M):
    
    i, j = list(map(int, input().split()))
    
    print(Seq[j]-Seq[i-1])