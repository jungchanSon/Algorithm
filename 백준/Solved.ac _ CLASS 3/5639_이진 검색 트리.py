import sys
from collections import deque
sys.setrecursionlimit(10001)
input = sys.stdin.readline

arr = []

while True:
    try: arr.append(int(input().rstrip()))
    except: break

q = deque()

def post_order(pre_start, pre_end):
    if pre_start > pre_end :
        return None

    root = arr[pre_start]
    middle_index = pre_end+1
    
    for i in range(pre_start, pre_end+1):
        if arr[i] > root:
            middle_index = i
            # print (middle_index)
            break
        
    post_order(pre_start+1, middle_index-1)
    post_order(middle_index, pre_end)
    q.append(root)
    
post_order(0, len(arr) -1)
while q:
    print(q.popleft())