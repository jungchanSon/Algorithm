import sys
import math
input = sys.stdin.readline

N = int(input())
arr = []
union_find_table = [i for i in range(N+1)]

for _ in range(N):
    arr.append(list(map(float, input().rstrip().split())))

def find(x):
    if x == union_find_table[x]:
        return x
    
    union_find_table[x] = find(union_find_table[x])
    return union_find_table[x]

def union(x, y):
    x = union_find_table[x]
    y = union_find_table[y]

    if x > y:
        union_find_table[x] = y
    else:
        union_find_table[y] = x
        
def cal_dist(x, y):
    dist = math.sqrt(abs(x[0] - y[0])**2 + abs(x[1] - y[1])**2)
    return dist

q = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dist = cal_dist(arr[i], arr[j])
        q.append((dist, i+1, j+1))
q.sort(reverse= True)

cnt = N-1
ans = 0

while cnt:
    cur = q.pop()

    if find(cur[1]) != find(cur[2]):
        union(cur[1], cur[2])
        ans += cur[0]
        cnt -=1
        
print(round(ans, 2))