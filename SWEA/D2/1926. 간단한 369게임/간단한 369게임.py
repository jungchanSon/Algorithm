N = int(input())
tmp = ['3', '6', '9']
res = ""
for i in range(1, N+1):
    target = str(i)
    c = False
    for s in target:
        if s in tmp:
            res += "-" 
            c = True
    if c:
        res += " "
        continue
    res += str(i)+" "
    
print(res)