T = int(input())
def check_str(s:str):
    if s[::-1] == s:
        return True
    else:
        return False
for test_case in range(1, T + 1):
    target = input()
    n = len(target)
    pv = (n-1)//2
    l = target[:pv]
    r = target[n-pv:]
    
    if check_str(l) and check_str(r) and check_str(target):
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")