# from collections import deque
# def solution(elements):
#     answer = 0
#     ans = set()
#     stack = deque()
    
#     temp = elements + elements
    
#     for i in range(len(elements)):
#         for j in range(len(temp)):
#             ans.add(sum(temp[j:j+i]))

#     return len(set(ans))


# print(solution([7,9,1,1,4]))

from collections import deque
def solution(elements):
    answer = 0
    ans = set()
    stack = deque()

    l = len(elements)
    temp = deque(elements)
    
    for i in range(l):
        for _ in range(l):
            for j in range(i):
                n = temp.popleft()
                stack.append(n)
                
            ans.add(sum(temp))
            
            while(stack):
                temp.append(stack.popleft())

    return len(set(ans))


print(solution([7,9,1,1,4]))