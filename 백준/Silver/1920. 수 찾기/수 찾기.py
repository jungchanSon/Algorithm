import sys
input = sys.stdin.readline

n = int(input().rstrip())
ns= list(map(int, input().rsplit()))
m = int(input().rstrip())
ms= list(map(int, input().rsplit()))

ns.sort()
for i in ms:
    left = 0
    right = len(ns)-1
    result = False

    while left <= right:
        mid = (left+right )// 2
        mid_value = ns[mid]
        if i < mid_value:
            right = mid -1
        elif i > mid_value:
            left = mid + 1
        else:
            result = True
            break
    
    if result:
        print(1)
    else:
        print(0)
            