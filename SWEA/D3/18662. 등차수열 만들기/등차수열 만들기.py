T = int(input())
def check_squence(x, y, z):
    if y - x == z - y:
        return True
    else:
        return False


for test_case in range(1, T + 1):
    ans = 0
    a, b, c = map(int, input().split())
    if check_squence(a, b, c):
        print(f"#{test_case} {ans:0.1f}")
        continue
    else:
       
        bb = (a+c)/2
        tmp = abs(bb - b)
        if check_squence(a, bb, c):
            ans = abs(bb - b)
            
        aa = b - (c - b)
        tmp = abs(a - aa)
        if check_squence(aa, b, c):
            if ans == 0:
                ans = tmp
            else:
                ans = min(ans, tmp)
        
        cc = b + (b - a)
        tmp = abs(cc - c)
        
        if check_squence(a, b, cc):
            if ans == 0:
                ans = tmp
            else:
                ans = min(ans, tmp)
        
    print(f"#{test_case} {ans:0.1f}")
