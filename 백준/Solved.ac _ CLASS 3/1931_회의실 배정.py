import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    temp = list(map(int, input().rstrip().split()))
    arr.append(temp)

#dfs -> 시간초과
# def dfs(depth, end, cnt):
#     if depth == N-1: return cnt
#     for i in range(depth+1, len(arr)):
#         if arr[i][0] >= end:
#             return dfs(i, arr[i][1], cnt+1)
        
#     return cnt

# mm = dfs(0, arr[0][1], 1)

# for i in range(1, N):
#     mm = max(mm, dfs(i, arr[i][1], 1))
# print(mm)

#dp -> 시간초과
# dp = [0 for _ in range(N)]
# dp[0] = 1

# for i in range(1, len(arr)):
#     mm = 1
#     for j in range(i-1, -1, -1):
#         if arr[i][0] >= arr[j][1]:
#             mm = max(mm, dp[j]+1)
#     dp[i] = mm
# print(max(dp))

arr.sort(key= lambda x : (x[1], x[0]))

endTime = arr[0][1]
cnt = 1
for i in range(1, len(arr)):
    if endTime <= arr[i][0]:
        cnt +=1
        endTime = arr[i][1]
print(cnt)

