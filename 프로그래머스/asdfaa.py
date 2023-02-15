def solution(tickets):
    visited = [False for _ in range(len(tickets))]
    ICN = []
    ans = []

    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            ICN.append((i, tickets[i]))
            
    def dfs(i, s, e, path, depth):
        # if visited[i]:
        #     return 
        # visited[i] =True
        
        # if False not in visited:
        #     ans.append(path)
        if depth == len(tickets): 
            ans.append(path)
        for j in range(len(tickets)):
            start = tickets[j][0]
            end = tickets[j][1]
            if e == start: 
                if not visited[j]:
                    visited[j] = True
                    dfs(j, start, end, path + [end], depth+1)
                    visited[j] = False

    for i in range(len(ICN)):
        visited = [False for _ in range(len(tickets))]
        
        index = ICN[i][0]
        start = ICN[i][1][0]
        end = ICN[i][1][1]
        
        dfs(index, start, end, [start, end], 1)
    
    ans.sort()
    
    return ans[0]



t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(t1))
print(solution(t2))