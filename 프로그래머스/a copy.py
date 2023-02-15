def solution(tickets):
    answer = []
    visited = [False for _ in range(len(tickets))]

    def dfs(i, s, e, path):
        # if visited[i]:
        #     return
        # visited[i] = True
        
        if len(path) == len(tickets)+1:
            answer.append(path)
        for j in range(len(tickets)):
            start, end = tickets[j]
            if e == start and visited[j] == False:
                visited[j] = True
                dfs(j, start, end, path+[end])
                visited[j] = False
    for i in range(len(tickets)):
        s, e = tickets[i]
        if s == "ICN": 
            visited = [False for _ in range(len(tickets))]
            dfs(i, s, e, [s, e])

    answer.sort()
    return answer[0]


tickets = [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"],["ATL", "ICN"], ["ATL","SFO"]]]

for i in tickets:
    print(solution(i))