def solution(n, t, m, p):
    answer = ''
    
    cnt = 0
    cnt2 = 1
    cur = ''
    while len(answer) < t: 
        temp = cnt
        cur = ''
        
        if temp == 0:
            cur = ['0']
        while temp:
            if temp % n == 10:
                cur += 'A'
            elif temp % n == 11:
                cur += 'B'
            elif temp % n == 12:
                cur += 'C'
            elif temp % n == 13:
                cur += 'D'
            elif temp % n == 14:
                cur += 'E'
            elif temp % n == 15:
                cur += 'F'
            else:
                cur += str(temp % n)
            temp //= n
        temp = list(cur)
        while temp and len(answer) < t:
            c = temp.pop() 
            if m == p and cnt2 % m == 0:
                answer += c
            elif cnt2 % m == p:
                answer += c
            cnt2 += 1
        cnt+= 1
    return answer