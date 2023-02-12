import sys
import math
input = sys.stdin.readline

data = list(input().rstrip())
stack = []

for i in data:
    if ord(i) >= 65 and ord(i) <= 90:
        print(i, end="")
    else:
        if i == ")":
            while stack and stack[-1] != "(":
                print(stack.pop(), end = "")
            stack.pop()
            
        else:
            if i != "(":
                if i == "+" or i == "-":
                    while stack and (stack[-1] != "("):
                            print(stack.pop(), end = "")
                else:
                    while stack and ( stack[-1] == "*" or stack[-1] == "/"):
                            print(stack.pop(), end = "")
                
            stack.append(i)
while stack:
    print(stack.pop(), end = "")

#참고 : https://nahwasa.com/entry/%EB%B0%B1%EC%A4%80-1918-%EC%9E%90%EB%B0%94-%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EC%8B%9D-boj-1918-java