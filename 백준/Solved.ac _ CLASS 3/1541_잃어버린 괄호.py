import sys
import math
input = sys.stdin.readline

s = list(input().rstrip())

result = []
index = 0
while s:
    op1 = math.inf
    op2 = math.inf
    
    if '-' in s:
        op1 = s.index('-')    
    if '+' in s:
        op2 = s.index('+')
    
    if op1 != math.inf or op2 != math.inf:
        temp = "".join(s[0:min(op1, op2)])
        result.append(int(temp))
        result.append(s[min(op1, op2)])
        s = s[min(op1, op2) + 1:]
    else :
        result.append(int("".join(s)))
        s = 0
    
cal = ""
index = 0
check = False
while result:
    c = result.pop(0)
    if type(c) == int:
        cal += str(c)
    elif c == "-" and check == False:
        cal += "-("
        check = True
    elif c == "-" and check == True:
        cal += ")-("
    elif c == "+":
        cal += "+"
if check :
    cal += ")"
print(eval(cal) )
