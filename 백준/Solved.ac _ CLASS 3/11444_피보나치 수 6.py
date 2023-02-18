import sys
input = sys.stdin.readline
N = int(input())

fib_matrix = [[1, 1], [1, 0]]

def multi_m(a, b):
    
    temp = [[0, 0], [0, 0]]
    for k in range(2):
        for i in range(2):
            s = 0
            for j in range(2):
                s += a[k][j] * b[j][i] % 1000000007
            temp[k][i] = s

    return temp

def pow_m(m, n) :
    if n == 1:
        return m

    else :
        mat = pow_m(m, n//2)

        if n % 2 == 0:
            return multi_m(mat, mat)
        else:
            return multi_m(multi_m(mat, mat), m)

temp = pow_m(fib_matrix, N)
temp[0][0] = temp[0][0] % 1000000007
temp[0][1] = temp[0][1] % 1000000007
temp[1][0] = temp[1][0] % 1000000007
temp[1][1] = temp[1][1] % 1000000007

print(temp[1][0])
#도움 : https://st-lab.tistory.com/252