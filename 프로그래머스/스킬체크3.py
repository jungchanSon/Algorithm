def solution(n, stations, w):
    answer = 0
    
    for i in range(len(stations)):
        stations[i] -= 1

    temp = []
    for station in stations:
        start = station-w
        end = station+w+1
        temp.append((start, end))

    need = []
    
    pe = 0
    for i in range(len(temp)):
        s, e = temp[i]
        if i == len(temp) -1:
            v = n - e
            if v > 0:
                need.append(v)
        if s <= 0 :
            pe = e
            continue
        if pe > s :
            pe = e
            continue
        need.append(s - pe)
        
        pe = e

    maxN = w*2 +1
    
    for i in need:
        answer += i //maxN
        if i % maxN > 0:
            answer += 1 
    return answer

data1 = [11, [4, 11], 1]
data2 = [16, [9], 2]
print(solution(data1[0], data1[1], data1[2]))
print(solution(data2[0], data2[1], data2[2]))