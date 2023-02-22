import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
visited = [False for _ in range(N)]
arr.sort()

def bt(depth, l):
    global temp
    
    if depth == M:
        print(*l)
        return
        
    temp = -1
    
    for j in range(N):
        if arr[j] != temp:
            if l:
                if arr[j] >= l[-1]:
                    bt(depth+1, l+[arr[j]])
                    temp = arr[j] 
            else:
                bt(depth+1, l+[arr[j]])
                temp = arr[j] 
arr_set = set(arr)
arr_set = list(arr_set)
arr_set.sort()

# for i in range(len(arr_set)):
#     visited = [False for _ in range(N)]
# visited[i] = True
    
bt( 0, [])
    
