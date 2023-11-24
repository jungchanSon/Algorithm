def solution(new_id: str):
    answer = ''
    
    new_id = new_id.lower()
    tmp = ""
    for i in range(len(new_id)):
        if new_id[i].isalnum() or new_id[i] == '-' or new_id[i] == "_" or new_id[i] == ".":
            if i > 0 and new_id[i] == "." and tmp and tmp[-1] == ".":
                continue
            else:
                tmp += new_id[i]

    if tmp and tmp[0] == ".":
        tmp = tmp[1:]
    if tmp and tmp[-1] == ".":
        tmp = tmp[:-1]
    if len(tmp) == 0:
        tmp = "aaa"
    
    if len(tmp) >= 16:
        tmp = tmp[:15]
    if tmp and tmp[-1] == ".":
        tmp = tmp[:-1]
    
    if len(tmp) <= 2:
        while len(tmp) != 3:
            tmp += tmp[-1] 
    print(tmp)
    return tmp

