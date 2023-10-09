def solution(dartResult):
    answer = 0
    dartResult = list(dartResult)
    point_list = []
    
    while dartResult:
        n = ""
        while dartResult and dartResult[0].isnumeric():
            n += dartResult.pop(0)
        n = int(n)
        s = dartResult.pop(0)
        p = ""
        
        if dartResult:
            if dartResult[0] == "*" or dartResult[0] == "#":
                p = dartResult.pop(0)
        print(n, s, p)
        if s == "D":
            n **= 2
        elif s == "T":
            n **= 3
        
        if p == "#":
            n *= -1
        elif p == "*":
            n *= 2
            if point_list:
                point_list[-1] *= 2
        point_list.append(n)
    answer = sum(point_list)
    return answer