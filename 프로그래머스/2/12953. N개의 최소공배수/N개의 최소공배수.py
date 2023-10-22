def solution(arr):
    if len(arr) == 1:
        return arr[0]
    answer = 0
    arr.sort()
    
    for _ in range(len(arr)):
        poped = arr.pop(0) 
        for i in arr:
            if i % poped == 0:
                break
            if i == arr[-1]:
                arr.append(poped)
                break
    
    def gcd(a, b):
        r = 0
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    
    def lcd(a, b):
        return a * b / gcd(a, b)
    
    a = arr.pop(0)
    b = arr.pop(0)
    
    answer = lcd(a, b)
    while arr:
        p = arr.pop()
        answer = lcd(answer, p)
    return answer