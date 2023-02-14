import sys

def solution(number, k):
    ans = []

    l = list(number)
    cnt = 0
    
    for i in range(len(number)-1):
        if cnt == k : 
            break
        m = max(l[i: i+k-cnt+1])
        
        index = l.index(m)
        
        l = l[:index]+l[index:]
        cnt += index - i
    while cnt != k:
        l.pop()
        cnt+=1 
    return "".join(l)

print(solution("943", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))