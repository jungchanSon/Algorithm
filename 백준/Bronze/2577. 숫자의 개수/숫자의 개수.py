A = int(input())
B = int(input())
C = int(input())

mult = str(A*B*C)

for i in range( 10):
    print(mult.count(str(i)))