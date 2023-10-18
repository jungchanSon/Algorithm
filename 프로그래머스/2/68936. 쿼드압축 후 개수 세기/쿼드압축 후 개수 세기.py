def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def bt(arr: list, n: int):
        s = 0
        a1 = arr[:n//2]
        a2 = arr[:n//2]
        a3 = arr[n//2:]
        a4 = arr[n//2:]
        
        for i in range(n//2):
            a1[i] = a1[i][:n//2]
            a2[i] = a2[i][n//2:]
            a3[i] = a3[i][:n//2]
            a4[i] = a4[i][n//2:]
        s = 0
        
        for i in arr:
            s += sum(i)
            
        if s == 0:
            answer[0] += 1
            return
        elif s == n**2:
            answer[1] += 1
            return
        bt(a1, n//2)
        bt(a2, n//2)
        bt(a3, n//2)
        bt(a4, n//2)
                
    bt(arr, n)
    return answer