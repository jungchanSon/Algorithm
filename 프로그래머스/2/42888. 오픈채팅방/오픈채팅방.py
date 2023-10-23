def solution(record):
    answer = []
    uid_name = {}
    
    for i in record:
        temp = i.split()
        op, uid, name = "", "", ""
        
        if len(temp) == 2:
            op, uid = temp
            answer.append([uid+"님이 나갔습니다.", uid])
        elif len(temp) == 3:
            op, uid, name = temp
            uid_name[uid] = name
            if op == "Enter":
                answer.append([uid+"님이 들어왔습니다.", uid])
    
    for i in range(len(answer)):
        uid = answer[i][1]
        data = answer[i][0]
        name = uid_name[uid]
        data = data.replace(uid, name)
        answer[i] = data
        
    return answer
