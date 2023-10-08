def solution(n):
    arr = [0]
    cnt = 1
    while len(arr) <= 100:
        if cnt % 3 != 0 and '3' not in str(cnt):
            arr.append(cnt)
        cnt += 1
    
    return arr[n]