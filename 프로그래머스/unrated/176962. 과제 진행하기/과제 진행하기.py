def solution(plans: list):
    def calc_term_min(cur_plan:list, next_plan:list):
        ch, cm = map(int, cur_plan[1].split(":"))
        nh, nm = map(int, next_plan[1].split(":"))
        
        return nh*60 +nm - ch*60 -cm
    answer = []
    plans.sort(key= lambda x: x[1])
    
    stack = []
    
    plans = list(map(lambda x : [x[0], x[1], int(x[2])], plans))
    while plans:
        cur_plan = plans.pop(0)
        
        if plans:
            next_plan = plans[0]
            term_min = calc_term_min(cur_plan, next_plan)
            if term_min >= cur_plan[2]:
                answer.append(cur_plan[0])
                term_min -= cur_plan[2]
                while term_min > 0 and stack:
                    if term_min >= stack[-1][2]:
                        term_min -= stack[-1][2]
                        answer.append(stack.pop()[0]) 
                    else:
                        stack[-1][2] -= term_min
                        break
                
            else:
                stack.append([cur_plan[0], cur_plan[1], cur_plan[2]-term_min]) 

        else:
            answer.append(cur_plan[0])
            break
            
    while stack:
        answer.append(stack.pop()[0])
    return answer