def solution(word):
    answer = 0
    word = list(word)
    alpa = ['A', 'E', 'I', 'O', 'U']
    cnt = 0
    def dfs(cur):
        nonlocal cnt
        if cur == word:
            return cnt
        if len(cur) > 4:
            return
        
        for i in alpa:
            cur.append(i)
            cnt += 1
            a = dfs(cur)
            if a :
                return a
            cur.pop()
    answer = dfs([])
    
    return answer