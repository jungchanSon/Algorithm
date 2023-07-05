n = int(input())
stack = list(map(int, input().rsplit()))
origin = stack.copy()

temp = []
ans = []
current = stack.pop()
ans.append(-1)
temp.append(current)

nums = [ 0 for _ in range(1000001)]
for i in origin:
    nums[i] += 1
    
while stack:
    current = stack.pop()
    
    while temp:
        tar = temp.pop()
        tar_num = nums[tar]
        cur_num = nums[current]
        
        if tar_num > cur_num:
            ans.append(tar)
            temp.append(tar)
            temp.append(current)
            break

    if not temp:
        ans.append(-1)
        temp.append(current)

    
print(*ans[::-1])
