from itertools import combinations
import sys
input = sys.stdin.readline

n, c = list(map(int, input().rsplit()))
weight = list(map(int,input().rsplit()))
ans = 1

arr1 = weight[:n//2] 
arr2 = weight[n//2:]

comb_arr1 = []
comb_arr2 = []
for i in range(len(arr1)+1):
    comb = combinations(arr1, i)
    for i in comb:
        comb_arr1.append(sum(i))
        
for i in range(len(arr2) +1) : 
    comb = combinations(arr2, i)
    for i in comb:
        comb_arr2.append(sum(i))
        
comb_arr1.sort()
for i in comb_arr2:
    l = 0 
    r = len(comb_arr1) - 1;
    if i > c :
        continue
    
    while l <= r:
        m = (l+r ) // 2
        if comb_arr1[m] + i > c :
            r = m - 1
        else: 
            l = m + 1 
    
    ans += r+1

print(ans-1)