import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
arr = [False for _ in range(G)]
ans = 0

"""
#시간초과 
for _ in range(P):
    check = False
    
    n = int(input()) - 1
    for i in range(n, -1, -1):
        if arr[i] == False:
            arr[i] = True
            ans += 1
            check = True
            break
    if not check:
        break
"""
ans = 0
nums = [0 for _ in range(G)]
for _ in range(G):
    check = True
    a = int(input()) - 1
    cur = a
    nums[a] += 1 

    if nums[a] > a+1 :
        break
    temp = nums[a] -1
    cnt = 0
    while temp != 0:
        cnt += temp
        a -= 1
        temp = nums[a]
    for i in range(cur-cnt, -1, -1):
        if arr[i] == False:
            check = False
            arr[i] = True
            ans += 1
            break
    
    if check:
        break
    
print(ans)