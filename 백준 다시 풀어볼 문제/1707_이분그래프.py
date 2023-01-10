import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

k = int(input().rstrip())


def dfs(n) : 
    if visited[n] == -1:
        visited[n] = True
    print(12341234)
    if edgeList[n]:
        for i in edgeList[n]:
            if visited[i] == visited[n]:
                return False
            else :
                visited[i] = not visited[n]
                return dfs(i)
    return True
    
for _ in range(k):
    result = True
    
    v, e = list(map(int, input().rstrip().split()))

    edgeList = [[] for _ in range(v+1)]    
    visited = [-1 for _ in range(v+1)]
    
    for _ in range(e):
        edge = list(map(int, input().rstrip().split()))
        edgeList[edge[0]].append(edge[1])
        # edgeList[edge[1]].append(edge[0])
        
    for i in range(1, v+1):
        print(i)
        if visited[i] == -1:
            print("visi")
            print(dfs(i))
            print(123)
            if temp == False:
                result = temp
    if result:
        print("YES")
    else:
        print("NO")
        
    print(result)