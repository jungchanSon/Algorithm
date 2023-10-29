import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().rsplit())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

ans = 2000000001
for i in range(n):
    s = i
    e = len(arr)
    while s < e:
        mid = (s+e) // 2
        if abs(arr[mid]- arr[i]) == m:
            print(m)
            quit()
            
        elif abs(arr[mid]-arr[i]) > m :
            e = mid 
            ans = min(ans, abs(arr[mid]-arr[i]))
        else:
            s = mid + 1
print(ans)