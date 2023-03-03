import sys
import math
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
INF = math.inf


# 투 포인트
l_index = 0
r_index = N-1

total = INF
min_l_index = 0
min_r_index = 0

while l_index < r_index:
    l_value = arr[l_index]
    r_value = arr[r_index]
    
    sum_l_r = l_value + r_value
    
    if abs(sum_l_r) < total:
        total = abs(sum_l_r)
        min_l_index = l_index 
        min_r_index = r_index
    
    if l_value+r_value < 0:
        l_index += 1
    else:
        r_index -= 1    

print(arr[min_l_index], arr[min_r_index])