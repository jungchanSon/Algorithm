import sys
input = sys.stdin.readline

q = []
ans = 0
data = input().rstrip()

for i in range(len(data)):
    if data[i] == "(":
        q.append(i)
    
    if data[i] == ")":
        if data[i-1] == ")":
            q.pop()
            ans += 1
        else :
            q.pop()
            ans += len(q)
            
print(ans)