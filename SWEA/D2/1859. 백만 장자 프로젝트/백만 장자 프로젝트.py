T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().rsplit()))
    ans = 0
    tmp = []
    mx = arr[-1]
    for i in range(len(arr)-1, -1, -1):
        if mx > arr[i]:
            ans += mx - arr[i]
            
        else:
            mx = arr[i]
            
        
    
    print("#"+str(test_case)+" "+str(ans))