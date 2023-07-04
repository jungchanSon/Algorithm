import sys
input = sys.stdin.readline
data_num = int(input().rstrip())
data = [[int(input()), input().rsplit()] for _ in range(data_num)]

a = set(["a","b"])
b = set(["a", "c"])


for n, mbti in data:
    ans = 1e9
    if n > 32:
        print(0)
        continue
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                temp = len(set(list(mbti[i])) - set(list(mbti[j])))
                temp += len(set(list(mbti[j])) - set(list(mbti[k])))
                temp += len(set(list(mbti[i])) - set(list(mbti[k])))
                ans = min(temp, ans)
    print(ans)