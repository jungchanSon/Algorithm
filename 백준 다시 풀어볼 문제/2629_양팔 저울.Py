import sys
input = sys.stdin.readline

n = int(input())
items = list(map(int, input().rstrip().split()))

m = int(input())
check = list(map(int, input().rstrip().split()))
ans = []
dp = [[0 for _ in range((i+1)*500+1)] for i in range(n+1)]
s = 0
def rec(cnt, w):
    if cnt >= n :
        return
    if dp[cnt][w] == 0:
        dp[cnt][w] = 1
    else : 
        return

    
    rec(cnt+1, w+items[cnt])
    rec(cnt+1, items[cnt])
    rec(cnt+1, w-items[cnt])
    
rec(0, 40000)

for i in check:
    if dp[n][i+40000] == 0:
        ans.append("N")
    else : 
        ans.append("Y")
print(" ".join(ans))
        
# 참고 : https://www.acmicpc.net/board/view/56807 
#       https://my-coding-notes.tistory.com/157#recentComments 