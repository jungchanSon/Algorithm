T = int(input())
def check_peramdrom(target: str):
    if target == target[::-1]:
        return True, target
    else:
        return False, target
    
for test_case in range(1, T + 1):
    N, M = map(int, input().rsplit())
    arr = []
    ans = 0
    peram = 0
    for _ in range(N):
        target = input()
        b, t = check_peramdrom(target)
        if b:
            peram = len(t)
        else:
            if t[::-1] in arr:
                ans += len(t) * 2
            else:
                arr.append(t)
    ans += peram
    print(f"#{test_case} {ans}")
