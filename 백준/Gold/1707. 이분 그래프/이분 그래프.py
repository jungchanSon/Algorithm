import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
test_num = int(input())

fail = False

def dfs(cur, cur_color):
    global fail
    
    if v_color[cur] == cur_color * -1:
        fail = True
        return
    if not v_color[cur] : 
        v_color[cur] = cur_color
            
        for i in graph[cur]:
            dfs(i, cur_color*-1)
        
for _ in range(test_num):
    v, e = map(int, input().rsplit())
    graph = [[] for _ in range(v+1)]
    v_color = [0 for _ in range(v+1)]  

    fail = False
    visited = [False for _ in range(v+1)]
            
    for _ in range(e):
        s, e = map(int, input().rsplit())
        graph[s].append(e)
        graph[e].append(s)
        
    cur_color = 1
            
    for i in range(1, v+1):
        if not v_color[i] and graph[i]:
            dfs(i, cur_color)
            if fail == True:
                break
            
    if fail:
        print("NO")
    else:
        print("YES")
