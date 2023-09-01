import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rsplit()))
arr.sort()


l = 0
r = n -1
ans = abs(arr[l] + arr[r])
a = arr[l]
b = arr[r]
while l < r:
    
    s = arr[l] + arr[r]
    if s ==  0:
        a = arr[l]
        b = arr[r]
        break
    if abs(s) < ans:
        ans = abs(s)
        a = arr[l]
        b = arr[r]
    if s < 0 :
        l += 1
    else :
        r -= 1   
answer = [a, b]
answer.sort()
print(answer[0], answer[1])
        