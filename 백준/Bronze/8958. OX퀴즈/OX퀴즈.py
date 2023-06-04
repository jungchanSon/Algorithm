data = [input() for _ in range(int(input()))]
for i in data:
    splited = i.split("X")
    ans = 0
    for i in splited:
        l = len(i)
        tmp = [i for i in range(1, l+1)]
        ans += sum(tmp)
    print(ans)