T = int(input())
for test_case in range(1, T + 1):
    tc = "#"+str(test_case)
    ans = 0
    A, B, C = map(int, input().rsplit())
    if C < 3 or B < 2:
        print(tc, -1)
        continue
    
    if B >= C:
        ans = B - C + 1
        B = C -1
        
    if A >= B:
        ans += A - B + 1
   
    print(tc, ans)