def solution(record):
    answer = []
    record_split = []
    d = dict()
    for i in record:
        record_split.append(i.split())
    
    for i in record_split:
        if i[0] == "Enter":
            d[i[1]] = i[2]
        elif i[0] == "Change":
            d[i[1]] = i[2]
    
    for i in record_split:
        if i[0] == "Enter":
            answer.append(d[i[1]]+"님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(d[i[1]]+"님이 나갔습니다.")
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))