n, m = map(int, input().rsplit())
data = list(map(int, input().rsplit()))

r = max(data)
l = 0

ans = 0
cur = 0
while l <= r:
    mount = 0
    cur = (r+l) // 2
    for i in data:
        if i - cur > 0:
            mount += i - cur

    if mount >= m:
        ans = cur
        l = cur + 1
        
    else :
        r = cur - 1
print(ans)