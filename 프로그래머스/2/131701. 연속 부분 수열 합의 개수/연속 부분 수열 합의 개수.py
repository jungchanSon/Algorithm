def solution(elements):
    answer = 0
    l = len(elements)
    temp_ans = set()
    
    elements += elements[:-1]
    
    for i in range(1, l+1):
        for j in range(len(elements)-i):
            s = sum(elements[j: j+i])
            temp_ans.add(s)
    answer = len(temp_ans)
    return answer