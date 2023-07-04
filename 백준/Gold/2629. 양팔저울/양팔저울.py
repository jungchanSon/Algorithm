num = int(input())
weights = list(map(int, input().rsplit()))
check_num = int(input())
check_weight = list(map(int, input().rsplit()))

dp = [False for _ in range(40001)]
temp = []
visited = []
for w in weights:
    temp = []
    for i in range(40001):
        if dp[i] == True :
            temp.append(i+w)
            temp.append(max(w-i, i-w))
    dp[w] = True
            
    for i in temp:
        dp[i] = True 
                
for i in check_weight:
    if dp[i]:
        print("Y", end= " ")
    else:
        print("N", end = " ")