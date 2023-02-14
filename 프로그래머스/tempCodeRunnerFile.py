def solution(s):
    answer = -1

    s = list(s)
    l = len(s)
    check = True
    while check and s:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
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
