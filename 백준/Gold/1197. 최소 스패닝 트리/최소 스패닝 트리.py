import sys
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
graph = []
cycle_table = [i for i in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().rstrip().split())
    graph.append((w, s, e))

graph.sort(reverse=True)


cnt = V-1
sum_weight = 0
def find(x):
    if cycle_table[x] == x:
        return x
    cycle_table[x] = find(cycle_table[x])
    return cycle_table[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        cycle_table[b] = a
    else:
        cycle_table[a] = b
        
while cnt != 0:
    w, s, e = graph.pop()
    if find(s) != find(e):
        union(s, e)
        cnt -= 1
        sum_weight += w
print(sum_weight)