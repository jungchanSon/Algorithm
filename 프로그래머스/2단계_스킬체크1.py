def solution(clothes):
    clothDict = {}
    for cloth, cType in clothes:
        if cType in clothDict.keys():
            clothDict[cType].append(cloth)
        else:
            clothDict[cType] = [cloth]
    print(clothDict)
    
    
    cKey = clothDict.keys()
    answer = 1 
    for i in cKey:
        l = len(clothDict[i])
        answer *= l+1

    answer -= 1
    
    return answer


data = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]], [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

for i in data:
    print(solution(i))