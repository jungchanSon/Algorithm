import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stacks = [[], [], []]
print(2**n -1)
def rec(a, b, c):
    if c == 0:
        return
    rec(a, 3-a-b, c-1)
    print(a+1, b+1)
    rec(3-a-b, b, c-1)

rec(0, 2, n)