import sys 
input = sys.stdin.readline

n = int(input())
book_dict = dict()

for _ in range(n):
    book = input()
    if book_dict.get(book):
        book_dict[book] += 1
    else:
        book_dict[book] = 1

mx = -1
ans = str()
for key in book_dict.keys():
    if book_dict[key] > mx:
        mx = book_dict[key]
        ans = key
        
    elif book_dict[key] == mx:
        ans = sorted([ans, key])[0]
        
print(ans)