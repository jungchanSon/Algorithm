n = int(input())
datas = [input().rsplit() for _ in range(n)]

for i in range(n):
    cnt, s = datas[i]
    ans = ''
    for j in s:
        ans += j*int(cnt)
    print(ans)