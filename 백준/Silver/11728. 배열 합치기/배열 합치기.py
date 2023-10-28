import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rsplit())
ans = []
arr1 = deque(list(map(int, input().rsplit())))
arr2 = deque(list(map(int, input().rsplit())))

while arr1 or arr2:
    if arr1 and arr2:
        if arr1[0] <= arr2[0]:
            ans.append(arr1.popleft())
        else:
            ans.append(arr2.popleft())
    else:
        if arr1:
            ans.append(arr1.popleft())
        else:
            ans.append(arr2.popleft())
            
print(*ans)