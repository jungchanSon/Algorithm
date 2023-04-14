def solution(n, wires):
    answer = []
    
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(current):
        s = 0
        if visited[current] == False:
            visited[current] = True
            s += 1
        else :
            return 0
        next_nodes = graph[current]
        for i in next_nodes:
            s += dfs(i)
        return s
    
    for i in range(len(wires)):
        visited = [False for _ in range(n+1)]
        a= wires[i][0]
        b= wires[i][1]
        graph[a].remove(b)
        graph[b].remove(a)
        n1 = dfs(a)
        n2 = dfs(b)
        graph[a].append(b)
        graph[b].append(a)
        answer.append(abs(n1-n2))
    return min(answer)