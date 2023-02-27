import sys
from math import inf
input = sys.stdin.readline

s = input().rstrip()
l = len(s)
dp = [inf for _ in range(l+1)]
dp[-1] = 0
def patition_palindrome(s):
    is_palindrome = [[False for _ in range(l)] for _ in range(l)]

    for i in range(l):
        is_palindrome[i][i] = True
    
    for i in range(1, l):
        if s[i] == s[i-1]:
            is_palindrome[i-1][i] = True 
    
    for i in range(2, l):
        for start in range(l-i):
            end = start + i 
            if s[start] == s[end] and is_palindrome[start+1][end-1]:
                is_palindrome[start][end] = True
            
    return is_palindrome
result = patition_palindrome(s)


for i in range(l):

    for j in range(i+1):
        if result[j][i]:
            dp[i] = min(dp[i], dp[j-1] + 1)
print(dp[l-1])

#도움 : https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80
#       https://yabmoons.tistory.com/592
"""
DP이용.

1. 길이가 1인 펠린드롬
2. 길이가 2인 펠린드롬 (AA, BB ...)
3. 길이가 3이상인 펠린드롬 (ABA, BCB ...)
    3-1. 처음 == 끝 
    3-2. 그 사이가 펠린드롬
"""