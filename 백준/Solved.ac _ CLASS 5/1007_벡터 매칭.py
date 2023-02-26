import sys
import math
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    P = []
    
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        P.append((a, b))
    
    combi_list = list(combinations(P, N//2))
    combi_len = len(combi_list)
    left_combi = combi_list[:combi_len//2]
    right_combi = combi_list[combi_len//2:]
    right_combi.reverse()
    ans = math.inf
    for i in range(combi_len//2):
        left_vector = [0, 0]
        right_vector = [0, 0]
        
        for x, y in left_combi[i]:
            left_vector[0] += x
            left_vector[1] += y
            
        for x, y in right_combi[i]:
            right_vector[0] += x
            right_vector[1] += y
            
        
        final_vector = [left_vector[0]-right_vector[0], left_vector[1]-right_vector[1]]
        ans = min(ans, math.sqrt(final_vector[0]**2 + final_vector[1]**2))

    print(ans)