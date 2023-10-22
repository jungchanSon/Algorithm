import itertools

def solution(expression):
    answer = 0
    
    ops = []
    if "-" in expression: ops.append("-")
    if "+" in expression: ops.append("+")
    if "*" in expression: ops.append("*")
    
    if len(ops) == 1:
        return abs(eval(expression))
    elif len(ops) == 3:
        expression = "(("+ expression + "))"
    elif len(ops) == 2:
        expression = "(" + expression + ")"
        
    perm_op = list(itertools.permutations(ops))    
    

    if len(ops) == 2:
        for op in perm_op:
            temp = expression.replace(op[0], ")" + op[0] + "(")
            answer = max(answer, abs(eval(temp)))
    if len(ops) == 3:
        for op in perm_op:
            temp = expression.replace(op[0], "))" + op[0] + "((")
            temp = temp.replace(op[1], ")" + op[1] + "(")
            answer = max(answer, abs(eval(temp)))
    return answer