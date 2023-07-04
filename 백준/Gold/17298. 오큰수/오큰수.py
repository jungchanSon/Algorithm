n = int(input())
stack = list(map(int, input().rsplit()))

temp = []
ans = []
current = stack.pop()
ans.append(-1)
temp.append(current)

while stack:
    current = stack.pop()
    
    while temp:
        tar = temp.pop()
        if tar > current:
            ans.append(tar)
            temp.append(tar)
            temp.append(current)
            break

    if not temp:
        ans.append(-1)
        temp.append(current)

    
print(*ans[::-1])
