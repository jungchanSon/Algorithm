import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
INF = 1e9


# 투 포인트
l_index = 0
r_index = N-1

total = INF
min_l_index = 0
min_r_index = 0

while l_index != r_index:
    l_value = arr[l_index]
    r_value = arr[r_index]
    
    if r_value <= 0:
        v1 = 0
        v2 = 0
        if r_index + 1 < N:
            v1 = r_value + arr[r_index+1]
        if r_index - 1 >= 0:
            v2 = r_value + arr[r_index-1]
        if v1 and abs(v1) < total :
            total = abs(v1)
            min_l_index = r_index
            min_r_index = r_index+1
        if v2 and abs(v2) < total:
            min_l_index = r_index-1
            min_r_index = r_index
        break
    if l_value >= 0:
        v1 = 0
        v2 = 0
        if l_index+1 < N:
            v1 = l_value + arr[l_index+1]
        if l_index-1 >= 0:
            v2 = l_value + arr[l_index-1]
        if v1 and abs(v1) < total:
            total = abs(v1)
            min_l_index = l_index
            min_r_index = l_index+1
        if v2 and abs(v2) < total:
            min_l_index = l_index-1
            min_r_index = l_index
        break
    total = min(total, abs(l_value + r_value))
    if total == abs(l_value + r_value):
        min_l_index = l_index
        min_r_index = r_index
    
    if abs(l_value) > abs(r_value):
        l_index +=1
    else:
        r_index -= 1

print(arr[min_l_index], arr[min_r_index])