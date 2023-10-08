def solution(arr):
    answer = []
    
    m = min(arr)
    mi = arr.index(m)
    arr.pop(mi)
    answer = arr
    return answer