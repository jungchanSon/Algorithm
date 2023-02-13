from collections import deque

def solution(begin, target, words):
    
    answer = 51
    visited = [False for _ in range(len(words))]
   
    if target not in words:
        return 0
   
    def dfs(word, cnt):
        nonlocal answer
        q = deque()
        q.append((begin, 0))
        
        while q:
            w, p = q.popleft()
            if w == target:
                answer = min(answer, p)

            for i in range(len(words)):
                dif = 0
                for j in range(len(words[i])):
                    if w[j] != words[i][j]:
                        dif += 1
                if dif == 1:
                    if not visited[i] :
                        visited[i] = True
                        q.append((words[i], p+1))
                        
    dfs(begin, 0)
    
    if answer == 51:
        return 0
    else: 
        return answer
  
data1 = ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
data3 = ["hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"]]
data2 = ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]

print(solution(data1[0], data1[1], data1[2]))
print(solution(data2[0], data2[1], data2[2]))
print(solution(data3[0], data3[1], data3[2]))
