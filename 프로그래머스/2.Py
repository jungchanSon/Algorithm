from collections import deque 
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    time = 0
    q = deque([0 for _ in range(bridge_length )])
    while truck_weights:
        q.popleft()
        if sum(q) + truck_weights[0] <= weight :
            truck = truck_weights.popleft()
            q.append(truck)
        else :
            q.append(0)
        time += 1
    while sum(q) != 0:
        q.popleft()
        time += 1
    return time


test = [[1, 10, [7,4,5,6]], [1, 100, [10]], [100, 100, [10,10,10,10,10,10,10,10,10,10]]]

for i in test:
    a = solution(i[0], i[1], i[2])
    print(a)