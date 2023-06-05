A, B = list(map(int, input().rsplit()))
data = list(map(int, input().rsplit()))

for i in data:
    if i < B:
        print(i, end= " ")