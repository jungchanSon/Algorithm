def solution(N, number):
    answer = 0
    if N == number:
        return 1
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        
    for cnt in range(2, 9):
        for i in range(1, cnt):
            for j in dp[i]:
                for k in dp[cnt-i]:
                    dp[cnt].add(j+k)
                    dp[cnt].add(j-k)
                    dp[cnt].add(j*k)
                    if k != 0 and j != 0 :
                        dp[cnt].add(j/k)
                        dp[cnt].add(k/j)
            if number in dp[cnt]:
                return cnt
    
    return -1 