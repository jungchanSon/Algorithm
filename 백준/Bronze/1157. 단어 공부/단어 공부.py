data = input().rstrip().upper()
num_alpa = [0 for _ in range(ord('Z') - ord('A')+1)]

for i in data:
    index = ord(i) - ord('A')
    num_alpa[index] += 1
max_num = max(num_alpa)
if num_alpa.count(max_num)>1:
    print('?')
else:
    print(chr((num_alpa.index(max_num)) + ord('A')))
