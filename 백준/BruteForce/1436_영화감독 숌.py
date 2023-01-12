import sys
input = sys.stdin.readline 

n = int(input().rstrip())


#하나씩 더하면서 666 들어있는지 확인
k = '666'

while n:
    if '666' in k:
        n -= 1
    k = str(int(k) + 1)
    
print(int(k)-1)

# f_k = ['6','6','6']
# b_k = ['6','6','6']


# f_cnt = '0'
# b_cnt = '0'

# k = '666'
# for i in range(1, n):
#     digits = len(str(k))
    
#     a = int(str(int(f_cnt) + 1) + k)
#     b = int(k + str(int(b_cnt) + 1))
    
#     print(a, b)
    
#     kk = (min(a, b))
#     if a == b:
#         b_cnt = str(int(b_cnt)+1)
#         f_cnt = str(int(f_cnt)+1)
#     else : 
#         if kk == a:
#             f_cnt = str(int(f_cnt)+1)
#         else :
#             b_cnt = str(int(b_cnt)+1)
#             if b_cnt.
#     print(kk)