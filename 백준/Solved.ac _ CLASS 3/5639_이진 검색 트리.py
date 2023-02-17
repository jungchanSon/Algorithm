import sys
from collections import deque
input = sys.stdin.readline

arr = []

while True:
    try: arr.append(int(input().rstrip()))
    except: break

q = deque()
q.append(arr[0])

# for i in arr[1:]:
#     if q[-1] > i:
#         q.append(i)
#     else :
#         print(q.pop())

for i in range(1, len(arr[1:])):
    if q[-1] > arr[i]:
        q.append(arr[i])
        
    else :
        print(q.pop())
        q.append(arr[i])
        while q[-2] > arr[i] and q[-3] < arr[i]:
            print(q.pop())
            print(q.pop())

while q:
    print(q.pop())