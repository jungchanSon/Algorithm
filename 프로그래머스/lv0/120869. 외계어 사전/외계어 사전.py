def solution(spell, dic):
    answer = 0
    
    for word in dic:
        for s in spell:
            if s not in word:
                break
            if s == spell[-1]:
                return 1
    
    return 2