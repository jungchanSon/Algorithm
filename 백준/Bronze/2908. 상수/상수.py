data = input().rsplit()

data[0] = int(data[0][::-1])
data[1] = int(data[1][::-1])

print(max(data))