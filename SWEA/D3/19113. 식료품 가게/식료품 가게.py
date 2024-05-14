T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    pi = list(map(int, input().rsplit()))
    ans = ""
    
    while pi:
        orgin = pi.pop()
        dc = int(orgin*0.75)
        ans = str(dc)+" "+ans
        pi.remove(dc)
        
    print(f"#{test_case} {ans}")