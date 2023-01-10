import sys

input = sys.stdin.readline

p = [0 for _ in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2
p[6] = 3
p[7] = 4
p[8] = 5
p[9] = 7
p[10]= 9
for i in range(11, 101):
    p[i] = p[i-2] + p[i-3]

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print(p[n])
    
    