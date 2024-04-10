def solution(s):
    answer = []
    set_ = set()
    dict_ = dict()
    
    for i in range(len(s)):
        c = s[i]
        if c not in set_:
            print(set_, c)
            set_.add(s[i])
            dict_[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - dict_[c])
            dict_[s[i]] = i
    return answer