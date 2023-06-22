T = int(input().rstrip())
Ns = [int(input()) for _ in range(T)]

ans = [[] for _ in range(10)]
def calc(s:list):
    result = ""
    for i in range(len(s)):
        if s[i][0] == " ":    
            result += s[i][1]
        else:
            result += s[i]

    return eval(result)
    
def bt(current:list, depth:int, max_depth:int):
    if depth == max_depth:
        if calc(current) == 0:
            ans[max_depth-1].append(current)
        return

    bt(current+["+"+str(depth)], depth+1, max_depth)
    bt(current+["-"+str(depth)], depth+1, max_depth)
    bt(current+[" "+str(depth)], depth+1, max_depth)
    
    # bt(current+[" "+str(depth)], depth+1, max_depth)
    
for i in range(3, 10):
    data = [x for x in range(1, i+1)]
    bt(["1"], 2, i+1)

for i in Ns:
    # n = int(input())
    answer = ans[i]
    answer.sort()
    for i in answer:
        print(*i, sep="")
    print()