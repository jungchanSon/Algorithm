data = list(map(int, input().rsplit()))
sum_ = 0
for i in data:
    sum_ += i*i
ans = sum_%10
print(ans)