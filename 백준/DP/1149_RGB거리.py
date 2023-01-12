import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = []

for _ in range(n):
    d = list(map(int, input().rstrip().split()))
    data.append(d)
    

size = 2**(n-1)*3 
dp = [ 0 for _ in range(size)]
# dp[n] != dp[n-1]
# r -> g -> r -> b ... 


answer = -1
def rec(depth, c, sum) :
    global answer
    if depth >= n-1:
        if answer == -1:
            answer = sum
        elif sum < answer:
            answer = sum
        return
        
    for i in range(3):
        if i != c:
            rec(depth+1, i, sum+data[depth+1][i])
            
            
for i in range(3):
    rec(0, i, data[0][i])
    
print(answer)