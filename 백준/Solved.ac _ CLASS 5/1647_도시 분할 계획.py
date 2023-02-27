import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
heap = []
union_find_table = [i for i in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().rstrip().split())
    heapq.heappush(heap, (C, A, B))

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        union_find_table[a] = find(b)
    else:
        union_find_table[b] = find(a)
        
def find(n):
    if union_find_table[n] == n:
        return n
    
    union_find_table[n] = find(union_find_table[n])
    
    return union_find_table[n]

cnt = N -1
ans = 0
while cnt > 1:
    c, a, b = heapq.heappop(heap)
    if find(a) != find(b):
        ans += c
        union(a, b)
        cnt -= 1
print(ans)