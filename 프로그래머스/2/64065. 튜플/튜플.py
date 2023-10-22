def preprocess(s: list):
    temp = s[2:]
    temp = temp.split("{")
    
    for i in range(len(temp)):
        temp[i] = list(map(int, temp[i][:-2].split(",")))
    
    return temp
def solution(s):
    answer = []
    splited = preprocess(s)
    
    if len(splited) == 1:
        return splited[0]
    
    splited.sort(key = lambda x: len(x))
    for i in splited:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer