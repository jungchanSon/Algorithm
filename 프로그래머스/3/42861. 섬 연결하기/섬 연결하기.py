def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [False for _ in range(n)]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    parent = [i for i in range( n+1)]
    
    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b :
            parent[b] = a
        else:
            parent[a] = b
            
    for i, j, k in costs:
        if find(i) != find(j):
            union(i, j)
        else: 
            continue
        answer += k
    return answer