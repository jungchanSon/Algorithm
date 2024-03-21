def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        temp = []
        for s in skill:
            si = st.find(s)
            temp.append(si)
        if -1 in temp:
            while temp and temp[-1] == -1:
                temp.pop()
            if -1 in temp:
                continue
        if temp == sorted(temp):
            answer += 1
        
    return answer