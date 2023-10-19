def solution(n):
    answer = []
    arr = []
    m = 0
    for i in range(1, n+1):
        arr.append([0]*i)
        m += i
    x, y = 0, 0
    cnt = n
    tmp = 0
    d = 1
    i = 1
    while i <= m:
        
        print(i)
        if d == 1:
            for j in range(i, i+cnt):
                arr[y][x] = j
                y += 1
            d = 2
            x += 1
            y -= 1
        elif d == 2:
            for j in range(i, i+cnt):
                arr[y][x] = j
                x += 1
            d = 3
            x -= 2
            y -= 1
        elif d == 3:
            for j in range(i, i+cnt):
                arr[y][x] = j
                x -= 1
                y -= 1
            d = 1
            y += 2
            x += 1
        i += cnt
        cnt -= 1
        
    for i in arr:
        for j in i:
            answer.append(j)
    return answer
"""
[1] 
[2][9]
[3][10][8]
[4][5][6][7]
"""