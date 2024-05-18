import copy
T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    num, chg = map(int, input().rsplit())
    arr = list(map(int, list(str(num))))
    dp = [[] for _ in range(chg+1)]
    dp[0].append(arr)
    dp_idx = 1
    while chg:
        prev = dp[dp_idx-1]
        for s in prev:
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    ss = s[:]
                    tmp = ss[i]
                    ss[i] = ss[j]
                    ss[j] = tmp
                    if ss not in dp[dp_idx]:
                        dp[dp_idx].append(ss)
                    ss = 0
        chg -= 1
        dp_idx += 1
    for i in dp[-1]:
        tmp = list(map(str, i))
        ans = max(ans, int("".join(tmp)))
    print(f"#{test_case} {ans}")