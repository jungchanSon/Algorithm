import sys
input = sys.stdin.readline

n = int(input())
items = list(map(int, input().rstrip().split()))

m = int(input())
check = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(80001)]
s = 0
def rec(cnt, w):
    if dp[w] == 0:
        dp[w] = 1
    else : 
        return
    if cnt >= n :
        return
    
    rec(cnt+1, w+items[cnt])
    rec(cnt+1, items[cnt])
    rec(cnt+1, w-items[cnt])
    
rec(0, 40000)

for i in check:
    if dp[i+40000] == 0:
        print("N", end=" ")
    else : 
        print("Y", end=" ")
        
# 참고 : https://www.acmicpc.net/board/view/56807 