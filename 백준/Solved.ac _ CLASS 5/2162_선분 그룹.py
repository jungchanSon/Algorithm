import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    arr.append((x1, y1, x2, y2))

union_find_table = [i for i in range(N)]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a > b:
        union_find_table[a] = b
    else:
        union_find_table[b] = a
        
def find(x):
    if x == union_find_table[x]:
        return x
    
    union_find_table[x] = find(union_find_table[x])
    return union_find_table[x]

# def check_cross(a, b):
#     x11, y11, x12, y12 = a
#     x21, y21, x22, y22 = b
    
#     f1= (x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)
#     f2= (x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)
    
#     if f1 * f2 <= 0 : 
#         return True
#     else :
#         return False

def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    
    s = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
    
    if s > 0:
        return 1
    elif s == 0:
        return 0
    else:
        return -1

def check_cross(a, b):
    x1, y1, x2, y2 = a
    x3, y3, x4, y4 = b
    p1p2 = ccw([x1, y1], [x2, y2], [x3, y3]) * ccw([x1, y1], [x2, y2], [x4, y4])
    p3p4 = ccw([x3, y3], [x4, y4], [x1, y1]) * ccw([x3, y3], [x4, y4], [x2, y2])
    if p1p2 <= 0 and p3p4 <= 0:
        if p1p2 == 0 and p3p4 == 0:
            # max_p1p2 = max(x1, x2)
            # max_p3p4 = max(x3, x4)
            # min_p1p2 = min(x1, x2)
            # min_p3p4 = min(x3, x4)
            
            
            #  https://www.acmicpc.net/board/view/112112
            #  이 부분이 문제였다...
            if max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min (y1, y2) :
                return True
            else:
                return False
            
        else:
            return True
    else : 
        return False
        

for i in range(N-1):
    for j in range(i+1, N):
        if find(i) != find(j) and check_cross(arr[i], arr[j]):
            union(i, j)
            # check_result = check_cross(arr[i], arr[j])
            # p1p2 = ccw([arr[i][0], arr[i][1]], [arr[i][2], arr[i][3]], [arr[j][0], arr[j][1]]) * ccw([arr[i][0], arr[i][1]], [arr[i][2], arr[i][3]], [arr[j][2], arr[j][3]])
            # p3p4 = ccw([arr[j][0], arr[j][1]], [arr[j][2], arr[j][3]], [arr[i][0], arr[i][1]]) * ccw([arr[j][0], arr[j][1]], [arr[j][2], arr[j][3]], [arr[i][2], arr[i][3]])
            # if p1p2 <= 0 and p3p4 <= 0:
            #     if p1p2 == 0 and p3p4 == 0:
            #         max_p1p2 = max(arr[i][0], arr[i][1])
            #         max_p3p4 = max(arr[j][0], arr[j][1])
            #         min_p1p2 = min(arr[i][0], arr[i][1])
            #         min_p3p4 = min(arr[j][0], arr[j][1])
                    
            #         if min_p3p4 <= max_p1p2 and min_p1p2 <= max_p3p4 :
            #             union(i, j)
            #     else:
            #         union(i, j)
            
for i in range(N):
    union_find_table[i] = find(union_find_table[i])
counter = Counter(union_find_table)
print(len(counter))
print(max(counter.values()))


"""
    1차 실패.
    
    두 선분의 양분 공식 : https://crazyj.tistory.com/140
    f1 * f2 < 0
    f1= (x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)
    f2= (x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)
    
    
    2차 CCW(Counter Clock Wise) 알고리즘 이용 : https://killerwhale0917.tistory.com/6
    2차원 평면 상 3개의 점에 대한 방향성을 구하는 알고리즘.
    이를 이용해, 선분의 교차 여부 check
    
    - 기본 아이디어 : 3점의 벡터의 외적을 이용.
    1. 벡터 AB, AC의 외적 계산.
    2. 외적의 결과값 -> 세 점의 방향성을 판단
    
    교차 판단 조건:
    1. p1p2 = ccw(a,b,c)*ccw(a,b,d) <= 0
    2. p3p4 = ccw(c,d,a)*ccw(c,d,b) <= 0
    3. p1p2 == 0 && p3p4 == 0 
       => if p1 > p2 : swap (p1, p2)
          if p3 > p4 : swap (p3, p4)
          return p3 <= p2 && p1 <= p4
"""

"""
# https://www.acmicpc.net/board/view/112112
# https://www.acmicpc.net/board/view/91251

한번더 압축해야함

why? 
a와 b 간, 최초 union => a-b
이후, b와 c간 union => a-b b-c

==> 한번더 union ==> a-b-c가 된다.
"""

