import sys
input = sys.stdin.readline

N, B = map(int, input().rstrip().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

def multi_matrix(m1, m2):
    temp_matrix = [[0] * len(m1) for _ in range(len(m1))]
    s = 0
    for k in range(len(m1)):
        for i in range(len(m1)):
            s = 0
            for j in range(len(m1[i])):
                s += m1[k][j] * m2[j][i]
            temp_matrix[k][i] = s % 1000

    return temp_matrix

def matrix_pow(m, B):
    if B == 1 :
        return m
    
    else: 
        mat = matrix_pow(m, B//2)
        if B % 2 == 0:
            return multi_matrix(mat, mat)
        if B % 2 == 1:
            return multi_matrix(multi_matrix(mat, mat), m)
        
ans = matrix_pow(matrix, B)

for i in range(len(ans)):
    for j in range(len(ans[0])):
        ans[i][j] = ans[i][j] % 1000
        
for i in ans:
    print(*i)

"""
C^n -> | C^(n/2) * C^(n/2) 
       | C^((n-1)/2) * C^((n-1)/2) * C
"""