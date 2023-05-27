def solution(number, k):
    #시간 초과
    # number = list(number)
    
    # cnt = 0    
    # while cnt < k:
    #     flag = True
    #     for i in range(len(number)-1):
    #         if number[i] < number[i+1]:
    #             number.pop(i)
    #             cnt += 1
    #             flag = False
    #             break
        
    #     if flag:
    #         for i in range(k-cnt):
    #             number.pop()
    #         break
            
    # return "".join(number)
    cnt = 0
    stack = []
    stack.append(number[0])

    for i in number[1:]:
        while stack and stack[-1] < i and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(i)
            
    while cnt < k:
        stack.pop()
        cnt += 1
    return "".join(stack)