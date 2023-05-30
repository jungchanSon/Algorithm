def solution(tickets):
    answer = []
    visited = [False for _ in range(len(tickets))] 
    LEN_TICKET = len(tickets)
    ICN = "ICN"
    
    def dfs(current:str, path:list):
        if len(path) == LEN_TICKET+1:
            return answer.append(path)
        
        for i in range(LEN_TICKET):
            start = tickets[i][0]
            end = tickets[i][1]
            
            if current == start and visited[i] == False:
                visited[i] = True
                dfs(end, path+[end])
                visited[i] = False
                
        
    for i in range(len(tickets)):
        start = tickets[i][0]
        end = tickets[i][1]
        visited = [False for _ in range(len(tickets))] 
        
        if start == ICN:
            visited[i] = True
            dfs(end, [start, end])
            
    return min(answer)