cnt = int(input().rstrip())

for i in range(1, cnt+1):
    s = "{0:>"+str(cnt)+"}"
    print(s.format("*"*i))
