def solution(genres, plays):
    answer = []
    d = dict()
    reverse_d = dict()
    dict_genres = dict()
    for i in range(len(genres)):
        if d.get(genres[i]):
            d[genres[i]]+= plays[i]
            dict_genres[genres[i]].append((i, plays[i]))
        else:
            d[genres[i]] = plays[i]
            dict_genres[genres[i]] = []
            dict_genres[genres[i]].append((i, plays[i]))

    
    for key in dict_genres.keys():
        dict_genres[key].sort(key = lambda x:x[1], reverse=True)
    print(dict_genres)
    for key in d.keys():
        reverse_d[d[key]] = key
    
    v = list(d.values())
    v.sort(reverse = True)
    for i in v:
        genre = reverse_d[i]
        target = dict_genres[genre]
        
        if len(target) >=2:
            for i in target[:2]:
                answer.append(i[0])
        else:
            for i in target:
                answer.append(i[0])
    
    return answer