cost = list(map(int, input().rsplit()))

cars = []
for _ in range(3):
    cars.append(list(map(int, input().rsplit())))

cars.sort()
min_time = min(cars, key= lambda x: x[0])[0]
max_time = max(cars, key= lambda x: x[1])[1]

board = [[False for _ in range(min_time, max_time+1)] for _ in range(3)]
for i in range(3):
    cars[i][0] -= min_time
    cars[i][1] -= min_time
    
for i in range(3):
    s, e = cars[i]

    for j in range(s, e):
        board[i][j] = True

ans = 0
for i in range(len(board[0])):
    current_cars = 0
    for j in range(3):
        if board[j][i]:
            current_cars += 1
    ans += cost[current_cars-1]*current_cars
print(ans)