import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().rstrip().split())) for _ in range(N)]

area = 0
for i in range(N-1):
    area += points[i][0] * points[i+1][1]
area += points[0][1]*points[N-1][0]

for i in range(N-1):
    area -= points[i][1] * points[i+1][0]
area -= points[0][0]*points[N-1][1]

ans = round(abs(area) / 2, 1)
print(ans)


"""
신발끈 공식 이용.
https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D

"""