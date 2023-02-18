import sys 
input = sys.stdin.readline

string = input().rstrip()

remove_str = list(input().rstrip())
split_str = list(string)
    
stack = []
length = len(remove_str)
for i in string:
    stack.append(i)
    
    if stack[-length:] == remove_str:
        for i in range(length):
            stack.pop() 

if stack:
    print(*stack, sep="")
else :
    print("FRULA")