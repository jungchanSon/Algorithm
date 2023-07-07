import sys 
input = sys.stdin.readline

n = int(input())
emp_map = dict()

for _ in range(n):
    name, state = input().rsplit()
    emp_map[name] = state

ans = []
for key in emp_map.keys():
    if emp_map[key] == "enter":
        ans.append(key)
        
ans.sort(reverse=True) 
for i in ans:
    print(i)