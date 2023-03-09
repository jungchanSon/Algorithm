import re
s = input("string >> ").rstrip()
regex = input("regEx >> ").rstrip()
p = re.compile(regex)
print(p.match(s))