from itertools import product

def solution(users, emoticons):
    answer = [0 , 0]
    
    sale = [10, 20, 30, 40]
    for s in product(sale, repeat=len(emoticons)):
        total1, total2 = 0, 0
        for u1, u2 in users:
            p = 0
            for i, e in enumerate(emoticons):
                if s[i] >= u1:
                    p += e * (100-s[i]) / 100
            if p >= u2:
                total1 += 1
            else: 
                total2 += p
        if answer[0] < total1:
            answer[0] = total1
            answer[1] = total2
        elif answer[0] == total1 and answer[1] < total2:
            answer[1] = total2
    return answer