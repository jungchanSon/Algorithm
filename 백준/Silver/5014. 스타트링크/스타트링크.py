import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().rsplit())

arr = [-1 for _ in range(F+1)]
arr[S] = 1
dy = [U, -1 * D]

q = [(S, 0)]
arr[S] = 0
while q:
    cy, depth = q.pop(0)
    for i in range(2):
        ny = cy + dy[i]
        
        if ny <= 0 or ny > F:
            continue
        if arr[ny] == -1:
            q.append((ny, depth+1))
            arr[ny] = depth+1

if arr[G] != -1:
    print(arr[G])
else:
    print("use the stairs")