import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().rstrip().split()))
M = int(input())
B = list(map(int, input().rstrip().split()))

result_a = []
for i in range(N):
    sum_a = 0
    for j in range(i, N):
        sum_a += A[j]
        remain = T - sum_a
        result_a.append(remain)

result_b = []
for i in range(M):
    sum_b = 0
    for j in range(i, M):
        sum_b += B[j]
        result_b.append(sum_b)
        
count_a = Counter(result_a)
count_b = Counter(result_b)

ans = 0
for i in count_a:
    ans += count_b[i] * count_a[i]
print(ans)


# a_index = 0
# b_index = 0
# ans = 0

# while a_index < len(result_a) and b_index < len(result_b):
#     if result_a[a_index] == result_b[b_index]:
#         cnt_b = 0
#         for i in range(b_index, len(result_b)):
#             if result_a[a_index] == result_b[i]:
#                 cnt_b += 1

#         cnt_a = 0
#         for i in range(a_index, len(result_a)):
#             if result_a[a_index] == result_a[i]:
#                 cnt_a += 1
                
#         ans += cnt_b * cnt_a
        
#         a_index += cnt_a
#         b_index += cnt_b
        
#     elif result_a[a_index] > result_b[b_index]:
#         b_index += 1
#     else:
#         a_index += 1
# print(ans)