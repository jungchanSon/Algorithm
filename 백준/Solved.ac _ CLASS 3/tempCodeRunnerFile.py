import sys
input = sys.stdin.readline

s = list(input().rstrip())


for i in range(len(s)):
    if s[i] == '-':
        s[i] = "-("
        s += ")"

print(eval("".join(s)))

# print(55-(50+40-(50+40-(70+30-(50+40-(50+40-(70+30)))))))
# print(55-(50+40-(50+40-(70+30-50+40-50+40-70+30))))
# print(55-(50+40-(50+40-70+30)))
# print(55-(50+40-50+40-70+30))
# print(55-(50+40-(50+40)-(70+30)))
