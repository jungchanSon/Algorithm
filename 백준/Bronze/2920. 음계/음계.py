data = list(map(int, input().rsplit()))

asc = [1,2,3,4,5,6,7,8]
des = asc[::-1]

if data == asc:
    print("ascending")
elif data == des:
    print("descending")
else :
    print("mixed")