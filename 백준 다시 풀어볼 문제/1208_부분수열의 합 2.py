import sys
from itertools import combinations

input = sys.stdin.readline
N, S = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
ans = 0

len_left = N//2
len_right = N - len_left

#00 01 10 11
left = [0 for _ in range(1<<len_left)]
for i in range(1<<len_left):
    for k in range(len_left):
        if i & (1<<k):
            left[i] += arr[k]

right = [0 for _ in range(1<<len_right)]
for i in range(1<<len_right):
    for k in range(len_right):
        if i & (1<<k):
            right[i] += arr[len_left+k]

left.sort()
right.sort(reverse=True)
left_index = 0
right_index = 0
while left_index < len(left) and right_index < len(right):
    left_num = left[left_index]
    right_num = right[right_index]

    sum_num = left_num + right_num
    
    if sum_num < S:
        left_index += 1
    elif sum_num > S:
        right_index += 1
    else:
        # c1 = 1
        # c2 = 1 
        # left_index += 1 
        # right_index += 1
        
        # while left_index < len(left) and left[left_index] == left[left_index-1]:
        #     c1 += 1 
        #     left_index += 1
        # while right_index < len(right) and right[right_index] == right[right_index-1]:
        #     c2 += 1 
        #     right_index += 1
        # ans += c1*c2
        
        l_cnt = 0
        r_cnt = 0
        for l in range(left_index, len(left)):
            if left[l] == left_num:
                l_cnt += 1
            else:
                break
        for r in range(right_index, len(right)):
            if right[r] == right_num:
                r_cnt += 1
            else:
                break
        left_index += l_cnt
        right_index+= r_cnt
        ans += l_cnt * r_cnt
if S == 0:
    ans -= 1
print(ans)

#도움 : https://peisea0830.tistory.com/40
#       https://lshdv.tistory.com/34
  
  
#--------------시간초과--------------      
# left = arr[:N//2]
# right = arr[N//2:]

# left_result = []
# right_result = []
# for i in range(1, len(left)+1):
#     for j in combinations(left, i):
#         left_result.append(sum(j))
# for i in range(1, len(right)+1):
#     for j in combinations(right, i):
#         right_result.append(sum(j))
        
# left_result.sort()
# right_result.sort(reverse=True)

# left_index = 0
# right_index = 0
# ans = 0

# while left_index < len(left_result) and right_index < len(right_result):
#     left_value = left_result[left_index]
#     right_value = right_result[right_index]
    
#     result = left_value + right_value
#     if result < S:
#         left_index += 1
#     elif result > S:
#         right_index += 1 
#     else :
#         l_cnt = 0
#         for i in left_result[left_index:]:
#             if i == left_value:
#                 l_cnt += 1
#             else: 
#                 break
#         r_cnt = 0
#         for i in right_result[right_index:]:
#             if i == right_value:
#                 r_cnt += 1
#             else:
#                 break
#         ans += l_cnt * r_cnt

#         left_index += l_cnt
#         right_index += r_cnt
# print(ans)