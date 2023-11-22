def solution(survey, choices):
    answer = ''
    d = dict()
    d['R'] = 0
    d['T'] = 0
    d['C'] = 0
    d['F'] = 0
    d['J'] = 0
    d['M'] = 0
    d['A'] = 0
    d['N'] = 0
    n = len(survey)
    for i in range(n):
        a, b = survey[i][0], survey[i][1]
        point = choices[i] - 4
        
        if point < 0:
            d[a] += -point
        elif point > 0: 
            d[b] += point
    
    if d["R"] >= d["T"]:
        answer += "R"
    else:
        answer += "T"
    if d["C"] >= d["F"]:
        answer += "C"
    else:
        answer += "F"
    if d["J"] >= d["M"]:
        answer += "J"
    else:
        answer += "M"
    if d["A"] >= d["N"]:
        answer += "A"
    else:
        answer += "N"
            
    return answer