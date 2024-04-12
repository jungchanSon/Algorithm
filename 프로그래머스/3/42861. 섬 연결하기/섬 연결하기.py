def solution(n, costs):
    answer = 0
    p = [i for i in range(n+1)]
    
    def find(x):
        if x == p[x]:
            return x
        p[x] = find(p[x])
        return p[x]
    
    def union(x, y):
        x, y = find(x), find(y)
        
        if x < y :
            p[y] = x
        else:
            p[x] = y
            
    costs.sort(key=lambda x: x[2])
    print(costs)
    
    while costs:
        a, b, c = costs.pop(0)
        a += 1
        b += 1
        if find(a) != find(b):
            union(a, b)
            answer += c
    return answer