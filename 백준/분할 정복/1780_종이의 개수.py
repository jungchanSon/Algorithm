import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

negative = 0
zero = 0 
positive = 0
def recursion(array, length):
    global negative, zero, positive
        
    f = array[0][0]
    check = True
    for i in array:
        for j in i:
            if f != j:
                check = False;
    
    if check:
        if f == -1:
            negative += 1
        elif f == 0:
            zero += 1 
        elif f == 1:
            positive += 1
        return
    
    array1 = []
    array2 = []
    array3 = []
    unit = length//3
    for i in range(length):

        array1.append(array[i][:unit])
        array2.append(array[i][unit:unit*2])
        array3.append(array[i][unit*2:unit*3])

        if i % unit == unit-1:
            recursion(array1, unit)
            recursion(array2, unit)
            recursion(array3, unit)
            array1 = []
            array2 = []
            array3 = []
            
recursion(arr, N)

print(negative)
print(zero)
print(positive)