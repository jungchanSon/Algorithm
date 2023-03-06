import sys
import math
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()

ans = [math.inf, []]

for i in range(N):
    l = arr[i]
    m_index = i + 1
    r_index = N - 1

    while m_index < r_index:
        value = l + arr[m_index] + arr[r_index]
        if abs(value) < ans[0]:
            ans[0] = abs(value)
            ans[1] = [l, arr[m_index], arr[r_index]]
            
        if value < 0:
            m_index += 1
        elif value > 0:
            r_index -= 1
        else:
            print(*[l, arr[m_index], arr[r_index]])
            quit()        

print(*(sorted(ans[1])))