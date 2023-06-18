K = int(input())
arr = []
for i in range(K):
    arr.append(int(input()))

stack = []

for i in arr:
    if i:
        stack.append(i)
    else:
        stack.pop()
        
print(sum(stack))
