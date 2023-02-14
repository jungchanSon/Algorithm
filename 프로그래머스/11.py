def solution(s):
    answer = 0

    s = list(s)
    l = len(s)
    check = True
    if l % 2 == 1: 
        return 0
    for _ in range(l//2 ):
        print(s)
        if not s :
            return 1
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                check = True
                break
            check = False

    if s:
        answer = 0
    else : 
        answer = 1
    return answer


print(solution("baabaa"))
print(solution("cdcd"))
