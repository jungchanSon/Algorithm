import copy
def solution(cards):
    visited = [False for _ in range(len(cards))]

    point = 0
    
    def dfs(i, p):
        nonlocal point
        if visited[i] :
            point = p
            return         
        visited[i] = True
        dfs(cards[i]-1, p+1)
    
    ans = []
    
    for i in range(0, len(cards)):
        visited[i] = True
        point = 0
        dfs(cards[i]-1, 1)

        ans.append(point)
    print(ans)

    ans.sort()
    answer = ans[-1] * ans[-2]
    
    
    return answer

print(solution([8,6,3,7,2,5,1,4]))

